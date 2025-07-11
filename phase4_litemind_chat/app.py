# phase4_litemind_chat/app.py

import streamlit as st
import time
import requests
import json
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# ------------------ LLM + Chroma Setup ------------------ #

OLLAMA_API_URL = "http://localhost:11434"
embedder = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_collection("agent_assist_docs")

def retrieve_docs(query, n_results=5):
    query_embedding = embedder.encode([query])[0].tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents"]
    )
    return results['documents'][0] if results and 'documents' in results else []

def ask_ollama(prompt):
    try:
        response = requests.post(
            f"{OLLAMA_API_URL}/api/generate",
            headers={"Content-Type": "application/json"},
            json={"model": "tinyllama", "prompt": prompt, "stream": False},
            timeout=60
        )
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"[Error] Ollama API: {e}"

# ------------------ Streamlit Setup ------------------ #

st.set_page_config(page_title="LiteMind Chat", layout="centered", initial_sidebar_state="auto")

# Session state init
if "history" not in st.session_state:
    st.session_state.history = []
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Apply Dark Mode
if st.session_state.dark_mode:
    st.markdown("""
    <style>
    body, .stApp { background-color: #121212; color: #ffffff; }
    .stTextInput > div > input, .stTextArea textarea {
        background-color: #1e1e1e;
        color: #ffffff;
        border: 1px solid #333333;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Controls
with st.sidebar:
    st.title("⚙️ Settings")
    if st.button("🧹 Clear Chat"):
        st.session_state.history = []
    st.session_state.dark_mode = st.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode)
    st.session_state.debug = st.checkbox("🔍 Show Retrieved Context", value=False)

# Main Title
st.title("🤖 LiteMind Chat — Agent Assist RAG")

# Chat History Display
chat_container = st.container()
input_container = st.container()

with chat_container:
    for role, msg in st.session_state.history:
        with st.chat_message(role):
            st.markdown(msg)

# Chat Input
with input_container:
    user_input = st.chat_input("Ask your document...")

    if user_input:
        st.session_state.history.append(("user", user_input))
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                context_docs = retrieve_docs(user_input)

                if st.session_state.debug:
                    st.markdown("**🔍 Retrieved Context:**")
                    for doc in context_docs:
                        st.markdown(f"> {doc[:300]}...")

                context = "\n\n".join(context_docs)
                prompt = f"""
Context:
{context}

User: {user_input}
Assistant:"""
                reply = ask_ollama(prompt)
                st.markdown(reply)
                st.session_state.history.append(("assistant", reply))

# Auto Scroll to Bottom
st.markdown("""
<script>
const chatContainer = window.parent.document.querySelector('.main');
if (chatContainer) chatContainer.scrollTo(0, chatContainer.scrollHeight);
</script>
""", unsafe_allow_html=True)
