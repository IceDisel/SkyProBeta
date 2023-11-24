import json
import logging
from datetime import datetime

import pandas as pd

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


def read_csv_xlsx_file(path: str) -> list[dict]:
    """
    Функция, которая принимает на вход путь до CSV или XLSX-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список.
    :param path:
    :return:
    """
    transactions_dict = []
    if path.endswith('.csv'):
        data = pd.read_csv(path, delimiter=';')
    elif path.endswith('.xlsx'):
        data = pd.read_excel(path)
    else:
        return []

    for _, row in data.iterrows():
        if ('id' in row and 'state' in row and 'date' in row and 'amount' in row and 'currency_name' in row
                and 'currency_code' in row and 'description' in row and 'from' in row and 'to' in row):
            try:
                transaction = {
                    "id": int(row["id"]),
                    'state': row['state'],
                    'date': datetime.strptime(row['date'][:-1], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S.%f"),
                    'operationAmount': {
                        'amount': '{:.2f}'.format(float(row['amount'])),
                        'currency': {
                            'name': row['currency_name'],
                            'code': row['currency_code']
                        }
                    },
                    'description': row['description'],
                    'from': row['from'],
                    'to': row['to']
                }
                transactions_dict.append(transaction)
            except ValueError:
                pass

    return transactions_dict


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
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях.")
