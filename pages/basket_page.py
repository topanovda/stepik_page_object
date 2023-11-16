from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY
        ), "Basket is not empty, its full"

    def should_be_basket_full(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_FULL
        ), "Basket is full, it isn't empty"
