import pytest

from src.widget import convert_date, get_mask_bankcard_account


# Тесты для функции get_mask_bankcard_account
@pytest.mark.parametrize("number_name, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Maestro 15968378687051995", "Maestro Не верный номер карты"),
    ("Счет 73654108430135874305", "Счет **4305")
])
def test_get_mask_bankcard_account(number_name: str, expected: str) -> None:
    assert get_mask_bankcard_account(number_name) == expected


# Тесты для функции convert_date
def test_convert_date() -> None:
    result = convert_date("2018-07-11T02:26:18.671407")
    assert result == "11.07.2018"
