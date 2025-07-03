import json
from typing import List, Dict

from pytonpoject.external_api import conversions


def json_get(file_patch: str) -> List[Dict]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:

        with open(file_patch, 'r', encoding='utf-8') as file:
            transaction = json.load(file)

        if isinstance(transaction, list):
            return transaction
        else:
            print("Ошибка: Данные в файле не являются списком.")
            return []

    except FileNotFoundError:
        print("Ошибка: Файл 'data/operations.json' не найден.")
    except json.JSONDecodeError:
        print("Ошибка: Некорректный формат JSON  файле 'data/operations.json'.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# if __name__ == "__main__":
    # get = json_get("../data/operations.json")
    # print(get)


def transaction_sum(transaction: list) -> float:
    """Функция возвращает сумму в рублях если транзакция приходит в другой валюте то функция конвертирует в рубли"""
    for x in transaction:
        if x:
            operation_amount = x["operationAmount"]["currency"]["code"]
            summ = x["operationAmount"]["amount"]
            summ_tu = float(summ)
            if operation_amount == "RUB":
                return summ_tu
            elif operation_amount == "USD":
                exchange_rate = conversions("USD", "RUB")
                total_sum_rub = summ_tu * exchange_rate
                return round(total_sum_rub, 2)
            elif operation_amount == "EUR":
                exchange_rate = conversions("EUR", "RUB")
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

if __name__ == "__main__":
    summa_transaction = transaction_sum(transact)
    print(summa_transaction)



