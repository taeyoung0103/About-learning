from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

def bank_get2():
    res = es.search(index="bank", body={"query": { "match": { "bank": "국민은행" }}, "size": 0, "aggs": { "b_1": {"terms": { "field": "customers"}}}})
    datas = res['aggregations']['b_1']['buckets']
    return datas


# 단위 test용 코드 
# if __name__== "__main__":
#     bank_get2()
