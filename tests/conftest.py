import pytest
from base.webdriverfactory import WebDriverFactory


@pytest.fixture
def one_time_setup(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='chrome'
    )


@pytest.fixture
def browser(request):
    return request.config.getoption('--browser')
