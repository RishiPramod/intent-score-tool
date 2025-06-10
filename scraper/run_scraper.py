import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scraper.jobs_scraper import scrape_jobs_from_wellfound

companies = ["notion", "airtable", "zapier", "asana", "clickup"]
all_jobs = []

for company in companies:
    jobs = scrape_jobs_from_wellfound(company)
    print(f"Scraped {len(jobs)} jobs for {company}")
    all_jobs.extend(jobs)

with open("/home/rishi/intent_score_project/data/jobs_sample.json", "w") as job_file:
    json.dump(all_jobs, job_file, indent=2)

print("All jobs scraped and saved to jobs_sample.json")