"""
Sample client script to interact with the Agentic RAG FastAPI services.
"""
import requests

# 1. Ingest PDF
with open('sample.pdf', 'rb') as f:
    files = {'file': ('sample.pdf', f, 'application/pdf')}
    resp = requests.post('http://localhost:8000/ingest_pdf/', files=files)
    print('Ingest PDF response:', resp.status_code, resp.text)
    pdf_content = resp.json() if resp.headers.get('content-type', '').startswith('application/json') else {}
    print('PDF Content:', pdf_content)

# 2. Vectorize extracted text (example: only text, but you can use images/tables as needed)
texts = [pdf_content.get('text', '')]
print('Texts to vectorize:', texts)
resp = requests.post('http://localhost:8001/vectorize/', json={'texts': texts})
embeddings = resp.json() if resp.headers.get('content-type', '').startswith('application/json') else []
print('Embeddings:', len(embeddings[0]))

# 3. Upsert into Pinecone
upsert_payload = {
    'ids': ['doc1'],
    'vectors': embeddings,
    'metadata': [{'source': 'sample.pdf'}]
}
resp = requests.post('http://localhost:8002/upsert/', json=upsert_payload)
upsert_result = resp.json() if resp.headers.get('content-type', '').startswith('application/json') else {}
print('Upsert result:', upsert_result)

# 4. Create embedding for a query string
query_text = "rubber"
print('Query text to vectorize:', query_text)
query_embedding_resp = requests.post('http://localhost:8001/vectorize/', json={'texts': [query_text]})
query_embedding = query_embedding_resp.json()[0] if query_embedding_resp.headers.get('content-type', '').startswith('application/json') else None
print('Query embedding:', len(query_embedding))

# 5. Query Pinecone
query_payload = {
    'vector': query_embedding,
    'top_k': 1
}
resp = requests.post('http://localhost:8002/query/', json=query_payload)
# query_result = resp.json() if resp.headers.get('content-type', '').startswith('application/json') else {}
print('Query result done')
