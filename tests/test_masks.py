import pytest

from src.masks import get_mask_the_bankcard, get_mask_the_bank_account


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("7000 7922 8960 6361", "7000 79** **** 6361"),
    ("7000 7922 8960 6361 5", "Не верный номер карты"),
    ("70007922896063615", "Не верный номер карты")
])
def test_get_mask_the_bankcard(card_number, expected):
    assert get_mask_the_bankcard(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("736 541084 301358 74305", "**4305"),
    ("73654108430135874305 4", "Не верный номер счета")
])
def test_get_mask_the_bank_account(account_number, expected):
    assert get_mask_the_bank_account(account_number) == expected
