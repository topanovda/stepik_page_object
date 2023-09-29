from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.driver.current_url
        assert (
            "login" in current_url
        ), f"Expected 'login' in URL, but got: {current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_EMAIL
        ), "Login email is not presented"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_PASSWORD
        ), "Login password is not presented"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_SUBMIT
        ), "Login submit button is not presented"
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_EMAIL
        ), "Register email is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD
        ), "Register password is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_CONFIRM_PASSWORD
        ), "Register confirm password is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_SUBMIT
        ), "Register submit button is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
        assert True
