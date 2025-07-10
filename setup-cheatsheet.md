# 🧠 Python + GenAI Project Setup Cheatsheet

A universal, step-by-step guide to set up any Python-based AI/LLM project including venv, requirements, Streamlit, Ollama, and Git workflows.

---

## 📁 1. Create Project Directory

```bash
mkdir my_project
cd my_project
```

---

## 🐍 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv         # Create venv
source venv/bin/activate     # Linux/macOS
# OR
.\venv\Scripts\activate      # Windows
```

---

## 📦 3. Install Core Dependencies

```bash
pip install --upgrade pip
pip install requests streamlit sentence-transformers chromadb
```

Add more as needed: `pdfplumber`, `langchain`, `pypdf`, etc.

---

## 📄 4. Generate `requirements.txt`

```bash
pipreqs . --force  # Best practice (detects only used libraries)
# OR
pip freeze > requirements.txt  # Full environment (less ideal)
```

---

## 🗂️ 5. Suggested Project Structure

```
my_project/
│
├── venv/
├── phase1_llm_core/
│   └── chat_cli.py
├── phase2_chat_ui/
│   └── app.py
├── phase3_agent_assist/
│   ├── ingest.py
│   └── rag_chain.py
├── phase4_litemind_chat/
│   └── app.py
├── images/                 # Screenshots or output visuals
├── chroma_store/           # Ignored by Git (vector DB)
├── README.md
├── vision.md
├── requirements.txt
└── .gitignore
```

---

## 🤖 6. Ollama LLM Setup

```bash
# Install Ollama from: https://ollama.com/download

ollama pull tinyllama
ollama run tinyllama

# To switch models:
ollama pull mistral
ollama run mistral
```

---

## 💻 7. Run Apps (Phase-wise)

```bash
# Phase 1: CLI Chat
python phase1_llm_core/chat_cli.py

# Phase 2: Streamlit UI
streamlit run phase2_chat_ui/app.py

# Phase 3: RAG Engine
python phase3_agent_assist/ingest.py
python phase3_agent_assist/rag_chain.py

# Phase 4: LiteMind Chat UI
streamlit run phase4_litemind_chat/app.py
```

---

## 🧰 8. Git Commands

```bash
git init
git remote add origin https://github.com/<username>/<repo>.git

# Setup .gitignore
echo "venv/" >> .gitignore
echo "chroma_store/" >> .gitignore
echo "*.DS_Store" >> .gitignore
echo "*.pyc" >> .gitignore

# Commit and Push
git add .
git commit -m "🚀 Initial Commit"
git push -u origin main
```

---

## 📸 9. Add Screenshot to Git

```bash
mkdir images
mv ~/Downloads/screenshot.png images/phase4_ui.png
git add images/phase4_ui.png

# Reference in README.md
![Phase 4 UI](images/phase4_ui.png)
```

---

## 🧠 10. Recommended Tools for Saving This Cheatsheet

* [GitHub Gist](https://gist.github.com/)
* [Notion](https://notion.so)
* [Obsidian](https://obsidian.md)
* Local markdown file: `project_setup_cheatsheet.md`

---

📅 **Use this for every new Python + GenAI project and adapt as needed.**
