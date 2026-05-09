import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("\nAvailable Models:\n")

# List all available models
for model in genai.list_models():

    # Show only models that support text generation
    if "generateContent" in model.supported_generation_methods:
        print(f"Model Name : {model.name}")
        print(f"Display Name : {model.display_name}")
        print(f"Description : {model.description}")
        print("-" * 50)