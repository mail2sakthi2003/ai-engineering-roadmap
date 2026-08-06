# foundations/test_embeddings.py
from chromadb.utils import embedding_functions
import numpy as np

embedder = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

sentences = [
    "The cloud bill went up unexpectedly this month.",
    "There was an unexpected spike in billing.",
    "The cat sat on the windowsill.",
]

vectors = embedder(sentences)

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print("Sentence 1 vs 2 (should be similar):", cosine_similarity(vectors[0], vectors[1]))
print("Sentence 1 vs 3 (should be different):", cosine_similarity(vectors[0], vectors[2]))