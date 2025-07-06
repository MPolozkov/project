import generators
from typing import Iterator, List, Dict


def test_filter_by_currency():
    """Проверяет, что функция возвращает пустой список, если на вход подан пустой список транзакций"""
    assert list(generators.filter_by_currency([], "USD")) == []


def tes_filter_by_match():
    """Проверяет, что функция возвращает исходный список, если в нем есть транзакции с указанной валютой"""
    transactions = [{"operationAmount": {"currency": {"code": "USD"}}}]
    assert list(generators.filter_by_currency(transactions, "USD")) == transactions


def test_filter_no_match():
    """Проверяет, что функция возвращает пустой список, если в списке транзакций нет транзакций с указанной валютой"""
    transactions = [{"operationAmount": {"currency": {"code": "EUR"}}}]
    assert list(generators.filter_by_currency(transactions, "USD")) == []


def test_filter_mixed_currencies():
    """Проверяет, что функция правильно фильтрует список транзакций, когда в нем есть транзакции с разными валютами"""
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}},
        {"operationAmount": {"currency": {"code": "USD"}}},
    ]
    result = list(generators.filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert result[0] == transactions[0]
    assert result[1] == transactions[2]


def test_filter_multiple_currencies():
    """Проверяет, что функция правильно фильтрует список транзакций, когда есть несколько разных валют и
    мы ищем конкретную."""
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}},
        {"operationAmount": {"currency": {"code": "RUB"}}},
    ]
    assert list(generators.filter_by_currency(transactions, "EUR")) == [transactions[1]]


def test_empty_list():
    """ Проверяет, что функция возвращает пустой список, если на вход передан пустой список транзакций"""
    transactions: List[Dict] = []
    result: Iterator[str] = generators.transaction_descriptions(transactions)
    assert list(result) == []


def test_single_transaction():
    """ Проверяет, что функция возвращает список, содержащий описание одной транзакции,
    если на вход передан список с одной транзакцией"""
    transactions: List[Dict] = [{"description": "Grocery shopping"}]
    result: Iterator[str] = generators.transaction_descriptions(transactions)
    assert (list(result) == ["Grocery shopping"])


def test_multiple_transactions():
    """Проверяет, что функция возвращает список, содержащий описания всех транзакций,
    если на вход передан список с несколькими транзакциями."""
    transactions: List[Dict] = [
        {"description": "Rent payment"},
        {"description": "Online purchase"},
        {"description": "Restaurant dinner"}
    ]
    result: Iterator[str] = generators.transaction_descriptions(transactions)
    assert (list(result) == ["Rent payment", "Online purchase", "Restaurant dinner"])


def test_card_number_generator_basic():
    """ правильно генерирует последовательность номеров карт для простых чисел"""
    generator = generators.card_number_generator(1, 3)
    result = list(generator)
    assert result == ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]


def test_card_number_generator_start_equals_end():
    """Проверяет случай, когда начальное и конечное значения равны. Должен быть сгенерирован только один номер карты"""
    generator = generators.card_number_generator(10, 10)
    result = list(generator)
    assert result == ["0000 0000 0000 0010"]


def test_card_number_generator_end_close_to_16_digits():
    """Проверяет генерацию номеров карт, когда конечное значение близко к максимальному 16-значному числу"""
    generator = generators.card_number_generator(9999999999999995, 10000000000000000)
    result = list(generator)
    assert result == ['9999 9999 9999 9995', '9999 9999 9999 9996', '9999 9999 9999 9997', '9999 9999 9999 9998', '9999 9999 9999 9999', '1000 0000 0000 0000']
