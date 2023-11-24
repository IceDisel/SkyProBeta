import json

import pytest

from data.data_for_test import EXPECTED_RESULT, TRANSACTIONS_FOR_TEST_2
from src.utils import get_transaction_amount_rub, read_csv_xlsx_file, read_json_file


@pytest.fixture
def tmp_path() -> str:
    return 'tests/test.json'


@pytest.fixture()
def expected_result() -> list:
    return EXPECTED_RESULT


def test_read_json_file_valid_file(tmp_path: str) -> None:
    """
    Тест на чтение корректного JSON-файла
    :param tmp_path: путь к файлу
    :return: None
    """
    data = [{'имя': 'Джон', 'возраст': 30}, {'имя': 'Алиса', 'возраст': 25}]

    with open(tmp_path, 'w', encoding="utf-8") as file:
        json.dump(data, file)

    assert read_json_file(str(tmp_path)) == data


def test_read_json_file_empty_file(tmp_path: str) -> None:
    """
    Тест на чтение пустого JSON-файла
    :param tmp_path: путь к файлу
    :return: None
    """
    open(tmp_path, 'w', encoding="utf-8").close()
    assert read_json_file(tmp_path) == []


def test_read_json_file_nonexistent_file() -> None:
    """
    Тест на чтение несуществующего JSON-файла
    :return: None
    """
    file_path = 'nonexistent.json'
    assert read_json_file(file_path) == []


def test_read_json_file_invalid_data(tmp_path: str) -> None:
    """
    Тест на чтение JSON-файла с некорректными данными
    :param tmp_path: путь к файлу
    :return: None
    """
    data = {'имя': 'Джон', 'возраст': 30}

    with open(tmp_path, 'w', encoding="utf-8") as file:
        json.dump(data, file)

    assert read_json_file(tmp_path) == []


def test_read_json_file_invalid_encoding(tmp_path: str) -> None:
    """
    Тест на чтение JSON-файла с некорректной кодировкой
    :param tmp_path: путь к файлу
    :return: None
    """
    data = [{'имя': 'Джон', 'возраст': 30}, {'имя': 'Алиса', 'возраст': 25}]

    with open(tmp_path, 'w', encoding='utf-16') as file:
        json.dump(data, file)

    assert read_json_file(tmp_path) == []


def test_read_csv_file(expected_result: list) -> None:
    """
    Тест для файла CSV с правильными данными.
    :return: None
    """
    file_path = 'tests/test_data.csv'

    assert read_csv_xlsx_file(file_path) == expected_result


def test_read_xlsx_file(expected_result: list) -> None:
    """
    Тест для файла XLSX с правильными данными.
    :return: None
    """
    file_path = 'tests/test_data.xlsx'

    assert read_csv_xlsx_file(file_path) == expected_result


def test_read_unsupported_file_format() -> None:
    """
    Тест для файла с неподдерживаемым форматом
    :return: None
    """
    file_path = 'tests/test.json'

    assert read_csv_xlsx_file(file_path) == []


def test_read_file_with_invalid_data() -> None:
    """
    Тест для файла с неправильными данными.
    :return: None
    """
    file_path = 'tests/test_data_1.csv'

    assert read_csv_xlsx_file(file_path) == []


@pytest.mark.parametrize("transaction", TRANSACTIONS_FOR_TEST_2)
def test_get_transaction_amount_rub(transaction: dict) -> None:
    """
    Тест функции get_transaction_amount_rub
    :param transaction: dict вход транзакции
    :return: None
    """
    if transaction == TRANSACTIONS_FOR_TEST_2[0]:
        expected = 31957.58
        assert get_transaction_amount_rub(transaction) == expected
    else:
        with pytest.raises(ValueError):
            get_transaction_amount_rub(transaction)
