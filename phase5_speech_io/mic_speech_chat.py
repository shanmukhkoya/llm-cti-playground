# phase5_speech_io/mic_speech_chat.py

import os
import tempfile
import time
import requests
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile
from faster_whisper import WhisperModel

# --- Settings ---
OLLAMA_URL = "http://localhost:11434"
MODEL_NAME = "tinyllama"
RECORD_SECONDS = 5  # Duration to record from mic
SAMPLE_RATE = 16000  # Whisper recommended sample rate

def record_audio(duration=RECORD_SECONDS, fs=SAMPLE_RATE):
    print(f"🎙️ Recording for {duration} seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("🛑 Recording complete.")
    return recording.flatten()

def save_wav(audio_data, fs=SAMPLE_RATE):
    tmp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    wavfile.write(tmp_file.name, fs, audio_data)
    return tmp_file.name

def transcribe_audio(audio_path):
    print("🔎 Transcribing...")
    model = WhisperModel("small", device="cpu", compute_type="int8")  # Adjust model size if needed
    segments, info = model.transcribe(audio_path)
    transcript = ""
    for segment in segments:
        transcript += segment.text + " "
    return transcript.strip()

def ask_llm(prompt):
    print("🤖 Asking LLM...")
    try:
        res = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False},
            timeout=60,
        )
        res.raise_for_status()
        return res.json().get("response", "[No response]")
    except Exception as e:
        return f"[LLM Error] {e}"

def main():
    audio_data = record_audio()
    wav_path = save_wav(audio_data)
    try:
        transcript = transcribe_audio(wav_path)
        print("\n📝 Transcription:")
        print("----------------")
        print(transcript)

        response = ask_llm(transcript)
        print("\n🤖 LLM Response:")
        print("----------------")
        print(response)
    finally:
        os.remove(wav_path)  # Cleanup temp file

if __name__ == "__main__":
    main()
