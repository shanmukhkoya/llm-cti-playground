import os
from typing import List
import chromadb
from sentence_transformers import SentenceTransformer
import subprocess
import threading
import itertools
import sys
import time

# === Initialize ChromaDB client ===
client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_collection(name="agent_assist_docs")

# === Initialize embedding model ===
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# === Spinner while LLM is generating ===
class Spinner:
    def __init__(self, message="Thinking... "):
        self.spinner = itertools.cycle(['|', '/', '-', '\\'])
        self.running = False
        self.thread = None
        self.message = message

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._spin)
        self.thread.start()

    def _spin(self):
        while self.running:
            sys.stdout.write(f"\r{self.message}" + next(self.spinner))
            sys.stdout.flush()
            time.sleep(0.1)

    def stop(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()
        sys.stdout.write('\r' + ' ' * (len(self.message) + 4) + '\r')
        sys.stdout.flush()

# === Retrieve context from vector DB ===
def search_similar_docs(query: str, top_k: int = 5) -> List[str]:
    query_embedding = embedder.encode([query]).tolist()
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k,
        include=["documents", "metadatas"]
    )
    docs = results['documents'][0]
    return docs

# === Build prompt from context + chat history ===
def generate_answer_with_ollama(context: List[str], chat_history: List[str], query: str) -> str:
    context_text = "\n---\n".join(context)
    history_text = "\n".join(chat_history[-6:])  # Keep last 6 turns to stay in context window
    prompt = f"""You are a helpful contact center assistant.

Context:
{context_text}

Conversation so far:
{history_text}
User: {query}
Assistant:"""

    cmd = ["ollama", "run", "tinyllama"]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = proc.communicate(input=prompt)

    if proc.returncode != 0:
        raise RuntimeError(f"Ollama CLI error: {stderr.strip()}")

    return stdout.strip()

# === CLI Loop ===
def main():
    print("🧠 Agent Assist Chat (RAG + Memory Enabled)\n")
    chat_history = []

    while True:
        query = input("You: ").strip()
        if query.lower() in ("exit", "quit"):
            break
        try:
            docs = search_similar_docs(query)
            if not docs:
                print("No relevant documents found.")
                continue

            spinner = Spinner("🤖 Thinking... ")
            spinner.start()
            answer = generate_answer_with_ollama(docs, chat_history, query)
            spinner.stop()

            print(f"\nLLM: {answer}\n")

            # Update chat history
            chat_history.append(f"User: {query}")
            chat_history.append(f"Assistant: {answer}")

        except Exception as e:
            print(f"[Error] {e}")

if __name__ == "__main__":
    main()
