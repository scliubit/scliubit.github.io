from scholarly import scholarly, ProxyGenerator
from fp.fp import FreeProxy
import logging
import time
import json
from datetime import datetime
import os

logging.basicConfig(level=logging.INFO)

MAX_RETRIES = 10
RETRY_DELAY = 30  # seconds
GOOGLE_SCHOLAR_ID = os.environ.get('GOOGLE_SCHOLAR_ID', 'x47f3O4AAAAJ')

author = None
for attempt in range(MAX_RETRIES):
    try:
        logging.info(f"Attempt {attempt + 1}/{MAX_RETRIES}: fetching a new proxy...")

        # Get a single fresh proxy explicitly each attempt
        proxy_url = FreeProxy(rand=True, timeout=5, https=True).get()
        logging.info(f"Using proxy: {proxy_url}")

        # Reset proxy before each attempt
        scholarly.use_proxy(None)
        pg = ProxyGenerator()
        pg.SingleProxy(http=proxy_url, https=proxy_url)
        scholarly.use_proxy(pg)

        author = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
        logging.info(f"Success on attempt {attempt + 1}")
        break
    except Exception as e:
        logging.warning(f"Attempt {attempt + 1} failed: {e}")
        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_DELAY)

if author is None:
    raise RuntimeError(f"Failed to fetch Google Scholar data after {MAX_RETRIES} attempts")

scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']: v for v in author['publications']}

os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)
logging.info('Created results/gs_data.json')

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author['citedby']}",
}
with open('results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
logging.info('Created results/gs_data_shieldsio.json')
