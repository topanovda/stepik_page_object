from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):
        login_link = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        alert = self.driver.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK
        ), "Login link is not presented"

    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
