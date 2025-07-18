import json
import unittest

import utils
from process_re import process_bank_search, process_bank_operations


class TestProcessBankSearch(unittest.TestCase):
    """Тест создает список банковских операций,
    задает поисковый запрос и проверяет,
    что функция вернула список,
    содержащий одну запись,
    и что эта запись содержит ожидаемое описание """
    def test_search_found(self):
        data = [{
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
              "amount": "48223.05",
              "currency": {
                "name": "руб.",
                "code": "RUB"
              }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
          },
            {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
              "amount": "9824.07",
              "currency": {
                "name": "USD",
                "code": "USD"
              }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
          }]
        search_term = 'Перевод'
        result = process_bank_search(data, search_term)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['description'], 'Перевод организации')

    def test_search_not_found(self):
        """Тест проверяет, что функция process_bank_search
        возвращает пустой список,
        когда поисковый запрос не найден в данных."""
        data = [{
                "id": 587085106,
                "state": "EXECUTED",
                "date": "2018-03-23T10:45:06.972075",
                "operationAmount": {
                  "amount": "48223.05",
                  "currency": {
                    "name": "руб.",
                    "code": "RUB"
                  }
                },
                "description": "Перевод организации",
                "to": "Счет 41421565395219882431"
              },
                {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                  "amount": "9824.07",
                  "currency": {
                    "name": "USD",
                    "code": "USD"
                  }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
                }]
        search_term = 'открытие'
        result = process_bank_search(data, search_term)
        self.assertEqual(len(result), 0)

    def test_search_case_insensitive(self):
        """Тест проверяет, что поиск выполняется без учета регистра.
        Он ищет "ПЕРЕВОД" (в верхнем регистре) и убеждается,
        что находит запись, содержащую "Перевод организации"
        (в нижнем регистре)."""

        data = [{
                "id": 587085106,
                "state": "EXECUTED",
                "date": "2018-03-23T10:45:06.972075",
                "operationAmount": {
                  "amount": "48223.05",
                  "currency": {
                    "name": "руб.",
                    "code": "RUB"
                  }
                },
                "description": "Перевод организации",
                "to": "Счет 41421565395219882431"
              },
                {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                  "amount": "9824.07",
                  "currency": {
                    "name": "USD",
                    "code": "USD"
                  }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
                }]
        search_term = 'ПЕРЕВОД'
        result = process_bank_search(data, search_term)
        self.assertEqual(len(result), 2)

    def test_empty_data(self):
        """Тест проверяет, как функция process_bank_search ведет себя,
        когда ей передается пустой список данных.
        Он убеждается, что функция возвращает пустой список."""
        data = []
        search_term = 'перевод'
        result = process_bank_search(data, search_term)
        self.assertEqual(len(result), 0)

    def test_empty_search_term(self):
        """Ищем в строке, игнорируя регистр.
         Если нашли, добавляем словарь в результат"""
        data = [{
                "id": 587085106,
                "state": "EXECUTED",
                "date": "2018-03-23T10:45:06.972075",
                "operationAmount": {
                  "amount": "48223.05",
                  "currency": {
                    "name": "руб.",
                    "code": "RUB"
                  }
                },
                "description": "Перевод организации",
                "to": "Счет 41421565395219882431"
              },
                {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                  "amount": "9824.07",
                  "currency": {
                    "name": "USD",
                    "code": "USD"
                  }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
                }]
        search_term = ''
        result = process_bank_search(data, search_term)
        self.assertEqual(len(result), 2)


class TestProcessBankOperations(unittest.TestCase):

    def test_empty_data(self):
        """Тест для пустых входных данных."""
        categories = []
        result = process_bank_operations([], categories)
        self.assertEqual(result, {})

    def test_no_matching_categories(self):
        """Тест, когда ни одна категория не совпадает."""
        data = [{
                "id": 587085106,
                "state": "EXECUTED",
                "date": "2018-03-23T10:45:06.972075",
                "operationAmount": {
                  "amount": "48223.05",
                  "currency": {
                    "name": "руб.",
                    "code": "RUB"
                  }
                },
                "description": "Перевод организации",
                "to": "Счет 41421565395219882431"
              },
                {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                  "amount": "9824.07",
                  "currency": {
                    "name": "USD",
                    "code": "USD"
                  }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
                }]
        categories = ["приход", "расход"]
        result = process_bank_operations(data, categories)
        self.assertEqual(result, {"приход": 0, "расход": 0})

    def test_multiple_matches(self):
        """Тест для нескольких совпадений."""
        data = [{"description": "Покупка в магазине продуктов"}, {"description": "Обед в кафе"}]
        categories = ["магазин", "кафе"]
        result = process_bank_operations(data, categories)
        self.assertEqual(result, {"магазин": 1, "кафе": 1})

    def test_case_insensitive(self):
        """Тест на нечувствительность к регистру."""
        data = [{
                "id": 587085106,
                "state": "EXECUTED",
                "date": "2018-03-23T10:45:06.972075",
                "operationAmount": {
                  "amount": "48223.05",
                  "currency": {
                    "name": "руб.",
                    "code": "RUB"
                  }
                },
                "description": "ПеРеВод орГаниЗации",
                "to": "Счет 41421565395219882431"
              },
                {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                  "amount": "9824.07",
                  "currency": {
                    "name": "USD",
                    "code": "USD"
                  }
                },
                "description": "ПеРеВод оргАниЗаЦии",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
                }]
        categories = ["перевод"]
        result = process_bank_operations(data, categories)
        self.assertEqual(result, {"перевод": 2})
