from typing import Iterator, Iterable


def filter_by_currency(transact: list, currency: str) -> Iterator:
    for x in transact:
        if x["operationAmount"]["currency"]["code"] == currency:
            yield x


transactions = [
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
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]

usd_transactions = filter_by_currency(transactions, "USD")

for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transact: list) -> Iterator:
    for i in transact:
        yield i["description"]


# description = transaction_descriptions(transactions)
# for _ in range(5):
    # print(next(description))


def card_number_generator(start: int, end: int) -> Iterator:
    for number in range(start, end + 1):
        card_number = str(number).zfill(16)
        formatted_number = " ".join([card_number[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_number


generator = card_number_generator(1, 5)
for card in generator:
    print(card)
