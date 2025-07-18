# 🐍 python.md — Python in llm-cti-playground

## 🔍 What is Python?

Python is a high-level, interpreted programming language known for its readability and vast ecosystem of libraries. It's widely used in AI/ML, automation, web development, and scripting tasks.

In this project, Python was the **core glue** that connected everything — from the LLM API calls to UI logic, file handling, audio processing, and more.

---

## 💡 Why We Used Python

- ✅ Easy to write and understand — ideal for rapid prototyping
- ✅ Rich ecosystem of GenAI and NLP libraries (e.g., `transformers`, `chromadb`, `sentence-transformers`)
- ✅ Works well with Streamlit, Ollama APIs, and Whisper models
- ✅ Strong community and open-source support

---

## 🛠️ How We Used Python in This Project

### 1. **LLM Chat Interface** (Phase 1 & 2)

```python
# Using Python's requests module to call local LLM API (Ollama)
import requests

def ask_llm(prompt):
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False
    })
    return res.json()["response"]
```

### 2. **Streamlit Web App** (Phase 2 & 4)

```python
import streamlit as st

st.title("💬 LLM Chat Interface")
user_input = st.text_input("Enter your message:")
if user_input:
    response = ask_llm(user_input)
    st.markdown(response)
```

### 3. **RAG Pipeline (Phase 3)**

```python
from chromadb import Client
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
vector = embedding_model.encode("Your query here")
```

### 4. **Speech-to-Text (Phase 5)**

```python
from pydub import AudioSegment
from faster_whisper import WhisperModel

audio = AudioSegment.from_file("file.mp3")
audio.export("file.wav", format="wav")

model = WhisperModel("base", compute_type="int8")
segments, _ = model.transcribe("file.wav")
```

### 5. **Other Python Features Used**

- Virtual environments (`venv`)
- File I/O for audio processing and logging
- Directory and path handling (`os`, `pathlib`)
- Exception handling (`try`, `except`)
- Modular code structure (functions, script-based entry points)

---

## 📦 Python Libraries Used (by Phase)

| Phase | Libraries |
|-------|-----------|
| 1     | `requests`, `json`, `os` |
| 2     | `streamlit`, `requests` |
| 3     | `chromadb`, `sentence-transformers`, `PyPDF2`, `docx2txt`, `unstructured` |
| 4     | Combines all above |
| 5     | `pydub`, `faster-whisper`, `speechrecognition`, `ffmpeg`, `os`, `wave` |

---

## 🧠 Tips

- Use `requirements.txt` to lock dependencies.
- Use `venv` to isolate environments:  
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- Install dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

---

> Python was the backbone of this project, powering everything from backend logic to speech and vector search.