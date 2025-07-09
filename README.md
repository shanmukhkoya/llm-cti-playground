````markdown
# llm-cti-playground

An interactive, modular GenAI playground designed to explore Large Language Models (LLMs) hands-on, tailored for Contact Center Integration (CTI) solutions architects. This project is structured in phases, each focusing on core GenAI concepts and practical use cases with easy-to-follow steps and lightweight dependencies.

---

## Model Choice and Setup Instructions

### Why TinyLLaMA is Our Priority Model

- **Lightweight and Fast:** At ~637 MB, TinyLLaMA runs smoothly on limited resource environments like WSL and cloud PCs without GPU.
- **Low Friction:** Requires minimal setup and no special hardware or cloud access.
- **Ideal for Learning:** Enables quick iterations and hands-on exploration of LLM concepts without long waits.
- **Future-Proof:** Uses the Ollama CLI and API interface, making it easy to switch to larger models (like Mistral or Llama 3) without changing code.
- **Expandable:** You can seamlessly upgrade to stronger models later.

### How to Setup Ollama and Models

1. **Install Ollama CLI**  
   Follow the official instructions here: [https://ollama.com/download](https://ollama.com/download)

2. **Pull TinyLLaMA Model**  
   ```bash
   ollama pull tinyllama
````

3. **Run TinyLLaMA Model**

   ```bash
   ollama run tinyllama
   ```

4. **Switch to Another Model (Optional)**

   ```bash
   ollama pull mistral
   ollama run mistral
   ```

---

## Project Phases Overview

Each phase is an independent module focusing on a specific capability. You can run and explore them separately.

---

### Phase 1: CLI LLM Interaction

**Purpose:**
Get familiar with basic LLM text interactions via CLI. Send prompts and receive text responses in your terminal.

**Folder:** `phase1_llm_core`

**How to Run:**

```bash
python chat_cli.py
```

**Details:**

* Uses Ollama CLI to send prompt to TinyLLaMA model.
* Demonstrates basic prompt-response cycle.

---

### Phase 2: Streamlit Chat UI

**Purpose:**
Introduce a web-based chat interface for interactive conversation with the LLM.

**Folder:** `phase2_chat_ui`

**How to Run:**

```bash
streamlit run app.py
```

**Details:**

* Provides a simple chat UI in browser.
* Connects to the same Ollama backend as Phase 1.
* Improves user experience with a friendly GUI.

---

### Phase 3: Agent Assist with Retrieval-Augmented Generation (RAG)

**Purpose:**
Implement RAG architecture that combines document retrieval with LLM for context-aware responses, tailored for contact center use cases.

**Folder:** `phase3_agent_assist`

**How to Run:**

1. Ingest documents (PDF, DOCX, TXT) into vector store:

   ```bash
   python ingest.py
   ```
2. Run query app to ask questions based on uploaded documents:

   ```bash
   python rag_chain.py
   ```

**Details:**

* Uses ChromaDB vector store with Sentence Transformers for embedding.
* Retrieves relevant document chunks to supply context to LLM, improving answer accuracy.
* Demo use case: Agent Assist for contact center knowledge base.

---

### Phase 4: LiteMind Chat - Streamlit UI with RAG Integration

**Purpose:**
A polished Streamlit web chat interface that leverages RAG backend to answer user queries using uploaded documents and LLM.

**Folder:** `phase4_litemind_chat`

**How to Run:**

```bash
streamlit run app.py
```

**Details:**

* Combines Phase 2 UI and Phase 3 RAG logic.
* Shows thinking indicator while querying.
* Supports chat history to maintain conversation context.
* Displays context-based answers from your documents.

---

## Additional Notes

* **Document Formats Supported:** PDF, DOCX, TXT (others may require extensions).
* **Vector Store Persistence:** Stored locally under `chroma_store` (ignored by git).
* **Model API:** Ollama runs as a local server. Keep it running while using the app.
* **Environment:** Uses Python `venv` for isolated dependencies.
* **Recommended Python Version:** 3.10 or later.

---

## Getting Started

1. Clone the repository
2. Create and activate virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Install and run Ollama with TinyLLaMA
5. Explore each phase independently by navigating to respective folders and running the provided commands.

---

## Project Structure

```
llm-cti-playground/
├── phase1_llm_core/       # CLI interaction scripts
├── phase2_chat_ui/        # Streamlit chat UI
├── phase3_agent_assist/   # RAG ingestion and query
├── phase4_litemind_chat/  # Streamlit chat UI with RAG backend
├── requirements.txt
├── README.md
├── vision.md
├── .gitignore
└── chroma_store/          # Local vector DB storage (gitignored)
```

---
