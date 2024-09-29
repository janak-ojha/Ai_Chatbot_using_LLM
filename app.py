import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def llm_model(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("AI Chatbot")
    user_input = st.text_input("Enter your text input:")
    if st.button("Submit"):
        response = llm_model(user_input)
        st.write("Model Output:", response)

if __name__ == "__main__":
    main()
