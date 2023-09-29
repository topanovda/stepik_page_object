from .pages.product_page import ProductPage
from .pages.base_page import BasePage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(driver):
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
