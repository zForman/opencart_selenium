import time
from pages.home.main_home_page import HomePage


def test_num_el_in_feature_section(one_time_setup):
    page = HomePage(one_time_setup)
    num_of_items_on_mainpage = page.num_of_el_in_feature_section()
    assert len(num_of_items_on_mainpage) == 4


def test_add_item_in_cart(one_time_setup):
    page = HomePage(one_time_setup)
    page.add_item_in_cart()
    result = page.check_is_item_in_cart()
    assert '$0.00' not in result.text


def test_wish_list(one_time_setup):
    page = HomePage(one_time_setup)
    page.click_add_to_wish_list()


def test_search_positive(one_time_setup):
    page = HomePage(one_time_setup)
    page.search('iphone')
    result = page.check_search_result()
    print(result.text)
    assert 'meeting the search criteria' in result.text


def test_search_negative(one_time_setup):
    page = HomePage(one_time_setup)
    page.search('alcatel')
    result = page.check_search_result('negative')
    print(result)
    assert 'no' in result.text
