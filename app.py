from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os 
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro and get responses.
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

# Initializing our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask The Question")

# When Submit is clicked.
if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is...")
    st.write(response)
