import os
import unittest
from unittest.mock import patch
from pytonpoject.external_api import conversions
from dotenv import load_dotenv
import requests

load_dotenv()
token = os.getenv('API_KEY')


class TestConversions(unittest.TestCase):

    @patch('requests.request')
    def test_external(self, mock_request):
        """Тест успешное подключение к API"""
        mock_request.return_value.json.return_value = {'rates': {'USD': 1.23}}
        mock_request.return_value.raise_for_status.return_value = 200
        result = conversions(symbols='USD', base='RUB', token=token)
        self.assertEqual(result, 1.23)

    @patch('requests.request')
    def test_conversions_failure(self, mock_request):
        """Тест, ошибочные данные"""
        mock_request.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("Ошибка")
        with self.assertRaises(requests.exceptions.HTTPError):
            conversions(symbols='USD', base='EUR', token='test_token')
