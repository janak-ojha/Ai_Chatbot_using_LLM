import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Google Generative AI library with the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def llm_model(prompt):
    # Use the correct class or method to generate content
    model = genai.GenerativeModel('gemini-1.5-flash')  # Change this if necessary
    response = model.generate(prompt)  # Adjust based on actual method
    return response.text

def main():
    user_input = "The opposite of hot is"
    model_output = llm_model(user_input)
    print("Model Output:", model_output)

if __name__ == "__main__":
    main()
