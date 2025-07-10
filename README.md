# 💬 llm-cti-playground

An interactive, modular GenAI playground to explore Large Language Models (LLMs) hands-on — tailored for Contact Center Integration (CTI) solution architects. This project is structured into independent **phases**, each teaching core GenAI concepts with minimal setup, clear code, and lightweight dependencies.

---

## 🧠 Model Choice & Setup

### 🚀 Why TinyLLaMA Is Our Priority

- ✅ **Lightweight & Fast**: Just ~637MB, perfect for WSL or cloud PCs.
- ✅ **Low Resource**: Runs without GPU, internet, or external dependencies.
- ✅ **Learning-Friendly**: Ideal for rapid prototyping & understanding LLM internals.
- ✅ **Ollama-Compatible**: Swap to `llama3`, `mistral`, `phi3` easily later.
- ✅ **Scalable**: Upgrade-ready without changing your app code.

---

### 🔧 Setting Up Ollama & Model

1. **Install Ollama**  
   → Follow [https://ollama.com/download](https://ollama.com/download)

2. **Pull & Run TinyLLaMA**

   ```bash
   ollama pull tinyllama
   ollama run tinyllama
   ```

3. **Switch to Another Model (Optional)**

   ```bash
   ollama pull mistral
   ollama run mistral
   ```

---

## 🔍 Project Phases Overview

Each phase is isolated — run and understand them independently or combine them progressively.

---

### 📟 Phase 1: CLI Chat with LLM

- **Folder**: `phase1_llm_core`
- **Goal**: Text-based interaction with TinyLLaMA in terminal.

```bash
python chat_cli.py
```

- Sends prompt → receives response using Ollama's local LLM API.
- Great to understand basic prompt-response flow.

---

### 🌐 Phase 2: Streamlit Chat UI

- **Folder**: `phase2_chat_ui`
- **Goal**: Simple chat web app using Streamlit.

```bash
streamlit run app.py
```

- Replaces terminal with an elegant browser-based UI.
- Keeps backend same (TinyLLaMA via Ollama).

---

### 🧠 Phase 3: RAG for Agent Assist

- **Folder**: `phase3_agent_assist`
- **Goal**: Build Retrieval-Augmented Generation (RAG) engine to power CTI Agent Assist use cases.

#### 📝 Ingest Docs into Vector DB

```bash
python ingest.py
```

#### 🔍 Query LLM with Retrieved Context

```bash
python rag_chain.py
```

- **Supported Files**: `.pdf`, `.docx`, `.txt`
- Uses `ChromaDB` + `Sentence Transformers`
- Retrieves chunks relevant to query before calling the LLM.

---

### 💡 Phase 4: LiteMind Chat (RAG + Streamlit UI)

- **Folder**: `phase4_litemind_chat`
- **Goal**: Unified, production-style app combining RAG + UI.

```bash
streamlit run app.py
```

- 📁 Uses previously ingested documents.
- 🧠 Maintains **chat history** (session memory).
- 🔄 Shows **"thinking..."** while model responds.
- 💬 Feels like a mini ChatGPT trained on your internal docs.

![Phase 4 UI](images/phase4_ui.png)

---

## 📂 Project Structure

```
llm-cti-playground/
├── phase1_llm_core/         # CLI interaction
├── phase2_chat_ui/          # Streamlit chat UI
├── phase3_agent_assist/     # RAG document pipeline
├── phase4_litemind_chat/    # Streamlit + RAG combo
├── chroma_store/            # Chroma vector DB (ignored in Git)
├── venv/                    # Virtual environment
├── images/                  # Screenshots
├── requirements.txt
├── README.md
├── vision.md
└── .gitignore
```

---

## ⚙️ Setup Instructions (Once)

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Ensure Ollama is running TinyLLaMA
ollama run tinyllama
```

---

## 🧠 Extra Notes

- 🧾 **Document Support**: PDF, DOCX, TXT (others can be added)
- 💾 **Persistence**: Vector store in `chroma_store/` (excluded from Git)
- 🧠 **LLM Behavior**: Queries can fallback to model's pretraining if no relevant context is retrieved
- 📦 **Python Version**: Recommended 3.10+

---

## 🤝 Contribute or Extend

- Add more phases like:
  - 📢 **STT / TTS Voice Interface**
  - 🗣️ **LangChain Agent Routing**
  - 📡 **LLM API Gateway for Production**
- Replace `TinyLLaMA` with `phi3`, `llama3`, etc.

---

> Made with ❤️ to help CTI Solution Architects embrace GenAI one phase at a time.
