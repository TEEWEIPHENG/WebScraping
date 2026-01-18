import os
from dotenv import load_dotenv

load_dotenv()

# Database configuration
# Use /app/data for Docker, ./web_scraper.db for local
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./web_scraper.db")
DATABASE_ECHO = os.getenv("DATABASE_ECHO", "False").lower() == "true"

# App configuration
APP_NAME = "Web Scraper Service"
APP_VERSION = "1.0.0"
