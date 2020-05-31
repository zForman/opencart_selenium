from pages.login_page.user_login_page import UserLoginPage
from pages.home.main_home_page import HomePage
from pages.goods.clean_cart import CleanCart
import time


def test_clean(one_time_setup):
    login_page = UserLoginPage(one_time_setup)
    clean_cart = CleanCart(one_time_setup)
    home_page = HomePage(one_time_setup)
    login_page.login()
    clean_cart.cleaan_cart()
    time.sleep(1)
    assert "0 item(s) - $0.00" == home_page.check_is_item_in_cart()

