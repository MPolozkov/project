import unittest

from process_re import process_bank_operations


class TestProcessBankOperations(unittest.TestCase):

    def test_empty_description(self):
        """Функция проверяет поле пустое."""
        data = [{"description": ""}]
        categories = {}
        result = process_bank_operations(data, categories)
        self.assertEqual(result, categories)

    def test_category_found(self):
        """Функция проверяет случай, когда в описании есть слово из списка категорий."""
        data = [{"description": "Перевод организации"}]
        categories = ["Перевод организации"]
        result = process_bank_operations(data, categories)
        self.assertEqual(result, {"Перевод организации": 1})

    def test_category_not_found(self):
        """Проверяет случай, описании description нет"""
        data = []
        categories = []
        result = process_bank_operations(data, categories)
        self.assertEqual(result, {})




