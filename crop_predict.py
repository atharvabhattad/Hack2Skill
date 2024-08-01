import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import BatchNormalization, Flatten, Dense, Dropout
from PIL import Image
from googletrans import Translator


translator = Translator()


def translate_text(text, dest_language):
 
    if text is None or text.strip() == "":
        return text
    translated = translator.translate(text, dest=dest_language)
    return translated.text


def create_model():
    conv = DenseNet121(weights='imagenet', include_top=False, input_shape=(256, 256, 3), pooling='avg')
    
    model = Sequential()
    model.add(conv)
    model.add(BatchNormalization())
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.3))
    model.add(BatchNormalization())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(38, activation='softmax')) 
    
    return model


model = create_model()


model.build(input_shape=(None, 256, 256, 3))


model.load_weights('my_plant_model1.weights.h5')


class_names = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)_Powdery_mildew', 'Cherry_(including_sour)_healthy',
    'Corn_(maize)_Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)_Common_rust', 
    'Corn_(maize)_Northern_Leaf_Blight', 'Corn_(maize)_healthy', 'Grape___Black_rot',
    'Grape___Esca(Black_Measles)', 'Grape___Leaf_blight(Isariopsis_Leaf_Spot)', 'Grape___healthy',
    'Orange___Haunglongbing(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
    'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
    'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
]


disease_treatments = {
    'Apple___Apple_scab': 'Remove and destroy fallen leaves in autumn to reduce overwintering spores. Apply fungicides like captan or myclobutanil starting at green tip and repeating every 7-10 days as necessary.',
    'Apple___Black_rot': 'Prune out infected branches and mummified fruits. Apply fungicides such as thiophanate-methyl or captan starting at petal fall and continuing every 10-14 days as needed.',
    'Apple___Cedar_apple_rust': 'Remove galls from cedar trees in winter. Apply fungicides such as myclobutanil or mancozeb to apple trees starting at pink bud stage and continuing every 7-10 days until 1-2 weeks after petal fall.',
    'Cherry_(including_sour)_Powdery_mildew': 'Apply fungicides such as sulfur or myclobutanil when disease is first detected and repeat every 10-14 days. Ensure good air circulation and avoid overhead watering.',
    'Corn_(maize)_Cercospora_leaf_spot Gray_leaf_spot': 'Rotate crops with non-host species. Apply fungicides like azoxystrobin or pyraclostrobin at first sign of disease and repeat every 14 days as needed.',
    'Corn_(maize)_Common_rust': 'Plant resistant hybrids. Apply fungicides such as propiconazole or azoxystrobin at the onset of symptoms and repeat every 7-10 days as necessary.',
    'Corn_(maize)_Northern_Leaf_Blight': 'Use resistant varieties. Apply fungicides like mancozeb or azoxystrobin at the first sign of disease and repeat every 7-14 days as needed.',
    'Grape___Black_rot': 'Remove mummified berries and prune out infected shoots. Apply fungicides such as myclobutanil or mancozeb beginning at bud break and continuing every 10-14 days as necessary.',
    'Grape___Esca(Black_Measles)': 'Prune affected vines and remove dead wood. Apply fungicides like tebuconazole or thiophanate-methyl, but effectiveness is limited.',
    'Grape___Leaf_blight(Isariopsis_Leaf_Spot)': 'Improve air circulation through proper pruning. Apply fungicides such as mancozeb or copper-based products at the first sign of disease and repeat as necessary.',
    'Orange___Haunglongbing(Citrus_greening)': 'Remove and destroy infected trees. Control Asian citrus psyllid vector with insecticides like imidacloprid or thiamethoxam. Use certified disease-free nursery stock.',
    'Peach___Bacterial_spot': 'Plant resistant varieties. Apply copper-based bactericides starting at petal fall and continuing every 7-10 days during wet weather.',
    'Pepper,_bell___Bacterial_spot': 'Use certified disease-free seeds and transplants. Apply copper-based bactericides at the first sign of disease and repeat every 7-10 days during wet weather.',
    'Potato___Early_blight': 'Rotate crops and use certified disease-free seed potatoes. Apply fungicides such as chlorothalonil or mancozeb starting at first sign of disease and repeat every 7-10 days.',
    'Potato___Late_blight': 'Use resistant varieties and certified disease-free seed potatoes. Apply fungicides like chlorothalonil or mancozeb at first sign of disease and repeat every 5-7 days during wet weather.',
    'Squash___Powdery_mildew': 'Apply fungicides such as sulfur or potassium bicarbonate when disease is first detected and repeat every 7-10 days. Ensure proper spacing and good air circulation.',
    'Strawberry___Leaf_scorch': 'Remove infected leaves and debris. Apply fungicides such as myclobutanil or captan starting at first sign of disease and repeat every 10-14 days as needed.',
    'Tomato___Bacterial_spot': 'Use certified disease-free seeds and transplants. Apply copper-based bactericides at the first sign of disease and repeat every 7-10 days during wet weather.',
    'Tomato___Early_blight': 'Use resistant varieties and rotate crops. Apply fungicides such as chlorothalonil or mancozeb starting at first sign of disease and repeat every 7-10 days.',
    'Tomato___Late_blight': 'Remove and destroy infected plants. Apply fungicides such as chlorothalonil or mancozeb at first sign of disease and repeat every 5-7 days during wet weather.',
    'Tomato___Leaf_Mold': 'Improve air circulation through proper pruning and avoid overhead watering. Apply fungicides such as chlorothalonil or copper-based products at first sign of disease and repeat as necessary.',
    'Tomato___Septoria_leaf_spot': 'Remove infected leaves and improve air circulation. Apply fungicides such as chlorothalonil or mancozeb starting at first sign of disease and repeat every 7-10 days.',
    'Tomato___Spider_mites Two-spotted_spider_mite': 'Use miticides such as abamectin or bifenthrin. Encourage natural predators like ladybugs and predatory mites.',
    'Tomato___Target_Spot': 'Use resistant varieties and rotate crops. Apply fungicides such as chlorothalonil or mancozeb at first sign of disease and repeat every 7-10 days.',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 'Control whitefly populations with insecticides like imidacloprid or insecticidal soaps. Use resistant varieties and reflective mulches to reduce whitefly infestation.',
    'Tomato___Tomato_mosaic_virus': 'Remove and destroy infected plants. Disinfect tools and hands with a bleach solution. Use resistant varieties and avoid handling plants when they are wet.',
}





languages = {
    'en': 'English',
    'hi': 'Hindi',
    'mr': 'Marathi',
    'gu': 'Gujarati',
    'ta': 'Tamil'
}


selected_language = st.sidebar.selectbox("Select Language", list(languages.keys()), format_func=lambda lang: languages[lang])


st.title(translate_text("Plant Disease Prediction", selected_language))
st.sidebar.header(translate_text("Language Selection", selected_language))
upload_prompt = translate_text("Choose an image...", selected_language)
predicted_class_label = translate_text("Predicted class:", selected_language)
treatment_label = translate_text("Recommended treatment:", selected_language)


uploaded_file = st.file_uploader(upload_prompt, type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    
   
    img_array = np.array(image.resize((256, 256))) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
   
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)
    predicted_class_name = class_names[predicted_class[0]]
    

    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write(f"{predicted_class_label} {translate_text(predicted_class_name, selected_language)}")
    
 
    treatment = disease_treatments.get(predicted_class_name, "No treatment information available.")
    st.write(f"{treatment_label} {translate_text(treatment, selected_language)}")
