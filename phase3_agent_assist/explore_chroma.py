# phase3_agent_assist/explore_chroma.py

from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

# Setup: same DB path used in ingestion
CHROMA_PATH = "./chroma_store"
COLLECTION_NAME = "agent_assist_docs"

# 1. Connect to ChromaDB
client = PersistentClient(path=CHROMA_PATH)

# 2. Get collection
collection = client.get_collection(COLLECTION_NAME)

# 3. Inspect stored documents
def show_documents():
    print("\n📄 Stored Documents:")
    print("----------------------")
    docs = collection.get()
    for i in range(len(docs["ids"])):
        print(f"🆔 ID: {docs['ids'][i]}")
        print(f"📄 Text: {docs['documents'][i][:120]}...")
        print(f"📎 Metadata: {docs['metadatas'][i]}")
        print("-" * 60)

# 4. Run a sample search query
def run_query():
    query = input("\n🔍 Enter a query to search: ")
    if not query.strip():
        print("⚠️ Empty query. Exiting.")
        return

    results = collection.query(
        query_texts=[query],
        n_results=3,
        include=["documents", "distances", "metadatas"]
    )

    print("\n🔎 Top Matches:")
    print("----------------------")
    for i in range(len(results["documents"][0])):
        print(f"Rank {i+1}")
        print(f"📄 Text: {results['documents'][0][i][:120]}...")
        print(f"📎 Metadata: {results['metadatas'][0][i]}")
        print(f"📐 Distance Score: {results['distances'][0][i]:.4f}")
        print("-" * 60)

if __name__ == "__main__":
    print("📂 ChromaDB Inspector")
    print("=====================")

    try:
        show_documents()
        run_query()
    except Exception as e:
        print(f"❌ Error: {e}")
