from pages.spring_app_pages.login_page import LoginPage
from config import BASE_URL
import pytest

@pytest.mark.parametrize(
    'creds',
    [
    pytest.param(("admin", "admin123"), id="admin login"),
    pytest.param(("user3", "user3"), id="user3 login"),
    pytest.param(("user4", "user4"), id="user4 login"),
    pytest.param(("user5", "user5"), id="user5 login"),
    ]
)

def test_login_localhost(driver, creds):
    login, password = creds
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.fill_login_field(login)
    login_page.fill_password_field(password)
    login_page.submit_login_button()
    login_page.wait_main_url()
    login_page.check_login_complete(f'{BASE_URL}')
    login_page.click_logout()
    login_page.check_logout_complete(f'{BASE_URL}/login')

users = ["admin123", "user1", "user12", "user123"]
passwords = ["admin123", "user3", "user4", "user5"]

def generate_pairs():
    pairs = []
    for user in users:
        for password in passwords:
            pairs.append(pytest.param((user, password), id=f"{user}:{password}"))
    return pairs

@pytest.mark.parametrize('failed_creds', generate_pairs())
def test_login_localhost_failed(driver, failed_creds):
    login, password = failed_creds
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.fill_login_field(login)
    login_page.fill_password_field(password)
    login_page.submit_login_button()
    login_page.catch_error_message('Invalid credentials')

