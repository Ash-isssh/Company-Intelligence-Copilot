from attr import define
from dotenv import load_dotenv
import os
from google import genai
# Load environment variables from .env file
load_dotenv()
# Get the GEMINIAI API key from environment variables
GEMINIAI_API_KEY = os.getenv("GEMINIAI_API_KEY")
def get_client():
    return genai.Client(api_key=GEMINIAI_API_KEY)