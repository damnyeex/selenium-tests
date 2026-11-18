from selenium.webdriver.common.by import By
from pages.base_page import BasePage

webdriver_tool_selector = (By.XPATH, '''//a[@class='selenium-button selenium-webdriver text-uppercase fw-bold']''')

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get("https://www.selenium.dev/")

    def click_webdriver_tool(self):
        webdriver_tool = self.find(webdriver_tool_selector)
        self.driver.execute_script("arguments[0].click();", webdriver_tool)