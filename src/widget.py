from masks import get_mask_card_number
from masks import get_mask_account

from typing import Union

# Словарь с префиксами карт и их названиями
CARD_PREFIXES = {
    "4": "Visa",
    "51": "Mastercard",
    "52": "Mastercard",
    "53": "Mastercard",
    "54": "Mastercard",
    "55": "Mastercard",
    "34": "American Express",
    "37": "American Express",
    "6011": "Discover",
    "65": "Discover",
    "35": "JCB",
    "220": "МИР"
}


def mask_account_card(name_card: Union[str, int]) -> str:
    try:
        # Пробуем обработать как номер карты
        masked_number = get_mask_card_number(name_card)
        card_type = "Неизвестно"

        # Определяем тип карты по префиксу
        for prefix, name in CARD_PREFIXES.items():
            if name_card.startswith(prefix):
                card_type = name
                break

        if card_type != "Неизвестно":
            return f"{card_type}: {masked_number}"
        else:
            return f"Номер карты (тип не определен): {masked_number}"

    except ValueError:
        try:
            # Если не получилось, пробуем обработать как номер счета
            masked_number = get_mask_account(name_card)
            return f"Номер счета: {masked_number}"
        except ValueError:
            # Если и это не получилось, значит, это не номер карты и не номер счета
            return name_card  # Или можно выбросить исключение


