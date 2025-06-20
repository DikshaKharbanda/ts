from crewai import Task
from datetime import datetime, timedelta

def create_scrape_task(agent, website_url, keywords):
    today = datetime.now()
    two_months_ago = today - timedelta(days=60)
    date_range_str = f"{two_months_ago.strftime('%d-%m-%Y')} to {today.strftime('%d-%m-%Y')}"
    return Task(
        description=(
            f"Scrape all tender/RFP listings from {website_url}. "
            f"Only include tenders published or starting within the last 2 months (from {date_range_str}). "
            f"Filter by these keywords: {', '.join(keywords)}. "
            "Extract and return for each tender: bid_no, bid_url, title, department, start_date, deadline, and PDF/document links if available."
        ),
        expected_output="A JSON list of tenders from the last 2 months, each with bid_no, bid_url, title, department, start_date, deadline, and PDF/document links.",
        agent=agent
    )
