import streamlit as st
import json
import pandas as pd
import os
import sys
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scoring.score import compute_score
from scoring.rating import get_rating

st.set_page_config(page_title="Caprae Lead Scorer", layout="centered")
metadata_df = pd.read_csv("data/companies_metadata.csv")

st.markdown("Choose an Industry")
selected_industry = st.text_input("Industry", placeholder="Enter industry (e.g. Software, Healthcare)")

st.markdown("Choose a Location")
selected_location = st.text_input("Location", placeholder="Enter location (e.g. San Francisco, CA)")

col1, col2, col3 = st.columns(3)
with col1:
    clear_clicked = st.button("Clear")
with col2:
    find_clicked = st.button("Find Companies")
with col3:
    cancel_clicked = st.button("Cancel")

if clear_clicked:
    st.experimental_rerun()  

elif cancel_clicked:
    st.info("Search cancelled. You may modify filters above.")

elif find_clicked:
    st.markdown("Matching Companies")
    matched_df = metadata_df[
        (metadata_df["Industry"] == selected_industry) &
        (metadata_df["Location"] == selected_location)
    ]
    if not matched_df.empty:
        st.success(f"Found {len(matched_df)} matching companies.")
        st.dataframe(matched_df.reset_index(drop=True), use_container_width=True)
    else:
        st.warning("No companies match that industry + location.")

if find_clicked and not matched_df.empty:
    st.markdown("Lead-to-Job Matching and Scoring")

    with open("data/jobs_sample.json") as f:
        all_jobs = json.load(f)
    with open("data/leads_sample.json") as f:
        all_leads = json.load(f)
    results = []

    for _, row in matched_df.iterrows():
        company = row["Company"]
        industry = row["Industry"]
        location = row["Location"]
        jobs = [j for j in all_jobs if j["company"] == company]
        leads = [l for l in all_leads if l["company"] == company]
        phone = f"+1-{random.randint(100,999)}-{random.randint(1000,9999)}"

        for lead in leads:
            for job in jobs:
                score = compute_score(job, lead)
                rating = get_rating(score)
                results.append({
                    "Company": company,
                    "Industry": industry,
                    "Location": location,
                    "Lead": lead["name"],
                    "LinkedIn": lead["linkedin"],
                    "Phone": phone,
                    "Job Title": job["title"],
                    "Score": score,
                    "Rating": rating,
                    "Job URL": job["url"],
                    "Intent Score": f"{score}/100"
                })

    if results:
        df_results = pd.DataFrame(results)
        st.dataframe(df_results, use_container_width=True)
        st.download_button(
            "Download Scored Leads CSV",
            df_results.to_csv(index=False),
            file_name="scored_leads.csv",
            mime="text/csv"
        )
    else:
        st.warning("No matching leads or jobs found.")
