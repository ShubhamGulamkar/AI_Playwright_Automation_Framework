import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "QA")

BASE_URLS = {
    "DEV": "https://dev-your-ctms-url.com",
    "QA": "https://qa-your-ctms-url.com",
    "UAT": "https://uat-your-ctms-url.com"
}

BASE_URL = BASE_URLS[ENV]
