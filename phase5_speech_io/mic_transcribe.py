import speech_recognition as sr

recognizer = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source:
    print("🎤 Say something...")
    audio = recognizer.listen(source)

    try:
        print("🧠 Transcribing...")
        text = recognizer.recognize_whisper(audio)  # Use Whisper backend
        print(f"📝 You said: {text}")
    except sr.UnknownValueError:
        print("❗Could not understand audio")
    except sr.RequestError as e:
        print(f"❗Whisper error: {e}")
