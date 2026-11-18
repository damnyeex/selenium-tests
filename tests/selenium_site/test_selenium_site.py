from pages.selenium_site_pages.main_page import MainPage
from pages.selenium_site_pages.webdriver_page import WebdriverPage
from pages.selenium_site_pages.projects_page import ProjectPage

def test_open_selenium_webdriver(driver):
    main_page = MainPage(driver)
    webdriver_page = WebdriverPage(driver)

    main_page.open()
    main_page.click_webdriver_tool()
    webdriver_page.check_tittle_is('WebDriver')

def test_len_selenium_projects(driver):
    main_page = MainPage(driver)
    projects_page = ProjectPage(driver)

    main_page.open()
    projects_page.click_projects_nav_link()
    projects_page.check_projects_url("https://www.selenium.dev/projects/")
    projects_page.check_count_projects(3)