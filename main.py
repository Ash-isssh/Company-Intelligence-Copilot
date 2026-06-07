from agents import company_research,job_data
from reports import report_orchestrator
company_data=company_research.research_company("Google")
job_requirements=job_data.get_job_requirements("Data Scientist", "Google")
report = report_orchestrator.report_generator(company_data, job_requirements)