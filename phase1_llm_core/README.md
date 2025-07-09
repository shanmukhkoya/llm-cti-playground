# Phase 1: TinyLLaMA CLI Chat

## Goal
Understand how to run a local LLM (tinyllama) using Ollama and create a simple CLI interface for chat.

## Steps
1. Run Ollama: `ollama run tinyllama`
2. In another terminal: `python chat_cli.py`
3. Interact with your local model!

## Learnings
- Ollama runs LLMs as REST API server
- POST to `/api/generate` gives model output
- Simple loop builds chat logic
