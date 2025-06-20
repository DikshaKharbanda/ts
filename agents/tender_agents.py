import os
from crewai import Agent, LLM
from crewai_tools import SeleniumScrapingTool

gemini_api_key = os.getenv("GEMINI_API_KEY")

gemini_llm = LLM(
    model="gemini/gemini-2.0-flash",  # Or "gemini/gemini-2.5-pro"
    api_key=gemini_api_key,
    temperature=0.7
)

def create_scraper_agent(website_url):
    return Agent(
        role="Tender Scraper",
        goal="Extract recent RFPs or tenders from the provided website using given keywords",
        backstory="Expert in scraping government and procurement portals for the latest opportunities.",
        tools=[SeleniumScrapingTool(website_url=website_url)],
        llm=gemini_llm,  # Explicitly assign Gemini LLM
        verbose=True
    )
