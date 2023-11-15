import json


def read_json_file(path: str) -> list[dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список.
    :param path: Путь до файла
    :return: Вывод списка словарей данных
    """
    try:
        with open(path, encoding="utf-8") as file_json:
            data = json.load(file_json)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, UnicodeError, json.JSONDecodeError):
        return []


def get_transaction_amount_rub(transaction: dict) -> float:
    """
    Функция, которая принимает на вход одну транзакцию
    :param transaction: dict вход транзакции
    :return: float сумму транзакции (amount) в рублях
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях.")
