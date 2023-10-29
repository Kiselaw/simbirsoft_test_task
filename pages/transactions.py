import csv

import allure

from helpers import time_converter

from .base import BasePage


class TransactionsPageLocators:
    """Класс для хранения XPATH."""
    TRANSACTIONS_BUTTON = "//button[contains(text(), 'Transactions')]"
    TRANSACTIONS = "//tr[contains(@ng-repeat, 'transactions')]"
    TRANSACTION_COLUMNS = "//td"


class TransactionsPage(BasePage):
    """Класс для методов страницы транзакций."""
    def get_transactions(self):
        transactions_button = self.get_element(TransactionsPageLocators.TRANSACTIONS_BUTTON)
        self.click(transactions_button)
        transactions = self.get_elements(TransactionsPageLocators.TRANSACTIONS)
        return transactions

    def create_csv_file(self, transactions):
        csv_file_path = './transactions.csv'
        with open(csv_file_path, 'w', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Дата-время Транзакции", "Сумма", "Тип Транзакции"])
            for transaction in transactions:
                split_text = transaction.text.split()
                columns = [" ".join(split_text[:5]), split_text[5], split_text[6]]
                writer.writerow([f"{time_converter(columns[0])}", f"{columns[1]}", f"{columns[2]}"])
        allure.attach.file(csv_file_path, name='CSV Transactions Report', attachment_type=allure.attachment_type.CSV)
