# Replace everything at the top with this up to the "Form"

import streamlit as st
import time

st.set_page_config(page_title="LiteMind Chat", page_icon="🤖", layout="centered")
st.title("🤖 LiteMind Chat — Agent Assist Powered by TinyLLaMA + RAG")

# Chat input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask your question here...", "")
    submit_button = st.form_submit_button("Send")

if submit_button:
    with st.spinner("Thinking..."):
        time.sleep(2)  # simulate thinking
        st.markdown(f"**You:** {user_input}")
        st.markdown(f"**LiteMind Chat:** You asked: {user_input}")
