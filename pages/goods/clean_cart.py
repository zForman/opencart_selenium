from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.login_page.user_login_page import UserLoginPage


class CleanCart(BasePage):
    _remove_all_item = (By.CSS_SELECTOR, 'button[title="Remove"]')

    def cleaan_cart(self):
        self.driver.execute_script("""
        $("button[title='Remove']").click()
        """)
