import pytest
from base.webdriverfactory import WebDriverFactory


@pytest.fixture
def one_time_setup(request, browser, base_url):
    wdf = WebDriverFactory(browser, base_url)
    driver = wdf.get_webdriver()
    yield driver, base_url
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='chrome'
    )

    parser.addoption(
        '--base_url',
        default='http://localhost:80',
    )


@pytest.fixture
def browser(request):
    return request.config.getoption('--browser').lower()


@pytest.fixture
def base_url(request):
    return request.config.getoption('--base_url').lower()
