from pages.admin.admin_login_page.admin_login_page import AdminLoginPage
import time


def test_admin_login(one_time_setup):
    admin_page = AdminLoginPage(one_time_setup)
    admin_page.login('user', 'bitnami1')
    admin_page.choose_product()
    admin_page.click_on_edit_item()
    time.sleep(6)