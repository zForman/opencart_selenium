import time
from pages.login_page.user_login_page import UserLoginPage


def test_user_login_success(one_time_setup):
    page = UserLoginPage(one_time_setup)
    page.login('user@mail.com', '1234')

    assert 'My Orders' == page.get_my_orders_title().text
