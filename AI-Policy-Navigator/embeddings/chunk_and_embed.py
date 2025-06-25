# AI Policy Navigator: Text Chunking & Embedding Script

import sys
import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

CHUNK_SIZE = 500  # characters per chunk

# Chunk text into fixed-size pieces
def chunk_text(text, chunk_size=CHUNK_SIZE):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        if chunk.strip():
            chunks.append(chunk.strip())
    return chunks

def main(txt_path, db_dir):
    # Read extracted text
    with open(txt_path, 'r', encoding='utf-8') as f:
        text = f.read()
    chunks = chunk_text(text)
    print(f"Chunked text into {len(chunks)} pieces.")

    # Load embedding model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks, show_progress_bar=True)

    # Set up ChromaDB
    client = chromadb.Client(Settings(persist_directory=db_dir))
    collection = client.get_or_create_collection("policy_chunks")

    # Store chunks and embeddings
    for idx, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        collection.add(
            documents=[chunk],
            embeddings=[emb.tolist()],
            ids=[f"chunk_{idx}"]
        )
    print(f"Stored {len(chunks)} chunks in vector DB at {db_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python chunk_and_embed.py <input.txt> <vector_db_dir>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
