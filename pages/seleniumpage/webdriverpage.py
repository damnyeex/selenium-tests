from selenium.webdriver.common.by import By

class WebdriverPage:
    def __init__(self, driver):
        self.driver = driver

    def check_tittle_is(self, title):
        page_title = self.driver.find_element(By.CSS_SELECTOR, 'h1')
        assert page_title.text == title
