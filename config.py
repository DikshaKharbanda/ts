import os
from pathlib import Path

# List of government tender websites to scrape
TENDER_URLS = [
    "https://gem.gov.in/",
    "https://eprocure.gov.in",
    "https://etenders.gov.in",
    "https://www.cppp.gov.in/",
    "https://mahatenders.gov.in/",
    "https://www.tendersontime.com/",
    "https://www.tenderwizard.com/",
    "https://www.bidassist.com/",
    "https://www.tenderdetail.com/",
    "https://www.indiatenders.com/",
    "https://etenders.gov.in/eprocure/app",
    "https://democppp.nic.in/cppp8/latestactivetendersnew/cpppdata"
]

# Path to save the results JSON file
RESULTS_PATH = Path("./data/results.json")

# Directory for prompt templates (if needed)
PROMPTS_PATH = Path("./prompts")

# Directory for downloads (e.g., PDFs)
DOWNLOADS_PATH = Path("./downloads")

# Create necessary directories if they don't exist
def create_directories():
    directories = [
        RESULTS_PATH.parent,
        PROMPTS_PATH,
        DOWNLOADS_PATH
    ]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✅ Directory created/verified: {directory}")

# Default request headers for scraping
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

# Scraping and tender search configuration
TENDER_CONFIG = {
    'max_tenders_per_site': 20,
    'request_timeout': 30,
    'delay_between_requests': 2,
    'max_retries': 3,
    'date_formats': [
        '%d-%m-%Y',
        '%d/%m/%Y',
        '%Y-%m-%d',
        '%Y/%m/%d',
        '%d %b %Y',
        '%d %B %Y'
    ]
}

# Keywords for different tender categories (optional, for advanced filtering)


# Initialize directories when config is imported
create_directories()
