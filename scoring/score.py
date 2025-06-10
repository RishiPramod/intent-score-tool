def compute_score(job, lead):
    score = 20

    if "AI" in job["title"] or "ML" in job["description"]:
        score += 30
    if lead["title"] in ["CTO", "Director", "VP", "Head"]:
        score += 20
    elif "Engineer" in lead["title"]:
        score += 15
    if "Remote" in job["location"]:
        score += 5
    return min(score, 100)
