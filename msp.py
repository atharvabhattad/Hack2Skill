import streamlit as st
import pandas as pd
from googletrans import Translator

translator = Translator()


def translate_text(text, dest_language):

    if not text or pd.isnull(text):
        return text
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


data = {
    "Sl No.": [1, "", 2, " ", 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, "", 15, 16, 17, 18, 19, 20, 21, "", 22],
    "Commodity": ["PADDY", "PADDY", "JOWAR", "JOWAR", "BAJRA", "RAGI", "MAIZE", "TUR (ARHAR)", "MOONG", "URAD", "GROUNDNUT", "SUNFLOWER SEED", "SOYABEEN", "SESAMUM", "NIGERSEED", "COTTON", "COTTON", "WHEAT", "BARLEY", "GRAM", "mASUR(LENTIL)", "RAPESEED & MUSTARD", "SAFFLOWER", "COPRA", "COPRA", "JUTE"],
    "Variety": ["Common", "Grade 'A'", "Hybrid", "Maldandi", "", "", "", "", "", "", "", "", "(yellow)", "", "", "Medium staple", "Long Staple", "", "", "", "", "", "", "MILLING", "BALL", ""],
    "2023-24": [2183, 2203, 3180, 3225, 2500, 3846, 2090, 7000, 8558, 6950, 6377, 6760, 4600, 8635, 7734, 6620, 7020, 2275, 1850, 5440, 6425, 5650, 5800, 10860, 11750, 5050]
}


df = pd.DataFrame(data)


translated_columns = {
    col: translate_text(col, languages[selected_language]) if col != "Sl No." and col != "2023-24" else col
    for col in df.columns
}


translated_data = df.copy()
for column in df.columns:
    if column != "Sl No." and column != "2023-24":
        translated_data[column] = df[column].apply(lambda x: translate_text(x, languages[selected_language]) if isinstance(x, str) else x)

st.title(translate_text("Crops MSP Table for 2023-24", languages[selected_language]))


st.dataframe(translated_data.rename(columns=translated_columns).set_index("Sl No."), width=1200, height=600)
