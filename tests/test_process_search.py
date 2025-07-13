import unittest

from process_re import process_bank_search


class TestProcessBankSearch(unittest.TestCase):

    def test_empty_data(self):
        """Проверяет, что функция возвращает пустой список,
        если ей передать пустой список данных"""
        self.assertEqual(process_bank_search([], "test"), [])

    def test_search_found(self):
        """Функция находит одну запись, когда в поисковой строке присутствует
        описание одной из транзакций."""
        data = [{"description": "test transaction", "amount": 100}, {"description": "another", "amount": 200}]
        result = process_bank_search(data, "test")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["description"], "test transaction")

    def test_search_not_found(self):
        """Функция возвращает пустой список,
        если поисковая строка не найдена ни в одной из транзакций"""
        data = [{"description": "test transaction", "amount": 100}, {"description": "another", "amount": 200}]
        result = process_bank_search(data, "nonexistent")
        self.assertEqual(len(result), 0)

    def test_case_insensitive(self):
        """Функция проверяет, что поиск нечувствителен к регистру символов."""
        data = [{"description": "Test Transaction", "amount": 100}]
        result = process_bank_search(data, "test")
        self.assertEqual(len(result), 1)

    def test_multiple_matches(self):
        """Функция проверяет, что находит все записи,
        соответствующие поисковой строке, если их несколько"""
        data = [{"description": "test transaction", "amount": 100}, {"description": "another test", "amount": 200}]
        result = process_bank_search(data, "test")
        self.assertEqual(len(result), 2)