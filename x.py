import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
from googletrans import Translator

cred = credentials.Certificate('signup-7d43c-5f48cbb1b6c8.json')
#firebase_admin.initialize_app(cred)


translator = Translator()

def translate_text(text, dest_language):
    translated = translator.translate(text, dest=dest_language)
    return translated.text

languages = {
    'English': 'en',
    'Hindi': 'hi',
    'Tamil': 'ta',
    'Bengali': 'bn',
    'Gujarati': 'gu'
}
selected_language = st.sidebar.selectbox("Select Language", list(languages.keys()))


def app():
    st.title(translate_text("Welcome", languages[selected_language]))
    choice = st.radio(translate_text('Login/SignUp', languages[selected_language]), 
                      [translate_text('Login', languages[selected_language]), 
                       translate_text('SignUp', languages[selected_language])])

    if choice == translate_text('Login', languages[selected_language]):
        email = st.text_input(translate_text('Email Address', languages[selected_language]))
        password = st.text_input(translate_text('Password', languages[selected_language]), type='password')
        
        def login():
            try:
                user = auth.get_user_by_email(email)
                st.success(translate_text('Login Successful', languages[selected_language]))
            except firebase_admin.auth.UserNotFoundError:
                st.warning(translate_text('User not found. Please check your email or sign up.', languages[selected_language]))
            except Exception as e:
                st.error(translate_text(f'An error occurred: {str(e)}', languages[selected_language]))
        
        st.button(translate_text('Login', languages[selected_language]), on_click=login)
    
    elif choice == translate_text('SignUp', languages[selected_language]):
        email = st.text_input(translate_text('Email Address', languages[selected_language]))
        password = st.text_input(translate_text('Password', languages[selected_language]), type='password')
        username = st.text_input(translate_text('Enter your unique username', languages[selected_language]))

        if st.button(translate_text('Create my account', languages[selected_language])):
            try:
                user = auth.create_user(email=email, password=password, uid=username)
                st.success(translate_text('Account created successfully', languages[selected_language]))
                st.markdown(translate_text('Please login using your email and password', languages[selected_language]))
                st.snow()
            except Exception as e:
                st.error(translate_text(f'Error creating user: {str(e)}', languages[selected_language]))

if __name__ == "__main__":
    app()
