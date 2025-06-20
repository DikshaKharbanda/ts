import os
from dotenv import load_dotenv
from config import TENDER_URLS, RESULTS_PATH
from agents.tender_agents import create_scraper_agent
from tasks.tender_tasks import create_scrape_task
from crewai import Crew, Process
import json

# Load environment variables
load_dotenv()

def main():
    # Prompt user for keywords
    keywords = input("Enter keywords to search in RFPs (comma-separated): ").split(",")
    keywords = [kw.strip() for kw in keywords if kw.strip()]
    all_results = {}

    for url in TENDER_URLS:
        agent = create_scraper_agent(url)
        task = create_scrape_task(agent, url, keywords)
        crew = Crew(
            agents=[agent],
            tasks=[task],
            verbose=True,
            process=Process.sequential
        )
        result = crew.kickoff()
        # Extract serializable data from CrewAI result object
        if hasattr(result, "raw"):
            all_results[url] = result.raw
        elif hasattr(result, "dict"):
            all_results[url] = result.dict()
        elif hasattr(result, "json_dict"):
            all_results[url] = result.json_dict
        else:
            all_results[url] = str(result)

    # Ensure the results directory exists
    os.makedirs(os.path.dirname(RESULTS_PATH), exist_ok=True)
    with open(RESULTS_PATH, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {RESULTS_PATH}")

if __name__ == "__main__":
    main()
