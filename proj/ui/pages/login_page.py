from ui.pages.base_page import BasePage
from ui.locators.pages_locators import LoginPageLocators

LOGIN = ''
PASSWORD = ''
BASE_TIMEOUT = 5


class LoginPage(BasePage):

    locators = LoginPageLocators()

    def credentials(self, login=LOGIN, password=PASSWORD):
        self.click_on_element(LoginPageLocators.HEADER_BUTTON)
        self.send_keys_to_input(LoginPageLocators.LOGIN_INPUT, login)
        self.send_keys_to_input(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)
        return LoginPage
