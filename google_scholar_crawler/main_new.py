#!/usr/bin/env python3
"""Fetch Google Scholar author data and write results/gs_data*.json.

Replacement for main.py. Compared with the old script:
- reads GOOGLE_SCHOLAR_ID from the environment (falls back to a default)
- auto mode: tries a direct connection first, then falls back to rotating
  free proxies (direct is fast when it works, e.g. local runs; CI runners
  are often blocked by Scholar and need the proxy path)
- fixes scholarly's proxy health-check mapping and free-proxy refresh calls
- keeps proxy rotation in the outer loop, re-binds both sessions after each
  rotation, and fails fast on captchas so retries remain bounded
- validates the author identity and payload before touching existing results
- writes output atomically and exits non-zero on failure so CI shows red
  instead of silently keeping stale data
"""

import argparse
import json
import logging
import os
import sys
import tempfile
import time
from datetime import datetime, timezone

from fp.fp import FreeProxy
from scholarly import ProxyGenerator, scholarly

MAX_RETRIES = 10
RETRY_DELAY = 60  # seconds between direct-connection retries
DEFAULT_SCHOLAR_ID = "x47f3O4AAAAJ"
FILL_SECTIONS = ["basics", "indices", "counts", "publications"]

RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger("scholar-crawler")


class CaptchaDetected(RuntimeError):
    pass


class ManagedProxyGenerator(ProxyGenerator):
    """Apply dependency compatibility fixes and leave rotation to the caller."""

    def _check_proxy(self, proxies) -> bool:
        request_proxies = {}
        for scheme in ("http", "https"):
            proxy = proxies.get(scheme) or proxies.get(f"{scheme}://")
            if proxy:
                request_proxies[scheme] = proxy
        return super()._check_proxy(request_proxies)

    def _fp_coroutine(self, timeout=1, wait_time=120):
        freeproxy = FreeProxy(rand=False, timeout=timeout)
        if not hasattr(self, "_dirty_freeproxies"):
            self._dirty_freeproxies = set()
        all_proxies = freeproxy.get_proxy_list(repeat=False)
        all_proxies.reverse()

        t1 = time.time()
        while time.time() - t1 < wait_time:
            proxy = all_proxies.pop()
            if not all_proxies:
                all_proxies = freeproxy.get_proxy_list(repeat=True)
                all_proxies.reverse()
            if proxy in self._dirty_freeproxies:
                continue
            proxies = {"http://": proxy, "https://": proxy}
            proxy_works = self._check_proxy(proxies)
            if proxy_works:
                dirty_proxy = yield proxy
                t1 = time.time()
            else:
                dirty_proxy = proxy
            self._dirty_freeproxies.add(dirty_proxy)

    def _handle_captcha2(self, url):
        raise CaptchaDetected("Google Scholar requested a captcha")

    def get_next_proxy(self, num_tries=None, old_timeout=3, old_proxy=None):
        return self._session, old_timeout

    def rotate(self, num_tries=None, old_timeout=3, old_proxy=None):
        return super().get_next_proxy(
            num_tries=num_tries,
            old_timeout=old_timeout,
            old_proxy=old_proxy,
        )


def bind_proxy_generator(pg: ManagedProxyGenerator) -> None:
    scholarly.set_retries(1)
    scholarly.use_proxy(pg, pg)


def fetch_author_once(scholar_id: str) -> dict:
    author = scholarly.search_author_id(scholar_id)
    return scholarly.fill(author, sections=FILL_SECTIONS)


def fetch_author_direct(scholar_id: str, retries: int):
    bind_proxy_generator(ManagedProxyGenerator())
    for attempt in range(1, retries + 1):
        try:
            author = fetch_author_once(scholar_id)
            log.info("Direct fetch succeeded on attempt %d/%d", attempt, retries)
            return author
        except Exception as e:
            log.warning("Direct attempt %d/%d failed: %s", attempt, retries, e)
            if attempt < retries:
                time.sleep(RETRY_DELAY)
    return None


def current_proxy(pg: ProxyGenerator):
    return pg._proxies.get("http://") or pg._proxies.get("http")


def rotate_proxy(pg: ManagedProxyGenerator, num_tries: int) -> None:
    old = current_proxy(pg)
    raw = old.split("://", 1)[-1] if old else None
    pg.rotate(num_tries=num_tries, old_proxy=raw)
    bind_proxy_generator(pg)


def fetch_author_via_proxies(scholar_id: str, retries: int):
    pg = ManagedProxyGenerator()
    pg.FreeProxies()
    bind_proxy_generator(pg)

    last_err = None
    for attempt in range(1, retries + 1):
        log.info("Proxy attempt %d/%d via %s", attempt, retries, current_proxy(pg))
        try:
            author = fetch_author_once(scholar_id)
            log.info("Proxy fetch succeeded on attempt %d/%d", attempt, retries)
            return author
        except Exception as e:
            last_err = e
            log.warning("Proxy attempt %d/%d failed: %s", attempt, retries, e)
            if attempt < retries:
                try:
                    rotate_proxy(pg, attempt)
                except Exception as re:
                    log.warning("Proxy rotation failed: %s", re)
                    break
    if last_err is not None:
        raise last_err
    return None


def validate(author: dict, expected_scholar_id: str) -> None:
    if not isinstance(author, dict):
        raise ValueError("payload is not an object")
    missing = [
        k for k in ("name", "scholar_id", "citedby", "publications")
        if k not in author
    ]
    if missing:
        raise ValueError(f"payload missing keys: {missing}")
    if not isinstance(author["name"], str) or not author["name"].strip():
        raise ValueError("author name is empty")
    if author["scholar_id"] != expected_scholar_id:
        raise ValueError(
            f"author id mismatch: requested {expected_scholar_id!r}, "
            f"got {author['scholar_id']!r}"
        )
    citedby = author["citedby"]
    if isinstance(citedby, bool) or not isinstance(citedby, int) or citedby < 0:
        raise ValueError(f"suspicious citedby value: {citedby!r}")

    publications = author["publications"]
    if not isinstance(publications, list) or not publications:
        raise ValueError("publications must be a non-empty list")
    publication_ids = []
    for index, publication in enumerate(publications):
        if not isinstance(publication, dict):
            raise ValueError(f"publication {index} is not an object")
        publication_id = publication.get("author_pub_id")
        if not isinstance(publication_id, str) or not publication_id.strip():
            raise ValueError(f"publication {index} has no author_pub_id")
        publication_ids.append(publication_id)
    if len(set(publication_ids)) != len(publication_ids):
        raise ValueError("publications contain duplicate author_pub_id values")


def write_json_atomic(path: str, data: dict) -> None:
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(data, f, ensure_ascii=False)
        os.replace(tmp, path)
    except BaseException:
        os.unlink(tmp)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=["auto", "direct", "proxy"],
        default="auto",
        help="auto: try direct once, then fall back to rotating free proxies "
             "(default); direct: only direct connection; proxy: only proxies",
    )
    args = parser.parse_args()

    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip() or DEFAULT_SCHOLAR_ID
    log.info("Fetching scholar id %s (mode=%s)", scholar_id, args.mode)

    author = None
    if args.mode in ("auto", "direct"):
        direct_tries = 1 if args.mode == "auto" else MAX_RETRIES
        author = fetch_author_direct(scholar_id, direct_tries)

    if author is None and args.mode in ("auto", "proxy"):
        try:
            author = fetch_author_via_proxies(scholar_id, MAX_RETRIES)
        except Exception as e:
            log.error("All proxy attempts failed: %s", e)

    if author is None:
        log.error("Fetch failed; keeping existing results")
        return 1

    try:
        validate(author, scholar_id)
    except ValueError as e:
        log.error("Fetched data failed validation: %s; keeping existing results", e)
        return 1

    author["updated"] = str(datetime.now(timezone.utc))
    author["publications"] = {
        v["author_pub_id"]: v for v in author["publications"]
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    data_path = os.path.join(RESULTS_DIR, "gs_data.json")
    write_json_atomic(data_path, author)
    log.info("Wrote %s (citedby=%d, %d publications)",
             data_path, author["citedby"], len(author["publications"]))

    shieldsio = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
    }
    shields_path = os.path.join(RESULTS_DIR, "gs_data_shieldsio.json")
    write_json_atomic(shields_path, shieldsio)
    log.info("Wrote %s", shields_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
