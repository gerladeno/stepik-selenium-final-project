from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, url):
        assert self.browser.current_url == url, "Url is not {}".format(url)

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Can't find login form using {}".format(
            LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Can't find register form using {}".format(
            LoginPageLocators.REGISTER_FORM)