from dotenv import load_dotenv
import os
from google import genai
# Load environment variables from .env file
load_dotenv()
# Get the GEMINIAI API key from environment variables
GEMINIAI_API_KEY = os.getenv("GEMINIAI_API_KEY")

def get_job_requirements(*args):
    client = genai.Client(api_key=GEMINIAI_API_KEY)
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"Give me the Important data in json format at{args[0]} about the job {args[1]}"
    )
    return response.text