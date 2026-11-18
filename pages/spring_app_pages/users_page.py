from selenium.webdriver.common.by import By
from pages.base_page import BasePage

profile_btn_selector = (By.XPATH, '''//ul[@class='users-list']/li[@class='user-card'][1]/div[@class='user-actions']/button''')

class UsersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Шаблон локатора: в {} подставляется имя поля
    FIELD_DIV = "//div[@class='profile-field'][label[normalize-space()='{}']]"

    def get_profile_field(self, field_name: str) -> tuple[str, str]:
        """Возвращает (label_text, value_text) для указанного поля."""
        field_div = self.driver.find_element(
            By.XPATH, self.FIELD_DIV.format(field_name)
        )
        label = field_div.find_element(By.TAG_NAME, "label").text
        value = field_div.find_element(By.TAG_NAME, "span").text
        return label, value

    def click_user_profile(self):
        user_profile_btn = self.find(profile_btn_selector)
        user_profile_btn.click()

    def check_user_profile_field(self, field_name:str, expected_value: str,):
        label, value = self.get_profile_field(field_name)
        assert label == field_name, f"Ожидали label {field_name!r}, получили {label!r}"
        assert value == expected_value, f"Ожидали {expected_value!r} в поле {field_name!r}, получили {value!r}"
