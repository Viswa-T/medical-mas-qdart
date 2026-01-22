from sentence_transformers import SentenceTransformer
from ingest import client, COLLECTION_NAME

model = SentenceTransformer("all-MiniLM-L6-v2")

def search_records(query):
    query_vector = model.encode(query).tolist()

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=3
    )

    return [point.payload["text"] for point in results.points]
