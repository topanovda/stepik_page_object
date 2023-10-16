from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import pytest
import time

# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


@pytest.mark.parametrize(
    "link",
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        # pytest.param(
        #     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        #     marks=pytest.mark.xfail,
        # ),
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    ],
)
def test_guest_can_add_product_to_basket(driver, link):
    page = ProductPage(driver, link)
    page.open()
    page.should_be_newYear_url()
    page.should_not_be_success_message()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    # page.test_guest_cant_see_success_message_after_adding_product_to_basket()
    page.product_name_matches_the_one_added()
    page.the_price_of_the_cart_is_the_same_as_the_price_of_the_product()

    time.sleep(10)


def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()
