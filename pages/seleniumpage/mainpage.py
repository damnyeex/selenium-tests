from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.selenium.dev/")

    def click_webdriver_tool(self):
        webdriver_tool = self.driver.find_element(By.XPATH,'''//a[@class='selenium-button selenium-webdriver text-uppercase fw-bold']''')
        self.driver.execute_script("arguments[0].click();", webdriver_tool)