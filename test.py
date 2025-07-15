# import requests
# resp = requests.post('http://localhost:8001/vectorize/', json={'texts': ["Hello world"]})
# print('Status:', resp.status_code)
# print('Headers:', resp.headers)
# print('Text:', resp.text)
# try:
#     print('JSON:', resp.json())
# except Exception as e:
#     print('JSON decode error:', e)


import os
import pinecone

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENV = os.getenv('PINECONE_ENV')
PINECONE_INDEX = os.getenv('PINECONE_INDEX')

# Initialize Pinecone (new API)
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
index = pc.Index(PINECONE_INDEX)
# ids = ['pen', 'pencil']  # replace with your actual IDs
# result = index.fetch(ids=ids)
print(index.describe_index_stats())