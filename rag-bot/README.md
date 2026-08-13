ingest.py — reads .md/.txt files from a ./docs folder, chunks them (sliding window, ~500 chars with overlap), writes chunks.json

embed.py — loads chunks.json, embeds and stores into a persistent Chroma collection (./chroma_db)

test_query.py — interactive console: retrieves top-k chunks for a question, builds a grounded prompt, calls Claude, shows both the answer and the retrieved chunks for eval