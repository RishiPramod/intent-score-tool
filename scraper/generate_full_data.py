import pandas as pd
import json
import random

df = pd.read_csv("/home/rishi/intent_score_project/data/companies_metadata.csv")
job_templates = {
    "Software": [
        ("AI Research Engineer", "Work on advanced machine learning models for software tools."),
        ("ML Backend Developer", "Design ML inference systems and deployment pipelines."),
        ("Data Scientist - SaaS", "Analyze product data and build prediction models.")
    ],
    "Healthcare": [
        ("AI Bioinformatics Analyst", "Use AI to interpret healthcare datasets."),
        ("Medical Data Scientist", "Model clinical outcomes from patient records."),
        ("Healthcare AI Engineer", "Build AI-driven diagnostic and health tools.")
    ]
}

job_data = []
for _, row in df.iterrows():
    for _ in range(2):
        title, desc = random.choice(job_templates[row['Industry']])
        job_data.append({
            "company": row["Company"],
            "title": title,
            "description": desc,
            "location": row["Location"],
            "url": f"{row['Website']}/careers/{title.lower().replace(' ', '-')}"
        })
names = ["Alex", "Taylor", "Morgan", "Jordan", "Casey"]
surnames = ["Smith", "Lee", "Garcia", "Patel", "Chen"]
titles = ["CTO", "Head of AI", "Director of Engineering", "VP of Product", "AI Researcher"]

lead_data = []
for _, row in df.iterrows():
    for _ in range(2):
        fname = random.choice(names)
        lname = random.choice(surnames)
        title = random.choice(titles)
        lead_data.append({
            "name": f"{fname} {lname}",
            "title": title,
            "company": row["Company"],
            "linkedin": f"https://linkedin.com/in/{fname.lower()}{lname.lower()}"
        })

with open("/home/rishi/intent_score_project/data/jobs_sample.json", "w") as jf:
    json.dump(job_data, jf, indent=2)
with open("/home/rishi/intent_score_project/data/leads_sample.json", "w") as lf:
    json.dump(lead_data, lf, indent=2)
print("jobs_sample.json and leads_sample.json updated.")
