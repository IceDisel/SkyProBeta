from data.data import DATA_LIST
from src.processing import dictionary_sorted, get_dictionary_search


def main() -> None:
    """Данный код для проверки"""

    print(get_dictionary_search(DATA_LIST, "CANCELED"))
    print(get_dictionary_search(DATA_LIST))
    print()
    print(dictionary_sorted(DATA_LIST, False))
    [print(item) for item in dictionary_sorted(DATA_LIST)]


if __name__ == "__main__":
    main()
