import json
import logging

logger = logging.getLogger(__name__)


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
                logger.info("JSON-файл успешно прочитан")
                return data
            else:
                logger.warning("JSON-файл не содержит список данных")
                return []
    except (FileNotFoundError, UnicodeError, json.JSONDecodeError):
        logger.exception("Произошла ошибка при чтении JSON-файла")
        return []


def get_transaction_amount_rub(transaction: dict) -> float:
    """
    Функция, которая принимает на вход одну транзакцию
    :param transaction: dict вход транзакции
    :return: float сумму транзакции (amount) в рублях
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        logger.info("Транзакция выполнена в рублях")
        return float(transaction["operationAmount"]["amount"])
    else:
        logger.error("Транзакция выполнена не в рублях")
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях.")
