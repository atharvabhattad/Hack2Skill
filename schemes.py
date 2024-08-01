import streamlit as st
from PIL import Image
import io
import base64

def adjust_image_opacity(image, opacity):
    """Adjust the opacity of the image."""
    image = image.convert("RGBA")
    alpha = image.split()[3]
    alpha = alpha.point(lambda p: p * opacity)
    image.putalpha(alpha)
    return image

def display_content_with_links():
    """Display text and link content."""
    contents = [
        ("Paramparagat Krishi Vikas Yojana", "https://dmsouthwest.delhi.gov.in/scheme/paramparagat-krishi-vikas-yojana/"),
        ("Soil health Card scheme", "https://soilhealth.dac.gov.in/home"),
        ("PM Kisan", "https://pmkisan.gov.in/"),
        ("Pradhan Mantri Krishi Sinchai Yojana", "https://pmksy.gov.in/"),
        ("Pradhan Mantri Fasal Bima Yojana", "https://pmfby.gov.in/"),
        ("Kisan Credit Card", "https://www.myscheme.gov.in/schemes/kcc"),
        ("Modified Interest Subvention Scheme (MISS) provides concessional short-term agri-loans", "https://www.nabard.org/content1.aspx?id=602&catid=23&mid=23"),
        (".Jharkhand Krishi Rin Mafi Yojana", "https://jkrmy.jharkhand.gov.in/"),
        ("Rainfed Area Development (RAD)", "https://nmsa.dac.gov.in/frmComponents.aspx"),
        ("PDigital Agriculture", "https://agriwelfare.gov.in/en/DigiAgriDiv"),
    ]
    
    content_html = "<div class='content'>"
    for text, link in contents:
        content_html += f"<p class='example-text'><strong>{text}</strong> -> <a href='{link}' class='example-link'>{link}</a></p>"
    content_html += "</div>"
    return content_html


st.set_page_config(page_title="Webpage with Background Image", layout="wide")

opacity = st.sidebar.slider("Adjust Background Image Opacity", min_value=0.0, max_value=1.0, value=1.0)

background_image = Image.open("Soil Health.png")  
background_image = adjust_image_opacity(background_image, opacity)


buffered = io.BytesIO()
background_image.save(buffered, format="PNG")
img_data = buffered.getvalue()
img_base64 = "data:image/png;base64," + base64.b64encode(img_data).decode()

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{img_base64}");
        background-size: cover;
        background-position: center;
        color: white;
        height: 100vh;
        width: 100vw;
        padding: 20px;
        box-sizing: border-box;
    }}
    .content {{
        text-align: left;
        line-height: 1.6;
        margin: 20px;
    }}
    .example-text {{
        font-size: 40px; /* Font size for example text */
    }}
    .example-link {{
        color: lightblue;
    }}
    h1 {{
        font-size: 100px; /* Font size for heading */
        text-align: left;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("<h1>Links</h1>", unsafe_allow_html=True)
st.markdown(display_content_with_links(), unsafe_allow_html=True)
