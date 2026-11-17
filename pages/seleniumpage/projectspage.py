from selenium.webdriver.common.by import By

class ProjectPage:
    def __init__(self,driver):
        self.driver = driver

    def click_projects_nav_link (self):
        projects_link = self.driver.find_element(By.XPATH, '//*[@id="main_navbar"]/ul/li[4]/a')
        projects_link.click()

    def check_projects_url(self, url):
        projects_url = self.driver.current_url
        assert projects_url == url, \
            f"Ожидался URL ${url}, получен {projects_url}"

    def check_count_projects(self, count):
        projects = self.driver.find_elements(By.CSS_SELECTOR, '.alert')
        assert len(projects) == count