import os

import logging

log_dir = '../log'
log_file = os.path.join(log_dir, 'masks.log')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file, "w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.ERROR)
logger.setLevel(logging.INFO)


def get_mask_card_number(card_number: str) -> str:
    """Функция для шифрования номера карты"""
    card_number_str = str(card_number)

    if card_number_str == "":
        logger.error('Поле для ввода пустое')
        return "Поле для ввода пустое"
    elif card_number_str.isalpha():
        logger.error('Номер карты должен состоять только из цифр')
        return "Номер карты должен состоять только из цифр"
    elif len(card_number_str) > 16:
        logger.error('Номер карты не должен быть больше 16 цифр')
        return "Номер карты не должен быть больше 16 цифр"

    logger.info('Получаем первые 6 цифр')
    first_six = card_number_str[:6]

    logger.info('Получаем последние 4 цифры')
    last_four = card_number_str[-4:]

    logger.info('Вычисляем количество символов для маскировки')
    masked_length = len(card_number_str) - 6 - 4

    logger.info('Создаем строку маскировки')
    masked_part = "*" * masked_length

    logger.info('Собираем маскированный номер')
    masked_number = first_six + masked_part + last_four

    logger.info('Форматируем по блокам по 4 цифры')
    formatted_number = " ".join([masked_number[i: i + 4] for i in range(0, len(masked_number), 4)])

    return formatted_number


if __name__ == '__main__':
    card = str(input())
    print(get_mask_card_number(card))


def get_mask_account(account_number: str) -> str:
    """Функция для шифрования номера счета"""
    account_number_str = str(account_number)

    if account_number_str == "":
        logger.error('Поле для ввода пустое')
        return "Поле для ввода пустое"
    elif account_number_str.isalpha():
        logger.error('Номер счета должен состоять только из цифр')
        return "Номер счета должен состоять только из цифр"
    elif len(account_number_str) < 19:
        logger.error('Номер счета должен быть больше 19 цифр')
        return "Номер счета должен быть больше 19 цифр"

    logger.info('Получаем последние 4 цифры')
    first_six = account_number_str[-4:]

    logger.info('Создаем строку маскировки')
    masked_part = "**"

    logger.info('Собираем маскированный номер')
    masked_number = masked_part + first_six

    return masked_number


# if __name__ == '__main__':
    # number = str(input())
    # print(get_mask_account(number))
