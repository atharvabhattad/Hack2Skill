import streamlit as st
from googletrans import Translator

translator = Translator()

def translate_text(text, target_language='hi'):
    result = translator.translate(text, dest=target_language)
    return result.text

def translate_page(elements, target_language='hi'):
    translated_elements = [translate_text(element, target_language) for element in elements]
    return translated_elements

def display_images(target_language='hi'):
    st.write("### Important Links")
    image_info = [
        ("Crop Production Method", "Crop Production.png", ""),
        ("Disease", "Plant Infection.png", "Disease"),
        ("Government Schemes", "Government Schemes.png", "Schemes"),
        ("Soil Health", "Soil Health.png", "soil"),
        ("Horticulture Methods", "Horticulture.png", ""),
        ("Crop Treatment", "Crop Treatment (1).png", ""),
        ("MSP Rates", "MSP Rates.png", "Rates"),
        ("Weather News", "Weather News.png", "Weather"),
    ]

    # Translate image titles
    image_titles = [item[0] for item in image_info]
    translated_titles = translate_page(image_titles, target_language)

    # Create columns for images
    num_cols = 4
    cols = st.columns(num_cols)

    for i, (original_title, img, page) in enumerate(image_info):
        with cols[i % num_cols]:
            st.image(img, caption=translated_titles[i], use_column_width=True)
            if page:
                if st.button(translated_titles[i]):
                    st.session_state.page = page

def home_page(target_language='hi'):
    st.title(translate_text("Home Page", target_language))
    st.write(translate_text("Welcome to the Home page!", target_language))
    display_images(target_language)

# Initialize session state variables if they do not exist
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'language_code' not in st.session_state:
    st.session_state.language_code = 'hi'

home_page(st.session_state.language_code)
