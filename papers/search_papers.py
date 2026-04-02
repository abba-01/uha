#!/usr/bin/env python3
"""
Semantic search across indexed citation papers.
Usage: python3 search_papers.py "your query here" [--top 8]
"""
import sys
import argparse
import psycopg2
from sentence_transformers import SentenceTransformer

DB_CONN = "dbname=repoindex user=root"
MODEL_NAME = "all-MiniLM-L6-v2"

def search(query, top_k=8):
    model = SentenceTransformer(MODEL_NAME)
    q_emb = model.encode([query])[0].tolist()
    conn = psycopg2.connect(DB_CONN)
    with conn.cursor() as cur:
        cur.execute("""
            SELECT title, chunk_index, chunk_text,
                   1 - (embedding <=> %s::vector) AS score
            FROM citation_papers
            ORDER BY embedding <=> %s::vector
            LIMIT %s
        """, (q_emb, q_emb, top_k))
        results = cur.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="+", help="Search query")
    parser.add_argument("--top", type=int, default=5, help="Number of results")
    args = parser.parse_args()
    query = " ".join(args.query)

    print(f"\nQuery: {query}\n{'='*60}")
    results = search(query, top_k=args.top)
    for title, chunk_idx, text, score in results:
        print(f"\n[Score: {score:.3f}] {title}")
        print(f"--- chunk {chunk_idx} ---")
        print(text[:500])
        print()
