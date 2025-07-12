# phase5_speech_io/speech_chat.py

import os
import requests
from faster_whisper import WhisperModel

# --- Settings ---
OLLAMA_URL = "http://localhost:11434"
MODEL_NAME = "tinyllama"
AUDIO_DIR = "phase5_speech_io/audio_inputs"

def list_audio_files():
    return [f for f in os.listdir(AUDIO_DIR) if f.endswith(('.mp3', '.wav'))]

def transcribe_audio(audio_path):
    print("🔎 Transcribing with Faster Whisper...")
    model = WhisperModel("tiny", device="cpu", compute_type="int8")  # lightweight on CPU

    segments, _ = model.transcribe(audio_path)
    transcript = ""
    for segment in segments:
        transcript += segment.text.strip() + " "

    return transcript.strip()

def ask_llm(prompt):
    print("🤖 Asking LLM...")
    try:
        res = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False}
        )
        res.raise_for_status()
        return res.json().get("response", "[No response]")
    except Exception as e:
        return f"[LLM Error] {e}"

def main():
    print("🎙️  Speech-to-LLM Chat")
    print("------------------------")
    audio_files = list_audio_files()

    if not audio_files:
        print(f"No audio files found in {AUDIO_DIR}/")
        return

    for idx, file in enumerate(audio_files):
        print(f"{idx + 1}. {file}")

    choice = input("Select a file to transcribe (1-N): ")
    try:
        choice_idx = int(choice) - 1
        input_file = audio_files[choice_idx]
    except:
        print("❌ Invalid selection.")
        return

    print(f"🎧 Using: {input_file}")
    audio_path = os.path.join(AUDIO_DIR, input_file)

    transcript = transcribe_audio(audio_path)
    print("\n📝 Transcription:")
    print("----------------")
    print(transcript)

    response = ask_llm(transcript)
    print("\n🤖 LLM Response:")
    print("----------------")
    print(response)

if __name__ == "__main__":
    main()
