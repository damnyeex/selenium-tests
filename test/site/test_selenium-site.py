from pages.seleniumpage.mainpage import MainPage
from pages.seleniumpage.webdriverpage import WebdriverPage
from pages.seleniumpage.projectspage import ProjectPage

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