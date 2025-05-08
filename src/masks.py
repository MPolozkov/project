from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция для шифрования номера карты"""
    card_number_str = str(card_number)

    if card_number_str == " ":
        return "Поле для ввода пустое"
    elif card_number_str.isalpha():
        return "Номер карты должен состоять только из цифр"
    elif len(card_number_str) > 15:
        return "Номер карты не должен быть больше 15 цифр"

    # Получаем первые 6 цифр
    first_six = card_number_str[:6]
    # Получаем последние 4 цифры
    last_four = card_number_str[-4:]
    # Вычисляем количество символов для маскировки
    masked_length = len(card_number_str) - 6 - 4
    # Создаем строку маскировки
    masked_part = "*" * masked_length
    # Собираем маскированный номер
    masked_number = first_six + masked_part + last_four
    # Форматируем по блокам по 4 цифры
    formatted_number = " ".join([masked_number[i : i + 4] for i in range(0, len(masked_number), 4)])

    return formatted_number


# if __name__ == '__main__':

# card_number = str(input())
# print(get_mask_card_number(card_number))


def get_mask_account(account_number: Union[int, str]) -> str:
    """функция для шифрования номера счета"""
    account_number_str = str(account_number)  # Преобразуем в строку

    if account_number_str == " ":
        return "Поле для ввода пустое"
    elif account_number_str.isalpha():
        return "Номер счета должен состоять только из цифр"
    elif len(account_number_str) < 19:
        return "Номер счета должен быть больше 19 цифр"

    # Получаем последние 4 цифры
    first_six = account_number_str[-4:]
    # Создаем строку маскировки
    masked_part = "**"
    # Собираем маскированный номер
    masked_number = masked_part + first_six

    return masked_number


# if __name__ == '__main__':

# account_number = str(input())
# print(get_mask_account(account_number))