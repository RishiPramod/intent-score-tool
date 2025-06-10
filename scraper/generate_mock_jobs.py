import os
import json

mock_jobs = [
    {
        "company": "Notion",
        "title": "AI Research Engineer",
        "description": "Work on LLMs and integrate them into Notion workspace...",
        "location": "San Francisco",
        "url": "https://notion.so/careers/ai-research-engineer"
    },
    {
        "company": "Airtable",
        "title": "AI Product Manager",
        "description": "Lead strategy and roadmap for AI features in Airtable's core product.",
        "location": "Remote",
        "url": "https://airtable.com/jobs/ai-product-manager"
    },
    {
        "company": "Zapier",
        "title": "Data Scientist - AI Automation",
        "description": "Build predictive models for automation triggers using NLP.",
        "location": "Remote",
        "url": "https://zapier.com/jobs/data-scientist-ai"
    },
    {
        "company": "Asana",
        "title": "Research Scientist - LLMs",
        "description": "Explore next-gen AI for productivity and project prediction.",
        "location": "San Francisco",
        "url": "https://asana.com/jobs/research-scientist-llm"
    },
    {
        "company": "ClickUp",
        "title": "Senior Software Engineer - AI",
        "description": "Develop AI-driven productivity recommendations for teams.",
        "location": "California",
        "url": "https://clickup.com/careers/senior-ai-engineer"
    }
]

with open("/home/rishi/intent_score_project/data/jobs_sample.json", "w") as f:
    json.dump(mock_jobs, f, indent=2)

print(f"✅ Mock jobs saved to {f}")