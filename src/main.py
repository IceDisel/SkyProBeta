from src import log
from src.masks import get_mask_the_bank_account, get_mask_the_bankcard
from src.settings import PATH_JSON
from src.utils import get_transaction_amount_rub, read_json_file

# from src.processing import dictionary_sorted, get_dictionary_search
logger = log.setup_logging()


def main() -> None:
    """Данный код для проверки"""

    print(read_json_file(PATH_JSON))
    transaction = read_json_file(PATH_JSON)
    print(get_transaction_amount_rub(transaction[0]))

    get_mask_the_bankcard("7895 456 85469 4526")
    get_mask_the_bankcard("7895 456 85469 452")

    get_mask_the_bank_account("42569854756958452365")
    get_mask_the_bank_account("425698547569584523658")


if __name__ == "__main__":
    main()
