from dotenv import load_dotenv
import os
from google import genai
# Load environment variables from .env file
load_dotenv()
# Get the GEMINIAI API key from environment variables
GEMINIAI_API_KEY = os.getenv("GEMINIAI_API_KEY")
# Initialize the GEMINIAI client

client = genai.Client(api_key=GEMINIAI_API_KEY)
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)