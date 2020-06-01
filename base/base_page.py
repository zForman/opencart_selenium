from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import utils.custom_logger as cl
import logging


BASE_URL = 'http://localhost:8046/index.php'


class BasePage:
    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.base_url = BASE_URL

    def find_element(self, locator):
        element = None
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.log.info(f'Element found with locator: {str(locator[1])}')
        except NoSuchElementException:
            self.log.info('Element not found with locator:', locator)
        return element

    def find_elements(self, locator):
        element = None
        try:
            element = self.wait.until(EC.presence_of_all_elements_located(locator))
            self.log.info(f'Element found with locator: {str(locator[1])}')
        except NoSuchElementException:
            self.log.info('Element not found with locator:', locator)
        return element

    def open(self):
        return self.driver.get(self.base_url)

    def get_title(self):
        return self.driver.title

    def click(self, locator):
        element = None
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.log.info(f'Element found with locator: {str(locator[1])} and clicked')
        except NoSuchElementException:
            self.log.info('Element not found with locator:', locator)
        return element.click()

    def input_text(self, locator, value):
        get_field = self.driver.find_element(*locator)
        get_field.clear()
        get_field.send_keys(value)
