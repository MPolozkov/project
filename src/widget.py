from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(name_card: str) -> str:
    """Маскирует номер карты или номер счета в строке."""
    name_card = name_card.strip()  # Удаляем пробелы в начале и конце
    if not name_card:
        return "Поле для ввода пустое"

    # 1. Ищем номер карты (13-19 цифр) в строке
    number_start = -1
    number_end = -1
    for i, char in enumerate(name_card):
        if char.isdigit():
            if number_start == -1:
                number_start = i
            number_end = i

    if number_start != -1:  # Если цифры найдены, пытаемся выделить карту
        card_number = name_card[number_start: number_end + 1]

        # Убедимся, что длина подходящая
        if len(card_number) >= 16:
            card_name = name_card[:number_start].strip()  # Имя - всё до цифр

            # 2. ПРОВЕРКА ФОРМАТА ИМЕНИ: Строго буквы, пробелы и дефисы
            # if all(char in allowed_chars for char in card_name):
            try:  # Попытка замаскировать номер
                if len(card_number) == 16:  # Предполагаем, что это карта
                    masked_number = get_mask_card_number(card_number)
                    return f"{card_name}: {masked_number}" if card_name else masked_number
                elif len(card_number) > 19:
                    masked_sort = get_mask_account(card_number)
                    return f"{card_name}: {masked_sort}" if card_name else masked_sort
            except ValueError:
                return "Некорректный формат номера"

        # Если строка состоит только из букв, сообщаем, что ничего не найдено.
        if all(char.isalpha() or char.isspace() for char in name_card):
            return "Номер карты или номер счета не найден"

    return "Некорректный ввод"


if __name__ == '__main__':
    name_card = str(input())
    print(mask_account_card(name_card))


def get_date(date_string: str) -> str:
    """Преобразует строку с датой в формате "2024-03-11T02:26:18.671407" в формат "ДД.ММ.ГГГГ"."""

    # проверка на пустоту
    if not date_string:
        return "Введите дату"

    try:
        # Преобразуем строку в объект datetime
        date_object = datetime.fromisoformat(date_string)

        # Форматируем объект datetime в нужный формат
        formatted_date = date_object.strftime("%d.%m.%Y")

        return formatted_date
    except ValueError:
        # Обрабатываем ошибки, если входная строка не соответствует ожидаемому формату
        return "Неверный формат даты"


# if __name__ == "__main__":
    # date_string = str(input())
    # print(get_date(date_string))
