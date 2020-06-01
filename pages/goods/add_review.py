from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time

class AddReview(BasePage):
    _nav_to_tablets_section = (By.XPATH, "//ul[@class='nav navbar-nav']//a[contains(text(),'Tablets')]")
    _choose_device = (By.XPATH, "//div[@class='caption']//a[contains(text(),'Samsung Galaxy Tab 10.1')]")
    _click_on_write_review = (By.XPATH, "//a[contains(text(),'Write a review')]")
    _input_name = (By.ID, "input-name")
    _input_review = (By.ID, "input-review")
    _add_rating = (By.CSS_SELECTOR, "input[name='rating'][value='5']")
    _click_on_confirm_review = (By.XPATH, "//button[@id='button-review']")
    _check_if_review_is_added = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def nav_to_tablets_section(self):
        return self.click(locator=self._nav_to_tablets_section)

    def click_on_device(self):
        return self.click(locator=self._choose_device)

    def click_on_write_review(self):
        self.click(self._click_on_write_review)

    def add_author(self, author):
        self.input_text(self._input_name, author)

    def add_review(self, review):
        self.input_text(self._input_review, review)

    def choose_rating(self):
        self.click(self._add_rating)

    def confirm_review(self):
        self.click(self._click_on_confirm_review)

    def check_if_review_is_added(self):
        return self.find_element(self._check_if_review_is_added)

    def write_review(self, author, comment):
        self.nav_to_tablets_section()
        self.click_on_device()
        time.sleep(3)
        self.click_on_write_review()
        self.add_author(author)
        self.add_review(comment)
        self.choose_rating()
        self.confirm_review()
