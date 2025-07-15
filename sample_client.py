"""
Sample client script to interact with the Agentic RAG FastAPI services.
"""
import requests

# 1. Ingest PDF
with open('sample.pdf', 'rb') as f:
    files = {'file': ('sample.pdf', f, 'application/pdf')}
    resp = requests.post('http://localhost:8000/ingest_pdf/', files=files)
    pdf_content = resp.json()
    print('PDF Content:', pdf_content)

# 2. Vectorize extracted text (example: only text, but you can use images/tables as needed)
texts = [pdf_content['text']]
resp = requests.post('http://localhost:8001/vectorize/', json={'texts': texts})
embeddings = resp.json()
print('Embeddings:', embeddings)

# 3. Upsert into Pinecone
upsert_payload = {
    'ids': ['doc1'],
    'vectors': embeddings,
    'metadata': [{'source': 'sample.pdf'}]
}
resp = requests.post('http://localhost:8002/upsert/', json=upsert_payload)
print('Upsert response:', resp.json())

# 4. Query Pinecone
query_payload = {
    'vector': embeddings[0],
    'top_k': 3
}
resp = requests.post('http://localhost:8002/query/', json=query_payload)
print('Query results:', resp.json())
