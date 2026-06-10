#This will search fo the related jobs over the internet and return the data in json format
from bs4 import BeautifulSoup
#can use this also to extract data from the html page if needed
#but serapi works as well here
import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()
def search_jobs(job_title,company):
    parameters = {
    "engine": "google_jobs",
    "q": f"{job_title}jobs only at {company}",
    "google_domain": "google.com",
    "hl": "en",
    "api_key": os.getenv("SERP_API_KEY"),
    }
    all_jobs=[]
    while True:
        response = requests.get(f"https://serpapi.com/search",params=parameters)
        results=response.json()
        for job in results.get("jobs_results", []):
            #All these titles are found currently in the json response from the serp api, if there is any change in the response structure then we can change it here accordingly
            all_jobs.append({
                "title": job["title"],
                "company": job["company_name"],
                "location": job["location"],
                "description": job["description"]
            })
        if "next_page_token" not in results.get("serpapi_pagination", {}):
            break
        #doing this for getting more results if there are more than 10 results for the given query, as serp api returns only 10 results per page
        parameters["next_page_token"] = results["serpapi_pagination"]["next_page_token"]
        #saving the data in json format for future use
    with open("job_results.json", "w") as f:
        json.dump(all_jobs, f, indent=2)