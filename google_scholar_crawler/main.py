from scholarly import scholarly, ProxyGenerator
import logging
from fp.fp import FreeProxy
# import jsonpickle
import json
from datetime import datetime
import os
logging.basicConfig(level=logging.INFO)

try:
    logging.info("Script started")
    proxy = FreeProxy().get()
    logging.info(f"Proxy: {proxy}")
    pg = ProxyGenerator()
    pg.FreeProxies()
    scholarly.use_proxy(pg)

    GOOGLE_SCHOLAR_ID = 'x47f3O4AAAAJ'
    author: dict = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    name = author['name']
    author['updated'] = str(datetime.now())
    author['publications'] = {v['author_pub_id']:v for v in author['publications']}
except Exception as e:
    logging.error(f"Error occurred: {e}")
    raise

os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

print('Create results/gs_data.json Done')


shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

print('Create results/gs_data_shieldsio.json Done')
