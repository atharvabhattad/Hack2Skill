import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("please wait...")
    recognizer.adjust_for_ambient_noise(source)
    print("Listening for your speech...")

    audio_data = recognizer.listen(source)
    print("Recognizing speech...")
    try:
        text = recognizer.recognize_google(audio_data)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Errror")