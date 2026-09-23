#!/usr/bin/env python3
"""Fetch Google Scholar author data and write results/gs_data*.json.

Replacement for main.py. Compared with the old script:
- reads GOOGLE_SCHOLAR_ID from the environment (falls back to a default)
- auto mode: tries a direct connection first, then falls back to rotating
  free proxies (direct is fast when it works, e.g. local runs; CI runners
  are often blocked by Scholar and need the proxy path)
- proxy rotation that actually rotates: a single ProxyGenerator is kept
  across attempts so scholarly's dirty-proxy memory survives, the failing
  proxy is explicitly marked dirty (scholarly's navigator passes the wrong
  dict key and never marks it), and sessions are re-bound after each
  rotation. The old script recreated the ProxyGenerator every retry, which
  reset the dirty set and deterministically re-picked the same proxy.
- validates the payload before touching the existing results
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


def fetch_author_once(scholar_id: str) -> dict:
    author = scholarly.search_author_id(scholar_id)
    return scholarly.fill(author, sections=FILL_SECTIONS)


def fetch_author_direct(scholar_id: str, retries: int):
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
    # scholarly stores proxies under 'http://'/'https://' keys (its navigator
    # mistakenly looks up 'http', which is why its own rotation never marks
    # the failing proxy dirty)
    return pg._proxies.get("http://") or pg._proxies.get("http")


def rotate_proxy(pg: ProxyGenerator, num_tries: int) -> None:
    old = current_proxy(pg)
    # the free-proxy coroutine compares against raw host:port list entries,
    # so strip the scheme before reporting the failed proxy as dirty
    raw = old.split("://", 1)[-1] if old else None
    pg.get_next_proxy(num_tries=num_tries, old_proxy=raw)
    # get_next_proxy builds a NEW session object on pg; re-bind it (and pass
    # pg twice, otherwise use_proxy spawns a hidden secondary ProxyGenerator
    # with its own fresh FreeProxies() for /citations pages)
    scholarly.use_proxy(pg, pg)


def fetch_author_via_proxies(scholar_id: str, retries: int):
    pg = ProxyGenerator()
    pg.FreeProxies()
    scholarly.use_proxy(pg, pg)

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


def validate(author: dict) -> None:
    missing = [k for k in ("name", "citedby", "publications") if k not in author]
    if missing:
        raise ValueError(f"payload missing keys: {missing}")
    if not isinstance(author["citedby"], int) or author["citedby"] < 0:
        raise ValueError(f"suspicious citedby value: {author['citedby']!r}")


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

    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", DEFAULT_SCHOLAR_ID)
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
        validate(author)
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
