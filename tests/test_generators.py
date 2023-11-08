import pytest

from data.data_for_test import TRANSACTIONS_FOR_TEST, TRANSACTIONS_FOR_TEST_1
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions() -> list[dict]:
    """
    Фикстура для предоставления списка словарей transactions
    :return: list[dict]:
    """
    return TRANSACTIONS_FOR_TEST


@pytest.mark.parametrize("currency, expected", TRANSACTIONS_FOR_TEST_1)
def test_filter_by_currency(transactions: list[dict], currency: str, expected: list[dict]) -> None:
    """
    Тест для функции filter_by_currency
    :param transactions: list[dict]
    :param currency: str
    :param expected: list[dict]
    :return: None
    """
    assert list(filter_by_currency(transactions, currency)) == expected


def test_transaction_descriptions(transactions: list[dict]) -> None:
    """
    Тест для функции transaction_descriptions
    :param transactions: list[dict]
    :return: None
    """
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]
    assert list(transaction_descriptions(transactions)) == expected


@pytest.mark.parametrize("start, end, expected", [
    (1, 5, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]),
    (10, 12, [
        "0000 0000 0000 0010",
        "0000 0000 0000 0011",
        "0000 0000 0000 0012",
    ]),
])
def test_card_number_generator(start: int, end: int, expected: list[str]) -> None:
    """
    Тест для функции card_number_generator
    :param start: int
    :param end: int
    :param expected:
    :return: list[str]
    """
    assert list(card_number_generator(start, end)) == expected
