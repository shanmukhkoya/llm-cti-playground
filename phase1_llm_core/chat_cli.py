from ollama_client import query_ollama

def chat():
    print("🤖 TinyLLaMA CLI Chat - Type 'exit' to quit\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        try:
            response = query_ollama(user_input)
            print(f"LLM: {response}\n")
        except Exception as e:
            print(f"⚠️ Error: {e}\n")

if __name__ == "__main__":
    chat()
