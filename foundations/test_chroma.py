# Hands-On with Chroma (Your Local Vector Database)

# Yesterday you saw the raw math (embeddings + cosine similarity) done by hand. 
# Today you'll see how Chroma wraps that into an actual database — one that stores documents,
# remembers them across runs, and does the similarity search for you automatically.

# Concept: what Chroma actually is

# Think of it like a regular database, but instead of WHERE id = 5, you query
# with WHERE meaning is similar to "X". Under the hood it's doing exactly the embed-and-compare'
# ' math you saw yesterday — it just handles storage, indexing, and persistence so you don't have to.

# Two important pieces:

# PersistentClient — tells Chroma to save everything to a folder on disk (./chroma_db), 
# so your data survives between script runs. (There's also an in-memory client for quick throwaway tests, 
# but we want persistence since this is the DB your RAG bot will actually query next week.)
# Collection — like a table. You can have multiple collections for different projects/purposes.


from chromadb import PersistentClient
from chromadb.utils import embedding_functions

# Same embedder as Day 3 — explicit, so Chroma doesn't fall back to the ONNX default
embedder = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Persistent = saved to disk in ./chroma_db, survives between runs
client = PersistentClient(path="./chroma_db")

# get_or_create = won't error if you run this script twice
collection = client.get_or_create_collection(
    name="cloud_notes",
    embedding_function=embedder
)

# Add some documents — this is where embedding actually happens, automatically
collection.add(
    documents=[
        "AWS RAM lets you share resources like subnets and Transit Gateway attachments across accounts without duplicating infrastructure.",
        "OIDC federated authentication allows CI/CD pipelines to get short-lived credentials without storing long-lived IAM access keys.",
        "IAM and STS role chaining enables cross-account access using AssumeRole for least-privilege architectures.",
        "Terraform modules let you package reusable infrastructure-as-code components for consistent multi-cloud deployments.",
        "Cats are independent animals that sleep up to 16 hours a day.",
    ],
    metadatas=[
        {"source": "aws-notes", "topic": "networking"},
        {"source": "aws-notes", "topic": "auth"},
        {"source": "aws-notes", "topic": "auth"},
        {"source": "terraform-notes", "topic": "iac"},
        {"source": "random", "topic": "unrelated"},
    ],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"]
)

print(f"Collection now has {collection.count()} documents.\n")

# Query — this embeds your question and finds the closest matching documents
results = collection.query(
    #query_texts=["How do I let pipelines authenticate without storing long-lived keys?"],
    query_texts=["I love cat and aeroplanes and want to learn more about them.cats love to sleep."],
    n_results=3
)

print("Top matches:")
for doc, distance, meta in zip(
    results["documents"][0],
    results["distances"][0],
    results["metadatas"][0]
):
    print(f"  [{distance:.4f}] ({meta['topic']}) {doc}")

#     OUTPUT:
#     Top matches:
#   [0.4684] (unrelated) Cats are independent animals that sleep up to 16 hours a day.
#   [0.9384] (networking) AWS RAM lets you share resources like subnets and Transit Gateway attachments across accounts without duplicating infrastructure.
#   [0.9449] (iac) Terraform modules let you package reusable infrastructure-as-code components for consistent multi-cloud deployments.