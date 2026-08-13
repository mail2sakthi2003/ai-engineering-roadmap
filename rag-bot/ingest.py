from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

DOCS_DIR = Path(__file__).parent / "docs"

def load_documents():
    """Read every .md and .txt file in docs/, keeping track of which file each came from."""
    documents = []
    for file_path in DOCS_DIR.glob("*"):
        if file_path.suffix in [".md", ".txt"]:
            text = file_path.read_text(encoding="utf-8")
            documents.append({"source": file_path.name, "text": text})
    return documents

def chunk_documents(documents):
    """Split each document into smaller overlapping chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,      # characters per chunk — a few paragraphs
        chunk_overlap=50,    # slight overlap so ideas at chunk boundaries aren't lost
        separators=["\n\n", "\n", ". ", " ", ""],  # tries to split on paragraph breaks first, then sentences, then words — last resort is mid-word
    )

    all_chunks = []
    for doc in documents:
        chunks = splitter.split_text(doc["text"])
        for i, chunk_text in enumerate(chunks):
            all_chunks.append({
                "text": chunk_text,
                "source": doc["source"],
                "chunk_id": f"{doc['source']}_{i}",
            })
    return all_chunks

if __name__ == "__main__":
    docs = load_documents()
    print(f"Loaded {len(docs)} document(s): {[d['source'] for d in docs]}\n")

    chunks = chunk_documents(docs)
    print(f"Split into {len(chunks)} chunks total.\n")

    # Look at a couple of chunks to build intuition for what "chunking" actually produces
    print("--- Example chunk 1 ---")
    print(f"Source: {chunks[0]['source']}")
    print(chunks[0]["text"])
    print(f"\n(length: {len(chunks[0]['text'])} characters)\n")

    print("--- Example chunk 2 ---")
    print(f"Source: {chunks[1]['source']}")
    print(chunks[1]["text"])
    print(f"\n(length: {len(chunks[1]['text'])} characters)")