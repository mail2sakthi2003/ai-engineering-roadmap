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

# This is sentence-transformers downloading the actual all-MiniLM-L6-v2 model — a small, open-source
# embedding model — from Hugging Face, the first time it's used. It's downloading:

# model weights (the trained numbers that turn text into vectors)
# tokenizer files (vocab.txt, tokenizer.json) — the rules for splitting text into tokens, 
#  same concept as Day 3, but this model has its own tokenizer, separate from Claude's
# config files — metadata about the model architecture

# This only happens once — it's now cached locally (usually in ~/.cache/huggingface or 
# C:\Users\mail2\.cache\huggingface on Windows). Every future run will skip straight to
# loading from disk, no download.

######## OUTPUT
# The actual result — this is the important part
# Sentence 1 vs 2 (should be similar): 0.60491174
# Sentence 1 vs 3 (should be different): 0.1336176

# Remember the sentences:

# "The cloud bill went up unexpectedly this month."
# "There was an unexpected spike in billing."
# "The cat sat on the windowsill."

# Sentence 1 vs 2 scored 0.60 — meaningfully higher similarity — even though they share
# almost no exact words ("bill" is the only real overlap). The model correctly recognized
# these two sentences mean roughly the same thing.

# Sentence 1 vs 3 scored 0.13 — close to zero, correctly recognizing that a cloud billing 
# sentence and a sentence about a cat have nothing to do with each other.

# Why this matters for what you're about to build: this gap — 0.60 vs 0.13 — is literally'
# ' the mechanism RAG retrieval runs on. When you ask your future RAG bot "why did our cloud costs spike?", '
# 'it will embed that question, compare it against every chunk of your documents using this exact same'
# ' cosine-similarity math, and pull back the chunks that score highest — even'
# ' if they don't share your exact wording. You just watched, with real numbers, 
# the core operation your Project A1 bot will run thousands of times.