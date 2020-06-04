from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import utils.custom_logger as cl
import logging


class BasePage:
    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver, wait=3):
        driver, base_url = driver
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.base_url = base_url

    def find_element(self, locator):
        element = None
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.log.info(f'Element with locator: {str(locator[1])} found ')
        except NoSuchElementException:
            self.log.info(f'Element with {locator} not found')
        return element

    def find_elements(self, locator):
        element = None
        try:
            element = self.wait.until(EC.presence_of_all_elements_located(locator))
            self.log.info(f'Element with locator: {str(locator[1])} found ')
        except NoSuchElementException:
            self.log.info(f'Element with {locator} not found')
        return element

    def open(self):
        return self.driver.get(self.base_url)

    def get_title(self):
        return self.driver.title

    def click(self, locator):
        element = None
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.log.info(f'Element with locator: {str(locator[1])} found and clicked')
        except NoSuchElementException:
            self.log.info(f'Element with {locator} not found')
        return element.click()

    def input_text(self, locator, value):
        print('\nlocator', locator[0], locator[1])
        print('*locator', *locator)
        try:
            get_field = self.driver.find_element(*locator)
            get_field.clear()
            get_field.send_keys(value)
            self.log.info(f'Element {locator} found, and value: {value} passed')
        except NoSuchElementException:
            self.log.info(f'Element with {locator} not found, and value: {value} not passed')
