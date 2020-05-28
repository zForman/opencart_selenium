from base.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    _login_link = (By.XPATH, "//a[contains(text(),'Login')]")
    _home_title = (By.XPATH, "//a[contains(text(),'Your Store')]")
    _feaure_section = (By.CSS_SELECTOR, "h4 a")
    _macbook_item = (By.XPATH, "//a[contains(text(),'MacBook')]")
    _add_item_to_cart = (By.CSS_SELECTOR, "div.col-lg-3:nth-child(1) span.hidden-xs")
    _cart_total = (By.CSS_SELECTOR, "#cart-total")
    _add_to_wishlist = (By.XPATH, "//button[@data-original-title='Add to Wish List'][1]")
    _search = (By.CSS_SELECTOR, '#search input')
    _search_button = (By.CSS_SELECTOR, '#search .btn-lg')
    _search_result_positive = (By.CSS_SELECTOR, 'h2:nth-child(6)')
    _search_result_negative = (By.CSS_SELECTOR, 'p:nth-child(7)')
    _go_to_shopping_cart = (By.XPATH, "//span[contains(text(),'Shopping Cart')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def num_of_el_in_feature_section(self):
        return self.find_elements(locator=self._feaure_section)

    def add_item_in_cart(self):
        return self.find_element(locator=self._add_item_to_cart).click()

    def check_is_item_in_cart(self):
        element = self.find_element(locator=self._cart_total)
        return element

    def click_add_to_wish_list(self):
        element = self.find_element(locator=self._add_to_wishlist)
        return element.click()

    def _set_search_query(self, query):
        element = self.find_element(locator=self._search)
        element.send_keys(query)

    def click_button_search(self):
        element = self.find_element(locator=self._search_button)
        element.click()

    def check_search_result(self, type_test='positive'):
        if type_test == 'negative':
            return self.find_element(locator=self._search_result_negative)
        else:
            return self.find_element(locator=self._search_result_positive)

    def search(self, query='iphone'):
        self._set_search_query(query)
        self.click_button_search()

    def go_to_shopping_cart(self):
        self.find_element(locator=self._go_to_shopping_cart)
