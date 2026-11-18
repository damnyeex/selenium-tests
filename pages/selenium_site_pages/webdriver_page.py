from selenium.webdriver.common.by import By
from pages.base_page import BasePage

webdriver_tool_selector = (By.CSS_SELECTOR, 'h1')

class WebdriverPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_tittle_is(self, title):
        page_title = self.find(webdriver_tool_selector)
        assert page_title.text == title
