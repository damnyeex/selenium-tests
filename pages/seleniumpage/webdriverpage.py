from selenium.webdriver.common.by import By

class WebdriverPage:
    def __init__(self, driver):
        self.driver = driver

    def check_tittle_is(self, tittle):
        page_tittle = self.driver.find_element(By.CSS_SELECTOR, 'h1')
        assert page_tittle.text == tittle
