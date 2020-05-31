from pages.login_page.user_login_page import UserLoginPage
from pages.goods.add_review import AddReview
import time


_author = 'Pol'

_comment = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


def test_add_review(one_time_setup):
    login_page = UserLoginPage(one_time_setup)
    review_page = AddReview(one_time_setup)
    login_page.login('user@mail.com', '1234')
    time.sleep(3)
    review_page.write_review(_author, _comment)
    assert 'Thank you for your review' in review_page.check_if_review_is_added().text
