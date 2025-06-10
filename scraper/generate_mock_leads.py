import json
import os

mock_leads = [
    {
        "name": "Emily Zhang",
        "title": "CTO",
        "company": "Notion",
        "linkedin": "https://linkedin.com/in/emilyzhang"
    },
    {
        "name": "Rahul Mehta",
        "title": "Head of AI",
        "company": "Airtable",
        "linkedin": "https://linkedin.com/in/rahulmehta"
    },
    {
        "name": "Sarah Lopez",
        "title": "Director of Engineering",
        "company": "Zapier",
        "linkedin": "https://linkedin.com/in/sarahlopez"
    },
    {
        "name": "James Kim",
        "title": "Lead Research Scientist",
        "company": "Asana",
        "linkedin": "https://linkedin.com/in/jameskim"
    },
    {
        "name": "Anna Rivera",
        "title": "VP of Product",
        "company": "ClickUp",
        "linkedin": "https://linkedin.com/in/annarivera"
    }
]

with open("/home/rishi/intent_score_project/data/leads_sample.json", "w") as f:
    json.dump(mock_leads, f, indent=2)

print(f"✅ Mock leads saved to {f}")
