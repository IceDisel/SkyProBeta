import re
from collections import Counter


def search_operations(data: list[dict], search_string: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска.
    :param data: Данные о банковских операциях.
    :param search_string: Строка поиска.
    :return: Возвращает список словарей, у которых в описании есть данная строка.
    """
    pattern = re.compile(search_string, re.IGNORECASE)

    return [item for item in data if pattern.search(item['description'])]


def count_operations_by_category(data: list[dict], categories: dict) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и словарь категорий операций.
    :param data: Данные о банковских операциях.
    :param categories: Словарь категорий операций.
    :return: Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    counter = Counter(item['description'] for item in data)
    categories.update(counter)

    return categories
