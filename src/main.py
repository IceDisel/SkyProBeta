from src.settings import PATH_JSON
from src.utils import get_transaction_amount_rub, read_json_file

# from src.processing import dictionary_sorted, get_dictionary_search


def main() -> None:
    """Данный код для проверки"""

    print(read_json_file(PATH_JSON))
    transaction = read_json_file(PATH_JSON)
    print(get_transaction_amount_rub(transaction[0]))


if __name__ == "__main__":
    main()
