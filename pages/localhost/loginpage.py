from selenium.webdriver.common.by import By
from utils.helpers.webdriver_wait_helpers import wait_current_url

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get("http://localhost:5173/login")

    def fill_login_field(self, selector, login):
        login_field = self.driver.find_element(By.CSS_SELECTOR, selector).send_keys(login)

    def fill_password_field(self, selector, password):
        password_field = self.driver.find_element(By.CSS_SELECTOR, selector).send_keys(password)

    def submit_login_button(self, selector):
        login_btn = self.driver.find_element(By.CSS_SELECTOR, selector)
        login_btn.click()

    def wait_main_url(self):
        wait_current_url(self)

    def check_login_complete(self, url):
        main_page = self.driver.current_url
        assert (url == main_page), \
            f"Ожидался URL ${url}, получен {main_page}"

    def click_logout(self, path):
        logout_btn = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", logout_btn)

    def check_logout_complete(self, url):
        login_page = self.driver.current_url
        assert (url == login_page), \
            f"Ожидался URL ${url}, получен {login_page}"

    def catch_error_message(self, message):
        error_message = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        assert (message == error_message)

