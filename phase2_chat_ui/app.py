import streamlit as st
import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "tinyllama"

st.set_page_config(page_title="LLM Chat UI", layout="centered")

st.title("💬 TinyLLaMA - Local Chat")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

prompt = st.chat_input("Type your message here...")

def get_ollama_response(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status()
    return response.json()["response"]

if prompt:
    st.session_state.chat_history.append(("user", prompt))
    try:
        reply = get_ollama_response(prompt)
        st.session_state.chat_history.append(("llm", reply))
    except Exception as e:
        st.error(f"Error: {e}")

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)
