from datetime import datetime
from typing import Union

from masks import get_mask_account, get_mask_card_number

# Словарь с префиксами карт и их названиями
CARD_PREFIXES = {
    "7": "Visa",
    "71": "Mastercard",
    "37": "American Express",
    "65": "Discover",
    "35": "JCB",
    "220": "МИР"
}

# Словарь для определения ТИПА
CARD_TYPES = {
    "98": "Classic",   # Visa Classic
    "41": "Gold",      # Visa Gold
    "92": "Platinum",  # Mastercard Standard
}


def mask_account_card(name_card: Union[str, int]) -> str:
    """Является ли входная строка номером карты или номером счета"""
    name_card_str = str(name_card)  # Преобразуем в строку в самом начале

    try:
        # Пробуем обработать как номер карты
        masked_number = get_mask_card_number(name_card_str)
        card_brand = "Неизвестно"
        card_type = "Неизвестно"  # Уровень карты

        # Определяем бренд карты по префиксу
        for prefix, brand in CARD_PREFIXES.items():
            if name_card_str.startswith(prefix):
                card_brand = brand
                break

        # Определяем тип карты (уровень) по BIN
        bin_number = name_card_str[4:6]
        if bin_number in CARD_TYPES:
            card_type = CARD_TYPES[bin_number]

        if card_brand != "Неизвестно" and card_brand == 13:
            return f"{card_brand} {card_type}: {masked_number}"
        else:
            masked_number = get_mask_account(name_card_str)
            return f"Номер счета: {masked_number}"

    except ValueError:
        # Если и это не получилось, значит, это не номер карты и не номер счета
        return name_card_str  # Или можно выбросить исключение


if __name__ == '__main__':

    name_card = str(input())
    print(mask_account_card(name_card))


def get_date(date_string: str) -> str:
    """Преобразует строку с датой в формате "2024-03-11T02:26:18.671407" в формат "ДД.ММ.ГГГГ"."""
    try:
        # Преобразуем строку в объект datetime
        date_object = datetime.fromisoformat(date_string)

        # Форматируем объект datetime в нужный формат
        formatted_date = date_object.strftime("%d.%m.%Y")

        return formatted_date
    except ValueError:
        # Обрабатываем ошибки, если входная строка не соответствует ожидаемому формату
        return "Неверный формат даты"


if __name__ == '__main__':
    date_string = str(input())
    print(get_date(date_string))
