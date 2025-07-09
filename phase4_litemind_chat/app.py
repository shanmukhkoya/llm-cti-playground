# phase4_litemind_chat/app.py

import streamlit as st
import time
import requests
import json
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# Initialize Chroma client & collection (adjust your collection name & path)
client = chromadb.PersistentClient(path="./chroma_store")
collection_name = "agent_assist_docs"
collection = client.get_collection(collection_name)

# Load embedding model for query encoding
embedder = SentenceTransformer('all-MiniLM-L6-v2')

OLLAMA_API_URL = "http://localhost:11434"  # Ollama API default port

# Function: Query ChromaDB with embedding and get top docs
def retrieve_docs(query, n_results=5):
    query_embedding = embedder.encode([query])[0].tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents"]
    )
    docs = results['documents'][0] if results and 'documents' in results else []
    return docs

# Function: Send prompt to Ollama CLI API (replace with your method if needed)
def ask_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            headers={"Content-Type": "application/json"},
            json={
                "model": "tinyllama",
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        data = response.json()
        return data["response"]
    except Exception as e:
        return f"[Error] Ollama API: {e}"

# Streamlit UI layout
st.set_page_config(page_title="LiteMind Chat", page_icon="🤖", layout="centered")

st.title("🤖 LiteMind Chat — Agent Assist Powered by TinyLLaMA + RAG")

# Session state to keep chat history and debug toggle
if "history" not in st.session_state:
    st.session_state.history = []

if "show_debug" not in st.session_state:
    st.session_state.show_debug = False

# Debug toggle checkbox
st.sidebar.checkbox("Show retrieved context (debug)", value=False, key="show_debug")

# Chat input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask your question here...", "")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input.strip():
    with st.spinner("Thinking..."):
        # Retrieve context docs from ChromaDB
        retrieved_docs = retrieve_docs(user_input)
        context_text = "\n\n".join(retrieved_docs) if retrieved_docs else ""

        # Show retrieved docs if debug enabled
        if st.session_state.show_debug:
            st.markdown("**Retrieved documents for context:**")
            for i, doc in enumerate(retrieved_docs):
                st.markdown(f"> {doc}")

        # Construct prompt with context + user query
        prompt = f"""
Context:
{context_text}

User: {user_input}
Assistant:
"""

        # Query Ollama for answer
        answer = ask_ollama(prompt)

        # Update chat history
        st.session_state.history.append(("User", user_input))
        st.session_state.history.append(("LiteMind Chat", answer))

# Display chat history
for speaker, message in st.session_state.history:
    if speaker == "User":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**{speaker}:** {message}")
