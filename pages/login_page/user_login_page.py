from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time


class UserLoginPage(BasePage):

    _login_user_button = (By.XPATH, "//a[contains(text(),'Login')]")
    _user_email = (By.ID, 'input-email')
    _password = (By.ID, 'input-password')
    _submint_button = (By.XPATH, "//input[@class='btn btn-primary']")
    _click_on_my_account = (By.XPATH, "//span[contains(text(),'My Account')]")
    _click_on_login = (By.XPATH, "//a[contains(text(),'Login')]")
    _click_on_logout = (By.CSS_SELECTOR, '.dropdown-menu-right li:last-child a')
    _confirm_logout = (By.XPATH, "//a[@class='btn btn-primary']")
    _my_orders_title = (By.XPATH, "//h2[contains(text(),'My Orders')]")

    def _enter_username(self, email):
        return self.find_element(locator=self._user_email).send_keys(email)

    def _enter_password(self, password):
        return self.find_element(locator=self._password).send_keys(password)

    def get_my_orders_title(self):
        return self.find_element(locator=self._my_orders_title)

    def click_on_my_account(self):
        return self.click(self._click_on_my_account)

    def click_on_login(self):
        return self.click(self._click_on_login)

    def click_on_logout(self):
        return self.click(self._click_on_logout)

    def click_login_button(self):
        return self.click(locator=self._submint_button)

    def click_on_confirm_logout(self):
        return self.click(locator=self._confirm_logout)

    def login(self, useremail, password):
        self.click_on_my_account()
        self.click_on_login()
        self._enter_username(useremail)
        self._enter_password(password)
        self.click_login_button()

    def logout(self):
        self.click_on_my_account()
        self.click_on_logout()
        self.click_on_confirm_logout()
