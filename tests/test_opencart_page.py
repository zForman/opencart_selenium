from selenium.webdriver.common.by import By
import pytest


@pytest.mark.parametrize('expected_status', [200])
@pytest.mark.parametrize('engine', ['OpenCart'])
def test_is_open_cart_page(call_api, engine, pytestconfig, expected_status):
    get_status = call_api.get_status()
    browser = pytestconfig.getoption('--browser')
    get_driver = call_api.web_browser(browser=browser)
    driver, url = get_driver
    driver.get(url)
    element = driver.find_element(By.XPATH, "//a[contains(text(),'OpenCart')]")
    assert element.text == engine
    driver.close()
    assert expected_status == get_status.status_code

