
````md
## Model Choice and Setup Instructions

### Why TinyLLaMA is Our Priority Model

- **Lightweight and Fast:** At ~637 MB, TinyLLaMA runs smoothly on limited resource environments like WSL and cloud PCs without GPU.
- **Low Friction:** Requires minimal setup and no special hardware or cloud access.
- **Ideal for Learning:** Enables quick iterations and hands-on exploration of LLM concepts without waiting for large models to load.
- **Future-Proof:** Uses the same Ollama CLI and API interface as larger models, making it easy to switch models without changing code.
- **Expandable:** Once ready, you can upgrade seamlessly to stronger models like Mistral, Llama 3, or Phi.

---

### How to Setup Ollama and Models

1. **Install Ollama**

Follow the official instructions:  
[https://ollama.com/download](https://ollama.com/download)

2. **Pull TinyLLaMA**

```bash
ollama pull tinyllama
````

3. **Run TinyLLaMA**

```bash
ollama run tinyllama
```

4. **Switch to Another Model**

To try other models, simply pull and run them:

```bash
ollama pull mistral
ollama run mistral
```

Or:

```bash
ollama pull llama3.3
ollama run llama3.3
```

## Project Phases & Usage

### Phase 1: CLI LLM Interaction

* Navigate to `phase1_llm_core`
* Run the CLI chat:

```bash
python chat_cli.py
```

---

### Phase 2: Streamlit Chat UI

* Navigate to `phase2_chat_ui`
* Start the UI:

```bash
streamlit run app.py
```

> 💡 Make sure Ollama is running the model in parallel.
