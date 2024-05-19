import os
from elasticsearch import Elasticsearch


ELASTIC_USERNAME = 'elastic'
ELASTIC_PASSWORD = '12345'
ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST') or '10.98.30.107'


    
class ElasticSearchService:
    def __init__(self):
        print("connected to elasticsearch service")

    def search(self, name):
        
        client = Elasticsearch(f'https://{ELASTICSEARCH_HOST}:9200',http_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD),verify_certs=False)
        res = client.search(index="your_index_name", query={
            "match": {
                "Series_Title": name
            }
        })
        client.close()
        return res['hits'], res['hits']['hits']