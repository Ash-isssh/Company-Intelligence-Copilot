from utils import gemini_client
client=gemini_client.get_client()

def get_job_requirements(*args):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"Give me the Important data in json format at{args[0]} about the job {args[1]}"
    )
    return response.text