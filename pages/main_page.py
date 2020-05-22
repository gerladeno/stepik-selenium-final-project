from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Can't find login link using {}".format(
            MainPageLocators.LOGIN_LINK)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
