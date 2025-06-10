# Intent Score AI Lead Finder (Caprae-style)

This AI-powered tool replicates the workflow of **Caprae Capital’s Pre-Screening Engine** to identify promising companies, score job leads based on intent, and visualize results through a smart and user-friendly Streamlit interface.
This tool is focused to improve the performance of "SCRAPER TOOL" by providing additional features of 
1.Lead of the company
2.LinkedIn profile of the Lead
3.Job title
4.Intent score
5.Rating according to the Intent score
---

## Features

- **Step-by-step UI flow** like Caprae Capital:
  - Select Industry (e.g., Software, Healthcare)
  - Select Location
  - Choose action: "Clear", "Find Companies", or "Cancel"
  - Get matched companies with scored leads and job titles

- **Intent Scoring Engine**:
  - Uses job descriptions + lead metadata to compute a custom score
  - Assigns a rating grade based on score range:

    | Score | Grade |
    |-------|--------|
    | 91–100 | A+     |
    | 81–90  | A−     |
    | 71–80  | B+     |
    | 61–70  | B−     |
    | 51–60  | C+     |
    | 41–50  | C−     |
    | 31–40  | D      |
    | 0–30   | F      |

- **Smart Filters + Autocomplete**:
  - Dynamic dropdowns that filter industries/locations as you type
  - Fully responsive logic using Streamlit widgets

- **CSV Download**: Export final scored leads in one click

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python (with Pandas and JSON)
- **Scoring Engine**: Custom logic (`score.py`)
- **Data**: Manually curated metadata, jobs & leads (in JSON/CSV)

---

## Project Structure

```bash
intent-score-tool/
├── streamlit_app/
│   └── app_flow.py          # Main app UI logic
├── scoring/
│   └── score.py             # Scoring logic (e.g., compute_score)
├── data/
│   ├── companies_metadata.csv       
│   ├── jobs_sample.json
│   ├── jobs_sample_unique.json
│   └── leads_sample.json
|       
├── requirements.txt
└── README.md


---

## Setup

1. Clone the repo:

git clone https://github.com/yourusername/intent-score-tool.git
cd intent-score-tool

2. Install dependencies:

pip install -r requirements.txt

3. Run the Streamlit app:

streamlit run streamlit_app/app_flow.py


