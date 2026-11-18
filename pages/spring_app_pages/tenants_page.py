from selenium.webdriver.common.by import By
from pages.base_page import BasePage

title_selector = (By.CSS_SELECTOR, 'h2')
tenant_info_selector = (By.CSS_SELECTOR, '.tenant-name')
tenant_detail_btn_selector = (By.XPATH, '''//*[@class='base-button base-button--secondary details-button'][1]''')

class TenantsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Шаблон локатора шапки в деталях тенанта: в {} подставляется имя селектора
    Header_INFO_DIV = "//div[@class='tenant-info-header']//{}"

    def get_header_info_text(self, tag:str) -> str:
        """Возвращает текст элемента с указанным тегом внутри .tenant-info-header."""
        element = self.driver.find_element(
            By.XPATH, self.Header_INFO_DIV.format(tag)
        )
        return element.text
    """Возвращает текст элементов с указанным тегом внутри .tenant-info-header."""
    def get_header_title_and_value(self) -> tuple[str, str]:
        return (
            self.get_header_info_text('h2'),
            self.get_header_info_text('p'),
            )


    def check_tenant_page_title(self, name):
        title = self.find(title_selector).text
        assert (name == title)

    def check_tenant_info(self, name):
        tenant_name = self.find(tenant_info_selector).text
        assert (name == tenant_name)

    def click_tenant_detail_btn(self):
        detail_btn = self.find(tenant_detail_btn_selector)
        detail_btn.click()

    def check_header_tag_text(self, tag: str, expected_value: str):
        actual = self.get_header_info_text(tag)
        assert actual == expected_value, (
            f"Ожидал {expected_value!r} в <{tag}>, получен {actual!r}"
        )

    def check_header_title_and_value(self, expected_title: str, expected_value: str):
        title, value = self.get_header_title_and_value()
        assert title == expected_title, f"Ожидал title {expected_title!r}, получен {title!r}"
        assert value == expected_value, f"Ожидал value {expected_value!r}, получен {value!r}"


