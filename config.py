import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Базовый URL
BASE_URL = os.getenv("BASE_URL", "http://localhost:5173")

# Словарь с URL (для параметризации фикстуры page_url)
URLS = {
    "tenants": os.getenv("URL_TENANTS", f"{BASE_URL}/tenants"),
    "users": os.getenv("URL_USERS", f"{BASE_URL}/users"),
    "admin": os.getenv("URL_ADMIN", f"{BASE_URL}/admin"),
}

# Словарь с кредами
CREDS = {
    "admin": (
        os.getenv("CREDS_ADMIN_LOGIN", "admin"),
        os.getenv("CREDS_ADMIN_PASS", "admin123")
    ),
    "user3": (
        os.getenv("CREDS_USER3_LOGIN", "user3"),
        os.getenv("CREDS_USER3_PASS", "user3")
    ),
}