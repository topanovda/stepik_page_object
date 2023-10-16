from .locators import ProductPageLocators
from .base_page import BasePage
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_newYear_url()
        # Проверка, что нет сообщения что товар в корзине
        self.should_not_be_success_message()
        # Добавление товара в корзину
        self.add_to_basket()
        # Вызов метода с математической операцией из класса BasePage
        self.solve_quiz_and_get_code()
        # Проверяем что нет сообщения об успехе
        self.test_guest_cant_see_success_message_after_adding_product_to_basket()
        # проверяем что сообщение пропадает после успешного добавления в корзину
        self.test_message_disappeared_after_adding_product_to_basket()
        # Сообщение о том, что товар добавлен в корзину. Название товара в сообщении долежн совпадать с тем товаром, который вы действительно добавили
        # self.product_name_matches_the_one_added()
        # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара

        # self.test_guest_can_go_to_login_page_from_product_page()

    def should_be_newYear_url(self):
        current_url = self.driver.current_url
        assert (
            "?promo=offer" in current_url
        ), f"Expected '?promo=offer1' in URL, but got: {current_url}"

    def should_not_be_success_message(self):
        # Проверяем, что элемент не появляется на странице в течение заданного времени
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def add_to_basket(self):
        add_basket = self.driver.find_element(
            *ProductPageLocators.ADD_BASKET_BUTTON
        ).click()

    def product_name_matches_the_one_added(self):
        # Проверяем наличие элемента с сообщением, что товар добавлен к корзину
        assert self.is_element_present(
            *ProductPageLocators.ITEM_ADDED_TO_CART
        ), "Message about adding is not presented"
        # Находим элемент и переводим сообщение в текст
        message = self.driver.find_element(*ProductPageLocators.ITEM_ADDED_TO_CART).text
        # Находим элемент и переводим название товара в текст
        product_name = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # Проверяем, что название товара в сообщении совпадает с товаром, который мы добавили
        assert product_name == message, "There is no such product in the message"

    def the_price_of_the_cart_is_the_same_as_the_price_of_the_product(self):
        # Проверяем наличие элемента с сообщением о стоимости товара
        assert self.is_element_present(
            *ProductPageLocators.BASKET_VALUE
        ), "Cart value not shown"
        # Находим элемент с ценой в сообщении и переводим в текст
        basket_value = self.driver.find_element(*ProductPageLocators.BASKET_VALUE).text
        # Находим элемент с ценой товара и переводим в текст
        cost_of_good = self.driver.find_element(*ProductPageLocators.COST_OF_GOOD).text
        # Проверяем, что цена товара совпадает с ценой в сообщении
        assert (
            cost_of_good == basket_value
        ), "The price of the cart does not match the price of the product"

    # @pytest.mark.xfail(reason="Падает")
    # def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
    #     # Проверяем, что элемента нет на странице
    #     assert self.is_not_element_present(
    #         *ProductPageLocators.SUCCESS_MESSAGE
    #     ), "Success message is presented, but should not be"

    # @pytest.mark.xfail(reason="Падает")
    # def test_message_disappeared_after_adding_product_to_basket(
    #     self, how, what, timeout=4
    # ):
    #     # проверка на исчезание элемента на странице
    #     try:
    #         WebDriverWait(self.driver, timeout, 1, TimeoutException).until_not(
    #             EC.presence_of_element_located((ProductPageLocators.SUCCESS_MESSAGE))
    #         )
    #     except TimeoutException:
    #         return False

    #     return True

    # def should_be_book_name(self):
    #     assert self.is_element_present(
    #         *ProductPagaLocators.
    #     ), "Login email is not presented"
