import time

from .pages.main_page import MainPage


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


def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(
        driver, link
    )  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
