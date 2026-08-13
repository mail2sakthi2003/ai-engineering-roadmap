from chromadb import PersistentClient
from chromadb.utils import embedding_functions
from ingest import load_documents, chunk_documents

def build_vector_store():
    # Same embedder as foundations/test_chroma.py — consistent across the whole roadmap
    embedder = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

    # Persisted to disk right inside this project folder
    client = PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(
        name="personal_knowledge",
        embedding_function=embedder
    )

    docs = load_documents()
    chunks = chunk_documents(docs)

    # chunk_id doubles as the Chroma document id — running this script twice
    # won't create duplicates, it just re-adds the same ids (same idea as Day 4)
    collection.add(
        documents=[c["text"] for c in chunks],
        metadatas=[{"source": c["source"]} for c in chunks],
        ids=[c["chunk_id"] for c in chunks],
    )

    print(f"Vector store now has {collection.count()} chunks embedded.")
    return collection

if __name__ == "__main__":
    build_vector_store()