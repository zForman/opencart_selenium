import pytest
from app import APICall


def pytest_addoption(parser):
    parser.addoption(
        '--base_url',
        help='enter URL and port: e.g. http://localhost:8046',
        required=True
    )

    parser.addoption(
        '--browser',
        help='Choose from Chrome, Safari, Firefox',
        choices='Chrome, Safari, Firefox',
        required=True
    )


@pytest.fixture
def call_api(request):
    base_url = request.config.getoption('--base_url')
    return APICall(base_url=base_url)
