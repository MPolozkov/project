import unittest
from unittest.mock import patch, mock_open

from reader_csv import reade_csv


class TestReadCsv(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="header1,header2\nvalue1,value2")
    def test_read_csv_success(self, mock_file):
        """Тест проверяет успешное чтение CSV файла."""
        file_path = "fake_file.csv"
        result = reade_csv(file_path)
        self.assertEqual(result, [{"header1": "value1", "header2": "value2"}])
        mock_file.assert_called_with(file_path, "r", encoding="UTF-8")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_csv_file_not_found(self, mock_file):
        """Тест проверяет обработку исключения FileNotFoundError."""
        file_path = "non_existent_file.csv"
        with self.assertRaises(FileNotFoundError):
            reade_csv(file_path)
        mock_file.assert_called_with(file_path, "r", encoding="UTF-8")