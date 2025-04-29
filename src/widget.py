from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(name_card: str) -> str:
    """Является ли входная строка номером карты или номером счета"""
    # Разделяем строку на слова
    words = name_card.split()
    card_number = ""
    card_name = ""

    # Ищем номер карты
    for word in words:
        if word.isdigit():
            card_number = word
            break  # Нашли номер, выходим из цикла

    if card_number and len(card_number) == 16:
        try:
            masked_number = get_mask_card_number(card_number)

            # Определяем имя карты (все слова до номера карты)
            card_name = " ".join(words[:words.index(card_number)])

            return f"{card_name}: {masked_number}" if card_name else masked_number

        except ValueError:
            return name_card

    elif len(str(card_number)) > 16:
        try:
            # Если в строке нет номера карты, пробуем обработать как номер счета
            masked_number = get_mask_account(card_number)
            return f"Счет: {masked_number}"
        except ValueError:
            # Если и это не получилось, возвращаем исходную строку
            return f"{name_card}, Если и это не получилось, возвращаем исходную строку"
    else:
        return "Номером карты и неомером счета должен состоять только из цифр"


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
