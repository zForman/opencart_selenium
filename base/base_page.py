from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'http://localhost:8046/index.php'


class BasePage:
    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.base_url = BASE_URL

    def find_element(self, locator, time_out=10):
        # print('locator is', locator)
        return self.wait.until(EC.presence_of_element_located(locator),
                               message=f'Can\'t find elements by locator {locator}')

    def find_elements(self, locator, time_out=10):
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                               message=f"Can't find elements by locator {locator}")

    def get_title(self):
        return self.driver.title

    def click(self, locator, time_out=10):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.click()

    def open(self):
        return self.driver.get(self.base_url)
