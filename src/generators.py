from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """
    Функция принимает список словарей и возвращает итератор,
    который выдает по очереди операции, в которых указана заданная валюта.
    :param transactions: List[dict]
    :param currency: str
    :return: Generator
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """
    Функция генератор, который принимает список словарей
    и возвращает описание каждой операции по очереди.
    :param transactions: List[dict]
    :return: Generator
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """
    Функция генератор номеров банковских карт, который должен генерировать номера карт
    в формате "XXXX XXXX XXXX XXXX", где X — цифра.
    (диапазоны передаются как параметры генератора).
    :param start: int
    :param end: int
    :return: Generator
    """
    for number in range(start, end + 1):
        card_number = str(number).zfill(16)
        format_card_number = ' '.join([card_number[index_j:index_j + 4] for index_j in range(0, len(card_number), 4)])
        yield format_card_number
