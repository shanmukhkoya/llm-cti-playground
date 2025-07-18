# 🧠 gen-ai.md — Generative AI Concepts & Applications in `llm-cti-playground`

> _This document captures all the **Generative AI** concepts, libraries, models, and techniques applied throughout the phases of our `llm-cti-playground` project. It serves as a consolidated knowledge checkpoint of your learning journey._

---

## ✅ What Is Generative AI?

Generative AI refers to systems that can generate content (text, images, audio, code, etc.) given a prompt or context — using large pretrained models like LLMs. These models are trained on massive datasets and learn to generate human-like output.

---

## 🎯 Why We Used GenAI in This Project

We aimed to:

- Learn how LLMs process natural language.
- Build **modular** GenAI applications across CLI, UI, RAG, and speech interfaces.
- Explore **resource-light** models that can run on CPU and within WSL environments.
- Learn how to **integrate open-source models** like TinyLLaMA with production-ready pipelines.

---

## 🧠 Key Concepts & How We Applied Them

| Concept | Description | Implementation in Our Project |
|--------|-------------|-------------------------------|
| **LLMs (Large Language Models)** | Text generation models trained on massive corpora. | Used `TinyLLaMA` via Ollama as the base model across all phases. |
| **Prompt Engineering** | Designing input prompts to get useful outputs from an LLM. | Prompted TinyLLaMA with structured queries in CLI, UI, and RAG apps. |
| **RAG (Retrieval-Augmented Generation)** | Enhancing LLM output by retrieving relevant knowledge. | Phase 3 & 4: Fetched context from PDF/DOCX/TXT using ChromaDB + Sentence Transformers before LLM prompt. |
| **Embeddings** | Vector representations of documents for semantic search. | Used Sentence Transformers to embed and store document chunks. |
| **ChromaDB** | Lightweight vector database to store and retrieve embeddings. | Used in Phase 3+ to power document search for agent-assist. |
| **Speech-to-Text (STT)** | Converting audio input into text. | Phase 5: Used Whisper (and Faster-Whisper) to transcribe `.mp3/.wav`. |
| **TTS (Text-to-Speech)** | Generating audio from text. | Upcoming Phase (planned): Use TTS to make LLM voice interactive. |
| **Inference API / Local LLMs** | Running LLMs locally (offline) with API endpoints. | Used `Ollama` as a lightweight LLM server to avoid cloud dependence. |
| **Modular AI Pipelines** | Decoupled system that allows plug-and-play of different models. | Structured codebase by phase (CLI, UI, RAG, STT) to keep each concept isolated and extensible. |

---

## 🧰 Libraries & Tools We Used

| Tool/Library | Purpose |
|--------------|---------|
| `Ollama` | Local model runtime for TinyLLaMA, Mistral, Phi3, etc. |
| `sentence-transformers` | For generating embeddings of documents. |
| `ChromaDB` | Vector store to retrieve semantically similar content. |
| `requests` | To send prompts to Ollama server. |
| `streamlit` | To build fast browser-based GenAI UIs. |
| `whisper`, `faster-whisper`, `whisperx` | For offline transcription of audio inputs. |
| `pydub` | For converting `.mp3` to `.wav` audio formats. |

---

## 🧪 Hands-On Learning Outcomes

- 💬 Built **CLI chat** using `requests` + `Ollama`.
- 🌐 Built **Streamlit UI chat** with history and async feedback.
- 🔎 Built **RAG system** using `ChromaDB` + `Sentence Transformers`.
- 🎙️ Built **STT phase** using Whisper-based transcription.
- 🧱 Understood **embedding stores**, vector databases, and how LLMs can be context-aware.
- 🚀 Validated how **lightweight GenAI** can work without GPUs or cloud APIs.

---

## 🌟 Next Planned Concepts

- 🗣️ Full **voice-to-voice AI assistant** using STT → LLM → TTS.
- 🧭 Build **LangChain Agents** to dynamically route user queries.
- 📡 Create **LLM Gateway** with structured API calls and responses.

---

## 📌 Summary

This journey wasn't just about running LLMs. It was about orchestrating GenAI workflows that are:

- 🔋 **Efficient**: Low resource usage, local-first setup
- 🧠 **Educational**: Clear, modular implementation of each GenAI concept
- 🧩 **Composable**: Can scale to multi-modal or production-grade architectures