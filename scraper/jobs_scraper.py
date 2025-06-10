import requests
from bs4 import BeautifulSoup

def scrape_jobs_from_wellfound(company_name):
    jobs = []
    base_url = "https://wellfound.com/company/{companies}/jobs"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(base_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        job_cards = soup.find_all('div', class_='job-card')
        for card in job_cards:
            title = card.find('h2').get_text(strip=True)
            desc = card.find('p').get_text(strip=True)
            link = "https://wellfound.com" + card.find('a')['href']
            jobs.append({
                "company": company_name,
                "title": title,
                "description": desc,
                "location": "Remote",
                "url": link
            })
    except Exception as e:
        print(f"Error scraping jobs from Wellfound for {company_name}: {e}")
    return jobs