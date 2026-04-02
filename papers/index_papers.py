#!/usr/bin/env python3
"""
Index citation papers into PostgreSQL with pgvector for semantic search.
Usage: python3 index_papers.py
"""

import os
import subprocess
import psycopg2
from psycopg2.extras import execute_values
from sentence_transformers import SentenceTransformer
import re

REFS_DIR = "/scratch/repos/uha/papers/references"
DB_CONN = "dbname=repoindex user=root"
CHUNK_SIZE = 400      # words per chunk
CHUNK_OVERLAP = 50    # word overlap between chunks
MODEL_NAME = "all-MiniLM-L6-v2"  # fast, 384-dim, runs local

PAPERS = {
    "planck2020_cosmological_parameters.pdf":
        "Planck Collaboration 2020 — Planck 2018 results VI: Cosmological parameters",
    "riess2022_H0_shoes.pdf":
        "Riess et al. 2022 — A Comprehensive Measurement of H0 with SH0ES",
    "brout2022_pantheon_plus.pdf":
        "Brout et al. 2022 — Pantheon+ Analysis: Cosmological Constraints",
    "riess2023_jwst.pdf":
        "Riess et al. 2023 — JWST Observations of Cepheids in SN Ia hosts",
    "freedman2024_trgb_jwst.pdf":
        "Freedman 2024 — Status of the JWST TRGB Hubble Constant",
    "poulin2019_ede.pdf":
        "Poulin et al. 2019 — Early Dark Energy can Resolve the Hubble Tension",
    "desi2024_instrument.pdf":
        "DESI Collaboration 2024 — DESI Instrument Overview",
    "heymans2021_kids1000.pdf":
        "Heymans et al. 2021 — KiDS-1000 Cosmology: Weak gravitational lensing",
    "amon2022_des_y3.pdf":
        "Amon et al. 2022 — DES Y3 Weak Lensing Shape Catalog",
    "aubourg2015_boss_cosmological.pdf":
        "Aubourg et al. 2015 — Cosmological implications of BAO measurements",
    "aylor2019_sounds_discordant.pdf":
        "Aylor et al. 2019 — Sounds Discordant: Classical Distance Ladder vs ΛCDM",
}


def extract_text(pdf_path):
    result = subprocess.run(
        ["pdftotext", "-layout", pdf_path, "-"],
        capture_output=True, text=True, timeout=60
    )
    text = result.stdout
    # Clean up common PDF artifacts
    text = re.sub(r'\f', '\n\n', text)           # form feeds
    text = re.sub(r'-\n(\w)', r'\1', text)        # dehyphenation
    text = re.sub(r'\n{3,}', '\n\n', text)        # excess newlines
    text = re.sub(r' {2,}', ' ', text)            # excess spaces
    return text.strip()


def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks


def setup_db(conn):
    with conn.cursor() as cur:
        cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS citation_papers (
                id SERIAL PRIMARY KEY,
                filename TEXT NOT NULL,
                title TEXT NOT NULL,
                chunk_index INTEGER NOT NULL,
                chunk_text TEXT NOT NULL,
                embedding vector(384),
                UNIQUE(filename, chunk_index)
            );
        """)
        cur.execute("""
            CREATE INDEX IF NOT EXISTS citation_papers_embedding_idx
            ON citation_papers USING ivfflat (embedding vector_cosine_ops)
            WITH (lists = 50);
        """)
        cur.execute("""
            CREATE INDEX IF NOT EXISTS citation_papers_fts_idx
            ON citation_papers USING gin(to_tsvector('english', chunk_text));
        """)
        conn.commit()
    print("Database tables ready.")


def paper_already_indexed(conn, filename):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT COUNT(*) FROM citation_papers WHERE filename = %s",
            (filename,)
        )
        return cur.fetchone()[0] > 0


def index_paper(conn, model, filename, title):
    pdf_path = os.path.join(REFS_DIR, filename)
    if not os.path.exists(pdf_path):
        print(f"  SKIP (not found): {filename}")
        return 0

    if paper_already_indexed(conn, filename):
        print(f"  SKIP (already indexed): {filename}")
        return 0

    print(f"  Extracting text: {filename}")
    text = extract_text(pdf_path)
    if len(text) < 100:
        print(f"  WARN: very little text extracted from {filename}")
        return 0

    chunks = chunk_text(text)
    print(f"  {len(chunks)} chunks, generating embeddings...")
    embeddings = model.encode(chunks, show_progress_bar=False, batch_size=32)

    rows = [
        (filename, title, i, chunk, emb.tolist())
        for i, (chunk, emb) in enumerate(zip(chunks, embeddings))
    ]

    with conn.cursor() as cur:
        execute_values(cur, """
            INSERT INTO citation_papers (filename, title, chunk_index, chunk_text, embedding)
            VALUES %s
            ON CONFLICT (filename, chunk_index) DO NOTHING
        """, rows, template="(%s, %s, %s, %s, %s::vector)")
    conn.commit()
    print(f"  Indexed {len(rows)} chunks.")
    return len(rows)


def search(conn, model, query, top_k=8):
    """Semantic search across all indexed papers."""
    q_emb = model.encode([query])[0].tolist()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT title, chunk_index, chunk_text,
                   1 - (embedding <=> %s::vector) AS score
            FROM citation_papers
            ORDER BY embedding <=> %s::vector
            LIMIT %s
        """, (q_emb, q_emb, top_k))
        return cur.fetchall()


if __name__ == "__main__":
    print(f"Loading model: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)

    conn = psycopg2.connect(DB_CONN)
    setup_db(conn)

    total = 0
    for filename, title in PAPERS.items():
        print(f"\n[{filename}]")
        n = index_paper(conn, model, filename, title)
        total += n

    print(f"\nDone. Total new chunks indexed: {total}")
    conn.close()

    # Quick test search
    print("\n--- Test search: 'inverse distance ladder H0 Omega_m' ---")
    conn = psycopg2.connect(DB_CONN)
    model2 = SentenceTransformer(MODEL_NAME)
    results = search(conn, model2, "inverse distance ladder H0 Omega_m model independent", top_k=5)
    for title, chunk_idx, text, score in results:
        print(f"\n[{score:.3f}] {title} (chunk {chunk_idx})")
        print(text[:300] + "...")
    conn.close()
