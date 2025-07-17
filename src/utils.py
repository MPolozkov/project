import json
import os
from typing import List, Dict

from external_api import conversions

import logging

log_dir = '../log'
log_file = os.path.join(log_dir, 'utils.log')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file, "w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.ERROR)
logger.setLevel(logging.WARNING)
logger.setLevel(logging.INFO)


def json_get(file_patch: str) -> List[Dict]:
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info('Открываем файл для чтения')
        with open(file_patch, 'r', encoding='utf-8') as file:
            transaction = json.load(file)

        logger.info('Передаем список')
        if isinstance(transaction, list):
            return transaction
        else:
            logger.error('Ошибка: Данные в файле не являются списком.')
            return []

    except FileNotFoundError:
        logger.error('Ошибка: Файл "data/operations.json" не найден.')
    except json.JSONDecodeError:
        logger.error('Ошибка: Некорректный формат JSON  файле "data/operations.json"".')
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    get = json_get("../data/operations.json")
    print(get)


def transaction_sum(transaction: list) -> float:
    """Функция возвращает сумму в рублях, если транзакция приходит
        в другой валюте то функция конвертирует в рубли"""
    for x in transaction:
        if x:
            logger.info('Получаем данные по операции')
            operation_amount = x["operationAmount"]["currency"]["code"]
            summ = x["operationAmount"]["amount"]
            logger.info('Получаем значение с двумя цифрами после точки')
            summ_tu = float(summ)
            if operation_amount == "RUB":
                logger.info('Выводим сумму если транзакция в рублях')
                return summ_tu
            elif operation_amount == "USD":
                logger.info('Если транзакция в долларах')
                exchange_rate = conversions("USD", "RUB")
                logger.info('Получаем рубли из долларов')
                total_sum_rub = summ_tu * exchange_rate
                return round(total_sum_rub, 2)
            elif operation_amount == "EUR":
                exchange_rate = conversions("EUR", "RUB")
                logger.info('Получаем рубли из евро')
                total_sum_rub = summ_tu * exchange_rate
                return round(total_sum_rub, 2)


transact = [
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        }
    }
]


# if __name__ == "__main__":
# summa_transaction = transaction_sum(transact)
# print(summa_transaction)
