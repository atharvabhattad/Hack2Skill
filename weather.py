import streamlit as st
import requests
from googletrans import Translator

translator = Translator()

languages = {
    'English': 'en',
    'Hindi': 'hi',
    'Tamil': 'ta',
    'Gujarati': 'gu',
}

def translate_text(text, dest_language):
    translated = translator.translate(text, dest=dest_language)
    return translated.text


selected_language = st.sidebar.selectbox("Select Language", list(languages.keys()))
dest_language = languages[selected_language]

st.title(translate_text('Weather Information', dest_language))

user_input = st.text_input(translate_text("Enter city:", dest_language), "")

if user_input:

    api_key = '30d4741c779ba94c470ca1f63045390a'

  
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}")

   
    data = weather_data.json()

   
    if data.get('cod') == 200:  
        try:
            weather = data['weather'][0]['main']
            temp = round(data['main']['temp'])
            humidity = data['main']['humidity']
            st.write(translate_text(f"The weather in {user_input} is: {weather}", dest_language))
            st.write(translate_text(f"The temperature in {user_input} is: {temp}ºC", dest_language))
            st.write(translate_text(f"The humidity in {user_input} is: {humidity}%", dest_language))
        except KeyError as e:
            st.write(translate_text(f"Error: Missing key in API response - {e}", dest_language))
    elif data.get('cod') == '404':
        st.write(translate_text("No City Found", dest_language))
    else:
        st.write(translate_text(f"Error: {data.get('message', 'Unknown error occurred')}", dest_language))
