from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_newYear_url()
        self.add_to_basket
        # Вызов метода с математической операцией из класса BasePage
        self.solve_quiz_and_get_code()
        # Сообщение о том, что товар добавлен в корзину. Название товара в сообщении долежн совпадать с тем товаром, который вы действительно добавили
        self.product_name_matches_the_one_added()
        # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара
        self.the_price_of_the_cart_is_the_same_as_the_price_of_the_product()

    def should_be_newYear_url(self):
        current_url = self.driver.current_url
        assert (
            "?promo=offer1" in current_url
        ), f"Expected '?promo=offer1' in URL, but got: {current_url}"

    def add_to_basket(self):
        add_basket = self.driver.find_element(
            *ProductPageLocators.ADD_BASKET_BUTTON
        ).click()

    def product_name_matches_the_one_added(self, product_name):
        # Проверяем наличие элемента с сообщением, что товар добавлен к корзину
        assert self.is_element_present(
            *ProductPageLocators.ITEM_ADDED_TO_CART
        ), "Message about adding is not presented"
        # Находим элемент и переводим сообщение в текст
        message = self.browser.find_element(
            *ProductPageLocators.ITEM_ADDED_TO_CART
        ).text
        # Находим элемент и переводим название товара в текст
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # Проверяем, что название товара в сообщении совпадает с товаром, который мы добавили
        assert product_name == message, "There is no such product in the message"

    def the_price_of_the_cart_is_the_same_as_the_price_of_the_product(
        self, basket_value
    ):
        # Проверяем наличие элемента с сообщением о стоимости товара
        assert self.is_element_present(
            *ProductPageLocators.BASKET_VALUE
        ), "Cart value not shown"
        # Находим элемент с ценой в сообщении и переводим в текст
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        # Находим элемент с ценой товара и переводим в текст
        cost_of_good = self.browser.find_element(*ProductPageLocators.COST_OF_GOOD).text
        # Проверяем, что цена товара совпадает с ценой в сообщении
        assert (
            cost_of_good == basket_value
        ), "The price of the cart does not match the price of the product"

    # def should_be_book_name(self):
    #     assert self.is_element_present(
    #         *ProductPagaLocators.
    #     ), "Login email is not presented"
