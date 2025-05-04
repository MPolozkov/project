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
        card_number = name_card[number_start : number_end + 1]

        # Убедимся, что длина подходящая
        if len(card_number) == 15:
            card_name = name_card[:number_start].strip()  # Имя - всё до цифр

            # 2. ПРОВЕРКА ФОРМАТА ИМЕНИ: Строго буквы, пробелы и дефисы
            allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -_"
            if all(char in allowed_chars for char in card_name):

                try:  # Попытка замаскировать номер
                    masked_number = get_mask_card_number(card_number)
                    return f"{card_name}: {masked_number}" if card_name else masked_number
                except ValueError:  # Не удалось замаскировать, значит формат номера неверен
                    return "Некорректный формат номера карты"

            else:
                return "Некорректный формат имени карты"
    # Если не нашли цифры, то пробуем счет
    digits_only = True
    for char in name_card:
        if not char.isdigit():
            digits_only = False
            break
    if digits_only:
        try:
            masked_account = get_mask_account(name_card)
            return f"Счет: {masked_account}"
        except ValueError:
            return "Некорректный формат номера счета"

    letters_only = True
    for char in name_card:
        if not char.isalpha() and char != " ":
            letters_only = False
            break
    if letters_only:
        return "Номер карты или номер счета не найден"  # Не нашли

    return "Некорректный ввод"


# if __name__ == '__main__':

# name_card = str(input())
# print(mask_account_card(name_card))


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
