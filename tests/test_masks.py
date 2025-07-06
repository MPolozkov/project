import pytest

from masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (123456789012346, "1234 56** ***2 346"),
        (648464846343648, "6484 64** ***3 648"),
        (7463967485374, "7463 96** *537 4"),
        ("аппрвалв", "Номер карты должен состоять только из цифр"),
        ("", "Поле для ввода пустое"),
        (12345678901234565635364846484634, "Номер карты не должен быть больше 15 цифр"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    result = get_mask_card_number(card_number)
    assert result == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        (123456789012345648464846343648, "**3648"),
        (648464846343648123456789012345, "**2345"),
        (746396748537412345678901234501, "**4501"),
        ("аппрвалв", "Номер счета должен состоять только из цифр"),
        ("", "Поле для ввода пустое"),
        (1234567890578, "Номер счета должен быть больше 19 цифр"),
    ],
)
def test_get_mask_account(account_number, expected):
    result = get_mask_account(account_number)
    assert result == expected
