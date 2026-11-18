import pytest
from config import CREDS, URLS
from config import BASE_URL
from pages.spring_app_pages.login_page import LoginPage

@pytest.fixture()
def page_url(request):
    return URLS[request.param]

@pytest.fixture()
def creds(request):
    return CREDS[request.param]

@pytest.fixture()
def logged_in_page(driver, creds):
    login, password = creds
    LoginPage(driver).login(login, password)

    assert driver.current_url.rstrip("/") == BASE_URL, (
        f"Логин не удался. Текущий URL: {driver.current_url}"
    )
    return driver