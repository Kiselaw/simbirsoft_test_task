from selenium.common.exceptions import TimeoutException
from .base import BasePage

class AccountPageLocators:
    """Класс для хранения XPATH."""
    DEPOSIT_BUTTON = "//button[contains(text(), 'Deposit')]"
    WITHDRAWL_BUTTON = "//button[contains(text(), 'Withdrawl')]"
    AMOUNT_INPUT = "//input[@type='number']"
    SUBMIT_BUTTON = "//button[@type='submit']"
    BALANCE = "//strong[@class='ng-binding'][2]"
    ACCOUNT_SELECT = "//select[@name='accountSelect']"
    ACCOUNT_OPTION_1 = "//select[@name='accountSelect']/option[1]"
    ACCOUNT_OPTION_2 = "//select[@name='accountSelect']/option[2]"
    USER_NAME = "//strong/span[contains(text(), 'Harry')]"


class AccountPage(BasePage):
    """Класс для методов страницы счета."""
    def deposit(self, amount):
        deposit_button = self.get_element(AccountPageLocators.DEPOSIT_BUTTON)
        self.click(deposit_button)
        amount_input = self.get_element(AccountPageLocators.AMOUNT_INPUT)
        self.input(amount_input, amount)
        submit_button = self.get_element(AccountPageLocators.SUBMIT_BUTTON)
        self.click(submit_button)

    def withdrawal(self, amount):
        withdrawl_button = self.get_element(AccountPageLocators.WITHDRAWL_BUTTON)
        self.click(withdrawl_button)
        amount_input = self.get_element(AccountPageLocators.AMOUNT_INPUT)
        self.input(amount_input, amount)
        submit_button = self.get_element(AccountPageLocators.SUBMIT_BUTTON)
        self.click(submit_button)

    def get_balance(self):
        balance = self.get_element(AccountPageLocators.BALANCE)
        return balance

    def swap_accounts(self):
        account_select = self.get_element(AccountPageLocators.ACCOUNT_SELECT)
        self.click(account_select)
        account_option_2 = self.get_element(AccountPageLocators.ACCOUNT_OPTION_2)
        self.click(account_option_2)
        account_option_1 = self.get_element(AccountPageLocators.ACCOUNT_OPTION_1)
        self.click(account_option_1)

    def check_right_user(self):
        try:
            user_name = self.get_element(AccountPageLocators.ACCOUNT_SELECT)
        except TimeoutException:
            user_name = None
        return user_name
