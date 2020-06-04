from base.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminLoginPage(BasePage):

    _username = (By.ID, 'input-username')
    _password = (By.ID, 'input-password')
    _click_on_login_button = (By.CSS_SELECTOR, "button[type='submit']")
    _click_on_catalog = (By.XPATH, "//a[contains(text(),'Catalog')]")
    _click_on_products = (By.XPATH, "//a[contains(text(),'Products')]")
    _click_on_item = (By.XPATH, "//a[contains(text(),'Products')]")
    _edit_item = (By.CSS_SELECTOR, '.btn-primary:nth-child(1)')

    def input_name(self):
        return self.find_element(self._username)

    def input_password(self):
        return self.find_element(self._password)

    def click_login_button(self):
        return self.click(self._click_on_login_button)

    def input_and_submit(self, user, password):
        self.input_name().send_keys(user)
        self.input_password().send_keys(password)
        self.click_login_button()

    def click_on_catalog(self):
        return self.click(self._click_on_catalog)

    def click_on_product(self):
        return self.click(self._click_on_products)

    def click_on_item(self):
        return self.click(self._click_on_item)

    def click_on_edit_item(self):
        _edit_item = self.find_element(self._edit_item)
        self.driver.execute_script("return arguments[0].click();", _edit_item)
        # return self.driver.execute_script("$('.btn-primary:nth-child(1)')[0].click();")

    def login(self, user, password):
        self.input_and_submit(user, password)

    def choose_product(self):
        self.click_on_catalog()
        self.click_on_product()
