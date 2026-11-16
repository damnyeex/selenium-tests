from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProjectPage:
    def __init__(self,driver):
        self.driver = driver

    def click_projects_nav_link (self):
        projects_link = self.driver.find_element(By.XPATH, '//*[@id="main_navbar"]/ul/li[4]/a')
        projects_link.click()

    def wait_current_url(self, current_url):
        WebDriverWait(self.driver, 10).until(EC.url_changes(current_url))

    def check_current_url(self, url):
        projects_url = self.driver.current_url
        assert projects_url == url, \
            f"Ожидался URL ${url}, получен {projects_url}"

    def check_count_projects(self, count):
        projects = self.driver.find_elements(By.CSS_SELECTOR, '.alert')
        assert len(projects) == count