from dotenv import load_dotenv
import os
from google import genai
# Load environment variables from .env file
load_dotenv()
# Get the GEMINIAI API key from environment variables
GEMINIAI_API_KEY = os.getenv("GEMINIAI_API_KEY")
# Initialize the GEMINIAI client
def company_data(company_name):
    # This function would contain the logic to fetch and return company data
    # For demonstration purposes, we will return a mock dictionary
    client = genai.Client(api_key=GEMINIAI_API_KEY)
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"Give me the Important data in the form of json about {company_name}"
    )
    return response.text