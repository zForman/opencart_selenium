from pages.account_page.edit_account import EditAccountPage
from pages.login_page.user_login_page import UserLoginPage
import pytest
import time


@pytest.mark.parametrize('user_email, password', [('gk@ya.ru', '1234')])
@pytest.mark.parametrize('name, last_name, email, telephone', [('genadiy', 'kurochkin', 'gk@ya.ru', "8563422")])
def test_edit_account_info(one_time_setup, name, last_name, email, telephone, user_email, password):
    page = UserLoginPage(one_time_setup)
    edit_account_page = EditAccountPage(one_time_setup)
    page.login(user_email, password)
    edit_account_page.click_on_edit_account()
    edit_account_page.update_account_information(name, last_name, email, telephone)
    assert 'Success' in edit_account_page.get_success_notification().text
