from selenium.webdriver.common.by import By
from pages.base_page import BasePage

projects_link_selector = (By.XPATH, '''//*[@id='main_navbar']/ul[1]/li/a/span[text()='Projects']''')
projects_selector = (By.CSS_SELECTOR, '.alert')

class ProjectPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def click_projects_nav_link (self):
        projects_link = self.find(projects_link_selector)
        projects_link.click()

    def check_projects_url(self, url):
        projects_url = self.driver.current_url
        assert projects_url == url, \
            f"Ожидался URL ${url}, получен {projects_url}"

    def check_count_projects(self, count):
        projects = self.find(projects_selector)
        assert len(projects) == count