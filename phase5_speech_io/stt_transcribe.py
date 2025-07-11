import os
from pydub import AudioSegment
import speech_recognition as sr

# Set your input directory
AUDIO_DIR = os.path.join(os.path.dirname(__file__), "audio_inputs")

def find_audio_file(extension=".mp3"):
    for fname in os.listdir(AUDIO_DIR):
        if fname.lower().endswith(extension) and not fname.endswith(":Zone.Identifier"):
            return os.path.join(AUDIO_DIR, fname)
    raise FileNotFoundError(f"No {extension} file found in {AUDIO_DIR}")

def convert_to_wav(file_path):
    audio = AudioSegment.from_file(file_path)
    wav_path = file_path.replace(".mp3", ".wav")
    audio.export(wav_path, format="wav")
    return wav_path

def transcribe_audio(wav_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)
    return recognizer.recognize_google(audio_data)

if __name__ == "__main__":
    try:
        mp3_file = find_audio_file(".mp3")
        print(f"[+] Found file: {mp3_file}")

        wav_file = convert_to_wav(mp3_file)
        print(f"[+] Converted to WAV: {wav_file}")

        transcript = transcribe_audio(wav_file)
        print("\n[🗣️  Transcription]")
        print(transcript)
    except Exception as e:
        print(f"[Error] {e}")
