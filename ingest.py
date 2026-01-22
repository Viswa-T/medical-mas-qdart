from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from sentence_transformers import SentenceTransformer
import uuid

model = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(":memory:")

COLLECTION_NAME = "medical_records"

if not client.collection_exists(COLLECTION_NAME):
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        ),
    )

with open("data/patients_records.txt", "r") as file:
    records = file.read().split("\n\n")

points = []

for record in records:
    embedding = model.encode(record).tolist()
    points.append(
        PointStruct(
            id=str(uuid.uuid4()),
            vector=embedding,
            payload={"text": record}
        )
    )

client.upsert(
    collection_name=COLLECTION_NAME,
    points=points
)

print("✅ Patient medical records successfully stored in Qdrant.")

