from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def __init__(self, driver):
    self.driver = driver

def wait_current_url(self):
    current_url = self.driver.current_url
    WebDriverWait(self.driver, 10).until(EC.url_changes(current_url))