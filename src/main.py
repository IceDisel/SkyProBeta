from src import log
from src.settings import PATH_CSV, PATH_JSON, PATH_XLSX
from src.utils import get_transaction_amount_rub, read_csv_xlsx_file, read_json_file

# from src.processing import dictionary_sorted, get_dictionary_search
logger = log.setup_logging()


def main() -> None:
    """Данный код для проверки"""

    print(read_json_file(PATH_JSON))
    transaction = read_json_file(PATH_JSON)
    print(get_transaction_amount_rub(transaction[0]))
    print(transaction[0])

    print("=================-----------")

    print(read_csv_xlsx_file(PATH_CSV)[1])

    print("======++++++++++===========")

    print(read_csv_xlsx_file(PATH_XLSX)[998])


if __name__ == "__main__":
    main()
