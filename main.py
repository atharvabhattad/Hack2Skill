import streamlit as st

# Dictionary to map page names to their respective Python files
PAGES = {
    "Home": "home_page.py",
    "Reading": "sensor.py",
    "Rates": "msp.py",
    "Disease": "crop_predict.py",
    "Crop": "cropdescription.py",
    "Erosion": "erosion.py",
    "Weather": "weather.py",
    "Chatbot": "chatbot.py",
    "Login/Signup": "x.py",
    "Schemes": "schemes.py",
    "soil": "soil.py",
}

# Initialize session state variables if they do not exist
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Sidebar for page selection
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()), index=list(PAGES.keys()).index(st.session_state.page))

# Update the session state to reflect the selected page
st.session_state.page = selection

# Load the selected page
page_file = PAGES[st.session_state.page]

# Execute the selected page file
with open(page_file) as f:
    exec(f.read())
