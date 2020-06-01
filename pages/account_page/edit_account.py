from selenium.webdriver.common.by import By
from base.base_page import BasePage
import logging
import utils.custom_logger as cl

# Success: Your account has been successfully updated.


class EditAccountPage(BasePage):
    logger = cl.custom_logger(logging.DEBUG)

    _success_update_notif = (By.CSS_SELECTOR, ".alert-success")
    _click_on_submit_changes = (By.CSS_SELECTOR, "input[type='submit']")
    _click_on_edit_account_info = (By.XPATH, "//a[contains(text(),'Edit your account')]")
    _input_first_name = (By.ID, "input-firstname")
    _input_last_name = (By.ID, "input-lastname")
    _input_email = (By.ID, "input-email")
    _input_telephon = (By.ID, "input-telephone")

    def click_on_edit_account(self):
        return self.click(locator=self._click_on_edit_account_info)

    def click_on_submit_changes(self):
        self.click(self._click_on_submit_changes)

    def get_success_notification(self):
        return self.find_element(locator=self._success_update_notif)

    def update_account_information(self, new_first_name, new_password, new_email, new_telephon):
        self.input_text(self._input_first_name, new_first_name)
        self.input_text(self._input_last_name, new_password)
        self.input_text(self._input_email, new_email)
        self.input_text(self._input_telephon, new_telephon)
        self.click_on_submit_changes()

