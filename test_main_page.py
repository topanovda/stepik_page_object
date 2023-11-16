import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


# def test_guest_can_go_to_login_page(driver):
#     link = "http://selenium1py.pythonanywhere.com/"
#     driver.get(link)
#     # time.sleep(5)
#     login_link = driver.find_element("css selector", "#login_link").click()


# def go_to_login_page(driver):
#     login_link = driver.find_element("css selector", "#login_link").click()


# def test_guest_can_go_to_login_page(driver):
#     link = "http://selenium1py.pythonanywhere.com/"
#     driver.get(link)
#     go_to_login_page(driver)

link = "http://selenium1py.pythonanywhere.com/"


# def test_guest_should_see_login_link(driver):
#     page = MainPage(driver, link)
#     page.open()
#     page.should_be_login_link()


# def test_guest_can_go_to_login_page(driver):
#     page = MainPage(
#         driver, link
#     )  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()  # открываем страницу
#     page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
#     login_page = LoginPage(driver, driver.current_url)  # получаем страницу логина
#     login_page.should_be_login_page()  # выполняем проверки страницы логина


def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.go_to_basket()  # переходим в корзину
    basket_page = BasketPage(driver, driver.current_url)  # получаем страницу корзины
    basket_page.should_be_basket_empty()  # выполняем проверку что корзина пуста
