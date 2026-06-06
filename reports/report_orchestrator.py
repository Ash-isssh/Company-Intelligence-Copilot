from dotenv import load_dotenv
import os
from google import genai
from agents import company_research,job_data
# Load environment variables from .env file
load_dotenv()
# Get the GEMINIAI API key from environment variables
GEMINIAI_API_KEY = os.getenv("GEMINIAI_API_KEY")
def report_generator(company_data, job_data):
    client = genai.Client(api_key=GEMINIAI_API_KEY)
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"Generate a report in good looking format about the company {company_data} and the job requirements {job_data}"
    )
    return response.text