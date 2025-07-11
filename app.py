import streamlit as st
import requests
import time

st.set_page_config(page_title="LiteMind Chat", layout="centered", initial_sidebar_state="auto")

# Session state setup
if "messages" not in st.session_state:
    st.session_state.messages = []
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Apply dark mode CSS
if st.session_state.dark_mode:
    dark_mode_css = """
    <style>
    body, .stApp { background-color: #121212; color: #ffffff; }
    .stTextInput > div > input, .stTextArea textarea {
        background-color: #1e1e1e;
        color: #ffffff;
        border: 1px solid #333333;
    }
    .stChatMessage {
        background-color: #1e1e1e;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
    }
    </style>
    """
    st.markdown(dark_mode_css, unsafe_allow_html=True)

# Sidebar settings
with st.sidebar:
    st.title("⚙️ Settings")
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
    st.session_state.dark_mode = st.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode)

st.title("💬 LiteMind Chat")

# Display chat history in container
chat_placeholder = st.container()
with chat_placeholder:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Input field at the bottom of the screen
prompt = st.chat_input("Type your question here...")

# Process user input
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with chat_placeholder:
        with st.chat_message("user"):
            st.markdown(prompt)

    with chat_placeholder:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = requests.post(
                        "http://localhost:11434/api/generate",
                        json={"model": "tinyllama", "prompt": prompt, "stream": False},
                        timeout=60,
                    )
                    response.raise_for_status()
                    output = response.json()["response"]
                except requests.exceptions.RequestException as e:
                    output = f"[Error] Ollama API: {e}"
                st.markdown(output)
                st.session_state.messages.append({"role": "assistant", "content": output})

# Auto-scroll to bottom
st.markdown(
    """
    <script>
        const chatContainer = window.parent.document.querySelector('.main');
        function scrollToBottom() {
            if (chatContainer) {
                chatContainer.scrollTop = chatContainer.scrollHeight;
            }
        }
        scrollToBottom();
        window.addEventListener("load", scrollToBottom);
        window.addEventListener("message", scrollToBottom);
    </script>
    """,
    unsafe_allow_html=True
)
