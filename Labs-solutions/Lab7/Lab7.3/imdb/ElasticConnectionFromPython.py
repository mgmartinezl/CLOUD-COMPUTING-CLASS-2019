from elasticsearch import Elasticsearch, helpers
import os
import uuid
import json

ELASTIC_API_URL_HOST = os.environ['ELASTIC_API_URL_HOST']
ELASTIC_API_URL_PORT = os.environ['ELASTIC_API_URL_PORT']
ELASTIC_API_USERNAME = os.environ['ELASTIC_API_USERNAME']
ELASTIC_API_PASSWORD = os.environ['ELASTIC_API_PASSWORD']

es = Elasticsearch(host=ELASTIC_API_URL_HOST,
                   scheme='https',
                   port=ELASTIC_API_URL_PORT,
                   http_auth=(ELASTIC_API_USERNAME, ELASTIC_API_PASSWORD))

count = 1
for file in os.listdir("C:\\Users\\gabim\\PycharmProjects\\elasticsearchScraper"):
    if file.endswith('.json'):
        json_file = open(file).read()
        print(json_file)
        data = json.loads(json_file)
        if len(data)>1:
            for d in data:
                es.index(index='imdb', doc_type='json', id=uuid.uuid4(), body=d)

es.indices.refresh(index='imdb')

if es.indices.exists(index="imdb"):
    print("idbm index exists!")
