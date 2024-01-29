from dotenv import load_dotenv
load_dotenv()
from PIL import Image


import streamlit as st 
import os 
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro and get responses.
model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input!="":
        
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini LLM Application")
input=st.text_input("Input Prompt : ",key="input")
# File uploader to get user input
uploaded_file = st.file_uploader("Choose an image...", type=['jpeg', 'jpg', 'png'])

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")



submit=st.button("Tell me about the image")

# When Submit is clicked.
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is...")
    st.write(response)
