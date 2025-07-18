import pytest

from widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "name_card, expected",
    [
        ("Visa Classic 6831982476737658", "Visa Classic: 6831 98** **** 7658"),
        ("6831982476737658385723", "**5723"),
        ("аппрвалв", "Некорректный ввод"),
        ("аппрвалв 683198247673765", "Некорректный ввод"),
        (" ", "Поле для ввода пустое"),
    ],
)
def test_mask_account_card(name_card, expected):
    result = mask_account_card(name_card)
    assert result == expected


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T10:30:00.000000", "31.12.2023"),
        ("2024-03-11", "11.03.2024"),
        ("invalid_date", "Неверный формат даты"),
        ("", "Введите дату"),
    ],
)
def test_mask_get_date(date_string, expected):
    result = get_date(date_string)
    assert result == expected
