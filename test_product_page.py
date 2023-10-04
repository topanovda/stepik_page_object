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
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_matches_the_one_added()
    page.the_price_of_the_cart_is_the_same_as_the_price_of_the_product()

    time.sleep(10)
