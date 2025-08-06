from scholarly import scholarly, ProxyGenerator
import logging
import time
# from fp.fp import FreeProxy
# import jsonpickle
import json
from datetime import datetime
import os
logging.basicConfig(level=logging.INFO)

MAX_RETRIES = 10
RETRY_DELAY = 60  # seconds
GOOGLE_SCHOLAR_ID = 'x47f3O4AAAAJ'


for _ in range(MAX_RETRIES):
    try:
        logging.info("Script started")
        # proxy = FreeProxy().get()
        # logging.info(f"Proxy: {proxy}")
        pg = ProxyGenerator()
        pg.FreeProxies()
        scholarly.use_proxy(pg)
        author: dict = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
        logging.info(f"Success with {_} attempts")
        break
    except Exception as e:
        logging.warning(f"Failed to set sleep time, retrying... {e}")
        time.sleep(RETRY_DELAY)

scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}

os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

logging.info('Create results/gs_data.json Done')


shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

logging.info('Create results/gs_data_shieldsio.json Done')
