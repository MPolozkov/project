import unittest
from unittest.mock import patch

from utils import transaction_sum


class TestTransactionSum(unittest.TestCase):

    @patch('utils.conversions')
    def test_transaction_sum_rub(self, mock_conversions):
        """Тест проверяет, что если транзакция в рублях (RUB), то возвращается сумма без конвертации."""
        transaction = [{"operationAmount": {"currency": {"code": "RUB"}, "amount": "100.00"}}]
        self.assertEqual(transaction_sum(transaction), 100.00)
        self.assertFalse(mock_conversions.called)

    @patch('utils.conversions')
    def test_transaction_sum_usd(self, mock_conversions):
        """Тест проверяет корректную конвертацию суммы из (USD) в (RUB)"""
        mock_conversions.return_value = 75.0
        transaction = [{"operationAmount": {"currency": {"code": "USD"}, "amount": "1.00"}}]
        self.assertEqual(transaction_sum(transaction), 75.0)
        mock_conversions.assert_called_once_with("USD", "RUB")

    @patch('utils.conversions')
    def test_transaction_sum_eur(self, mock_conversions):
        """Тест проверяет корректную конвертацию суммы из (EUR) в (RUB)"""
        mock_conversions.return_value = 85.0
        transaction = [{"operationAmount": {"currency": {"code": "EUR"}, "amount": "1.00"}}]
        self.assertEqual(transaction_sum(transaction), 85.0)
        mock_conversions.assert_called_once_with("EUR", "RUB")

    def test_empty_transaction(self):
        transaction = []
        result = transaction_sum(transaction)
        self.assertIsNone(result)

    def test_none_transaction(self):
        transaction = [None]
        result = transaction_sum(transaction)
        self.assertIsNone(result)
