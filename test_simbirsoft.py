from datetime import datetime as dt
import allure
import pytest

from helpers import fib
from pages.account import AccountPage
from pages.login import LoginPage
from pages.transactions import TransactionsPage

DAY = dt.today().date().day + 1
TEST_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"


@allure.title("Тестирование процесса аутентификации")
@pytest.mark.parametrize("driver", ['chrome', 'firefox', 'edge'], indirect=True)
def test_login(driver):
    page = LoginPage(driver)
    page.get_the_page(TEST_URL)
    page.login()


@allure.title("Тестирование осуществления транзакций")
@pytest.mark.parametrize("driver", ['chrome', 'firefox', 'edge'], indirect=True)
def test_account(driver):
    page = AccountPage(driver)
    with allure.step("Проверка корректности аккаунта после аутентификации"):
        user_name = page.check_right_user()
        assert user_name is not None
    with allure.step("Вычисление числа фибоначчи и осуществление транзакций"):
        # Так как сайт не всегда выдавал один и тот же результат при определенных действиях,
        # для достоверности проверки были добавлены переключения с одного счета на другой, а также перезагрузка страницы
        amount = fib(DAY)
        page.deposit(amount)
        page.refresh()
        page.swap_accounts()
        page.withdrawal(amount)
        page.refresh()
        page.swap_accounts()
    with allure.step("Проверка итогового баланса"):
        balance = page.get_balance()
        assert int(balance.text) == 0


@allure.title("Тестирование наличия транзакций и формирование отчета")
@pytest.mark.parametrize("driver", ['chrome', 'firefox', 'edge'], indirect=True)
def test_transactions(driver):
    page = TransactionsPage(driver)
    with allure.step("Получение транзакций для отчета"):
        transactions = page.get_transactions()
    with allure.step("Проверка кол-ва транзакций"):
        assert len(transactions) == 2
    with allure.step("Формирование отчета"):
        page.create_csv_file(transactions)
