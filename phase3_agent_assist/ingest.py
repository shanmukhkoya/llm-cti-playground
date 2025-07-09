import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from PyPDF2 import PdfReader
import docx
import pandas as pd

# ─── Initialize ChromaDB ────────────────────────────────────────────────────────
client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection(name="agent_assist_docs")

# ─── Loaders for Each Format ─────────────────────────────────────────────────────
def load_pdf(path):
    try:
        reader = PdfReader(path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception as e:
        print(f"[!] Failed to load PDF: {path} | Error: {e}")
        return ""

def load_docx(path):
    try:
        doc = docx.Document(path)
        return "\n".join(para.text for para in doc.paragraphs)
    except Exception as e:
        print(f"[!] Failed to load DOCX: {path} | Error: {e}")
        return ""

def load_txt_md(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"[!] Failed to load text file: {path} | Error: {e}")
        return ""

def load_csv(path):
    try:
        df = pd.read_csv(path)
        return "\n".join(df.astype(str).agg(" ".join, axis=1).tolist())
    except Exception as e:
        print(f"[!] Failed to load CSV: {path} | Error: {e}")
        return ""

def load_excel(path):
    try:
        df = pd.read_excel(path, engine="openpyxl")
        return "\n".join(df.astype(str).agg(" ".join, axis=1).tolist())
    except Exception as e:
        print(f"[!] Failed to load Excel: {path} | Error: {e}")
        return ""

# ─── Dispatcher ─────────────────────────────────────────────────────────────────
def load_document(path):
    ext = os.path.splitext(path)[1].lower().replace('.', '')
    if ext == "pdf":
        return load_pdf(path)
    if ext == "docx":
        return load_docx(path)
    if ext in ("txt", "md"):
        return load_txt_md(path)
    if ext == "csv":
        return load_csv(path)
    if ext in ("xls", "xlsx"):
        return load_excel(path)
    raise ValueError(f"Unsupported file type: {ext}")

# ─── Text Splitter ───────────────────────────────────────────────────────────────
def split_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# ─── Ingest Function ────────────────────────────────────────────────────────────
def ingest_directory(directory):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    for fname in os.listdir(directory):
        if ':' in fname:
            print(f"[-] Skipping system file: {fname}")
            continue

        path = os.path.join(directory, fname)
        if not os.path.isfile(path):
            continue

        print(f"[+] Processing: {fname}")
        try:
            text = load_document(path)
        except ValueError as ve:
            print(f"[!] Skipped unsupported file: {fname} | {ve}")
            continue

        if not text.strip():
            print(f"[!] Empty or unreadable: {fname}")
            continue

        chunks = split_text(text)
        embeddings = model.encode(chunks)
        ids = [f"{fname}_{i}" for i in range(len(chunks))]
        metadatas = [{"source": fname} for _ in chunks]

        collection.add(
            documents=chunks,
            embeddings=embeddings.tolist(),
            metadatas=metadatas,
            ids=ids
        )

#    client.persist()
    print("\n[✓] Ingestion complete. Embeddings stored in ./chroma_store")

# ─── Main Entrypoint ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "data")
    ingest_directory(data_path)
