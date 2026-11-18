from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.waits import wait_current_url

login_selector = (By.CSS_SELECTOR, "#login")
password_selector = (By.CSS_SELECTOR, "#password")
submit_login_btn_selector = (By.CSS_SELECTOR, ".login-button")
logout_btn_selector = (By.XPATH, '''//div[@class='nav-action']/button/span[text()='Выйти']''')
error_message_selector = (By.CSS_SELECTOR, '.error-message')

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get("http://localhost:5173/login")

    def fill_login_field(self, login):
        self.find(login_selector).send_keys(login)

    def fill_password_field(self, password):
        self.find(password_selector).send_keys(password)

    def submit_login_button(self):
        login_btn = self.find(submit_login_btn_selector)
        login_btn.click()

    def wait_main_url(self):
        wait_current_url(self)

    def check_login_complete(self, url):
        main_page = self.driver.current_url
        assert (url == main_page), \
            f"Ожидался URL ${url}, получен {main_page}"

    def click_logout(self):
        logout_btn = self.find(logout_btn_selector)
        self.driver.execute_script("arguments[0].click();", logout_btn)

    def check_logout_complete(self, url):
        login_page = self.driver.current_url
        assert (url == login_page), \
            f"Ожидался URL ${url}, получен {login_page}"

    def catch_error_message(self, message):
        error_message = self.find(error_message_selector).text
        assert (message == error_message)

    def login(self, login, password):
        self.open_login_page()
        self.fill_login_field(login)
        self.fill_password_field(password)
        self.submit_login_button()
        self.wait_main_url()
        return self

