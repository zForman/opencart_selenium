from selenium import webdriver
import requests


class APICall:
    def __init__(self, base_url):
        self.base_url = base_url

    def web_browser(self, browser):
        if browser == 'Chrome':
            driver = webdriver.Chrome(executable_path='webdrivers/chromedriver')

        elif browser == 'Firefox':
            driver = webdriver.Firefox(executable_path='webdrivers/geckodriver')

        else:
            driver = webdriver.Safari()

        return driver, self.base_url

    def get_status(self):
        url = self.base_url
        return requests.get(url=url)
