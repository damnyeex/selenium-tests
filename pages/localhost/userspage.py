from selenium.webdriver.common.by import By

class UsersPage:
    def __init__(self, driver):
        self.driver = driver

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

    def click_user_profile(self, path):
        user_profile_btn = self.driver.find_element(By.XPATH, path)
        user_profile_btn.click()

    def check_user_profile_field(self, field_name:str, expected_value: str,):
        label, value = self.get_profile_field(field_name)
        assert label == field_name, f"Ожидали label {field_name!r}, получили {label!r}"
        assert value == expected_value, f"Ожидали {expected_value!r} в поле {field_name!r}, получили {value!r}"
