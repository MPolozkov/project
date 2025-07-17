from typing import Any, Dict, List

import csv


def reade_csv(file_read: str) -> List[Dict[str, Any]]:
    transactions: List = []
    with open(file_read, "r", encoding="UTF-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            transactions.append(row)
        return transactions


# print(reade_csv('../data/transactions.csv'))
