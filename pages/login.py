from .base import BasePage


class LoginPageLocators:
    """Класс для хранения XPATH."""
    CUSTOMER_LOGIN_BUTTON = "//button[contains(text(), 'Customer Login')]"
    SELECT_FORM = "//select[@id='userSelect']"
    USER_LOGIN = "//option[contains(text(), 'Harry')]"
    LOGIN_BUTTON = "//button[contains(text(), 'Login')]"
    ACCOUNT_NAME = "//div/strong/span[contains(text(), 'Harry')]"


class LoginPage(BasePage):
    """Клсасс для методов страницы аутентификации."""
    def login(self):
        customer_login = self.get_element(LoginPageLocators.CUSTOMER_LOGIN_BUTTON)
        self.click(customer_login)
        select_form = self.get_element(LoginPageLocators.SELECT_FORM)
        self.click(select_form)
        user_login = self.get_element(LoginPageLocators.USER_LOGIN)
        self.click(user_login)
        login_button = self.get_element(LoginPageLocators.LOGIN_BUTTON)
        self.click(login_button)
        return self.get_element(LoginPageLocators.LOGIN_BUTTON)
