import pytest
from pages.localhost.loginpage import LoginPage

CREDS = {
    "admin": ("admin", "admin123"),
    "user3": ("user3", "user3"),
}

URLS = {
    "tenants": "http://localhost:5173/tenants",
    "users":   "http://localhost:5173/users",
    "admin":   "http://localhost:5173/admin",
}

@pytest.fixture()
def logged_in_page(driver, creds):
    login, password = creds
    LoginPage(driver).login(login, password)

    assert driver.current_url.rstrip("/") == "http://localhost:5173", (
        f"Логин не удался. Текущий URL: {driver.current_url}"
    )
    return driver

@pytest.fixture()
def page_url(request):
    return URLS[request.param]

@pytest.fixture()
def creds(request):
    return CREDS[request.param]