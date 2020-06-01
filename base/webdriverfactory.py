from selenium import webdriver
import logging


class WebDriverFactory:
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def get_webdriver(self):

        if self.browser == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--ignore-certificate-errors')
            driver = webdriver.Firefox(options=options)
        elif self.browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(4)
        driver.maximize_window()
        driver.get(self.base_url)
        return driver
