from utils import gemini_client
client=gemini_client.get_client()
from datetime import datetime
# Load environment variables from .env file
# Get the GEMINIAI API key from environment variables



def report_generator(company_data, job_data):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"Generate a report in good looking format about the company {company_data} and the job requirements {job_data}"
    )
    Filename = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    r= response.text
    with open(Filename, 'w',encoding="utf-8") as file:
        file.write(r)
    return r