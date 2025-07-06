import unittest
from unittest.mock import patch

import pandas as pd

from reader_xlsx import reader_xlsx


class TestReaderXlsx(unittest.TestCase):

    @patch('pandas.read_excel')
    def test_reader_xlsx_success(self, mock_read_excel):
        """Тест проверяет успешное чтение transactions_excel.xlsx."""
        reader_xlsx("transactions_excel.xlsx")

    @patch('pandas.read_excel', side_effect=FileNotFoundError)
    def test_reader_xlsx_file_not_found(self, mock_read_excel):
        """Файл 'transactions_excel.xlsx' не найден."""
        result = reader_xlsx("transactions_excel.xlsx")
        self.assertEqual(result, [])

    @patch('pandas.read_excel', side_effect=ImportError)
    def test_reader_xlsx_import_error(self, mock_read_excel):
        """Произошла ошибка при чтении файла"""
        result = reader_xlsx("transactions_excel.xlsx")
        self.assertEqual(result, [])

    @patch('pandas.read_excel', side_effect=Exception("Some error"))
    def test_reader_xlsx_general_error(self, mock_read_excel):
        """Ошибка: Библиотека 'openpyxl' не установлена. Пожалуйста, установите ее."""
        result = reader_xlsx("transactions_excel.xlsx")
        self.assertEqual(result, [])
