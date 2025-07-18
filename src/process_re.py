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
    if not isinstance(categories, list):
        return {}

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


