import elasticsearch as es
import pandas as pd
import json

#Create the instance of the elasticsearch link to "localhost:9200" by default
elastic = es.Elasticsearch(timeout=30)

#Name of the index to create in elasticsearch
index_name = 'women-entrepreneurship'

#Path of the csv ton ingest
csv_path = "Dataset3.csv"

#Create an index in elasticsearch
elastic.indices.create(index=index_name)

#Read and transform the data from csv file to json format
data = pd.read_csv(csv_path, ";")
data_json = data.to_json(orient='records')
data_in_json = json.loads(data_json)

#Push the data in elasticsearch
for i in data_in_json:
    elastic.index(index=index_name, doc_type="places", id=i.pop('No'), body=i)
