import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция, которая будет принимать список словарей
     с данными о банковских операциях и строку поиска"""
    result = []
    for d in data:
        data_string = ' '.join(str(value) for value in d.values())
        if re.search(search, data_string, re.IGNORECASE):
            result.append(d)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция которая, принимает список словарей с данными о
        банковских операциях, списка категорий операций,
        а возвращать словарь"""
    category_counts = {}

    for category in categories:
        category_counts[category] = 0

    for d in data:
        descriptions = d.get("description")
        if descriptions:
            for category in categories:
                if re.search(category, descriptions, re.IGNORECASE):
                    category_counts[category] += 1
                    break
    return category_counts

transact = [
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
    },
]


if __name__ == "__main__":
    categories = ["Перевод организации"]
    summa_transaction = process_bank_operations(transact, categories)
    print(summa_transaction)
