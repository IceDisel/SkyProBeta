import pytest

from src.processing import dictionary_sorted, get_dictionary_search


@pytest.fixture
def sample_data() -> list[dict]:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


# Тесты для функции get_dictionary_search
def test_get_dictionary_search_with_state_executed(sample_data: list[dict]) -> None:
    result = get_dictionary_search(sample_data, state="EXECUTED")
    assert len(result) == 2
    assert all(d['state'] == 'EXECUTED' for d in result)


def test_get_dictionary_search_with_state_canceled(sample_data: list[dict]) -> None:
    result = get_dictionary_search(sample_data, state="CANCELED")
    assert len(result) == 2
    assert all(d['state'] == 'CANCELED' for d in result)


def test_get_dictionary_search_with_state_nonexistent(sample_data: list[dict]) -> None:
    result = get_dictionary_search(sample_data, state="NONEXISTENT")
    assert len(result) == 0


# Тесты для функции dictionary_sorted
def test_dictionary_sorted_ascending(sample_data: list[dict]) -> None:
    result = dictionary_sorted(sample_data, sorting_order=True)
    assert len(result) == 4
    assert result[-1]['date'] == '2018-06-30T02:08:58.425572'
    assert result[0]['date'] == '2019-07-03T18:35:29.512364'


def test_dictionary_sorted_descending(sample_data: list[dict]) -> None:
    result = dictionary_sorted(sample_data, sorting_order=False)
    assert len(result) == 4
    assert result[-1]['date'] == '2019-07-03T18:35:29.512364'
    assert result[0]['date'] == '2018-06-30T02:08:58.425572'
