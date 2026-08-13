from chromadb import PersistentClient
from chromadb.utils import embedding_functions

embedder = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
client = PersistentClient(path="./chroma_db")
collection = client.get_collection(name="personal_knowledge", embedding_function=embedder)

query = "Explain about VPC attached mode."
results = collection.query(query_texts=[query], n_results=3)

for doc, dist, meta in zip(results["documents"][0], results["distances"][0], results["metadatas"][0]):
    print(f"[{dist:.4f}] ({meta['source']})")
    print(doc[:150] + "...\n")
