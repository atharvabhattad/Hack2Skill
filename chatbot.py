
import streamlit as st
import requests
import speech_recognition as sr


API_KEY = 'sk-proj-V3gbpuYrEmPQlMX78OtJT3BlbkFJvUvrnGtUmqiUi1MKIcdo' 
API_URL = 'https://api.openai.com/v1/chat/completions'

def get_chatgpt_response(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'model': 'gpt-3.5-turbo',  
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 150
    }
    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Please wait...")
        recognizer.adjust_for_ambient_noise(source)
        st.write("Listening for your speech...")

        audio_data = recognizer.listen(source)
        st.write("Recognizing speech...")
        try:
            text = recognizer.recognize_google(audio_data)
            st.write("You said: " + text)
            return text
        except sr.UnknownValueError:
            st.write("Error: Could not understand the audio.")
            return None

st.title("Voice Activated Chatbot")

if st.button("Voice"):
    user_input = recognize_speech()
    if user_input:
        response = get_chatgpt_response(user_input)
        if 'choices' in response:
            chatgpt_reply = response['choices'][0]['message']['content'].strip()
            st.write("Chatbot response: " + chatgpt_reply)
        else:
            st.write("Error: Could not get a response from the chatbot.")
            st.write("Response from API: " + str(response))
