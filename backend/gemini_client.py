import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load variables from the .env file
load_dotenv()

# Read the API key from the environment
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Gemini SDK
genai.configure(api_key=api_key)

# Create the model object
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(context, question):
    """
    Generates an answer using the retrieved document context.
    """

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the context below.

If the answer is not present in the context,
say:
"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text