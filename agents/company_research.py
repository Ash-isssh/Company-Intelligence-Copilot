from utils import gemini_client
client=gemini_client.get_client()
# Initialize the GEMINIAI client
def research_company(company_name):
    # This function would contain the logic to fetch and return company data
    # For demonstration purposes, we will return a mock dictionary
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"Give me the Important data in the form of json about {company_name}"
    )
    return response.text
