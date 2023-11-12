# from data.data import TRANSACTIONS
# from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
# from src.masks import get_mask_the_bankcard


# from src.processing import dictionary_sorted, get_dictionary_search


def main() -> None:
    """Данный код для проверки"""

    # print(get_dictionary_search(DATA_LIST, "CANCELED"))
    # print(get_dictionary_search(DATA_LIST))
    # print()
    # print(dictionary_sorted(DATA_LIST, False))
    # [print(item) for item in dictionary_sorted(DATA_LIST)]
    #
    # usd_transactions = filter_by_currency(TRANSACTIONS, "USD")
    #
    # for _ in range(2):
    #     print(next(usd_transactions)["id"])
    #
    # descriptions = transaction_descriptions(TRANSACTIONS)
    #
    # for _ in range(5):
    #     print(next(descriptions))
    #
    # for card_number in card_number_generator(1, 5):
    #     print(card_number)


if __name__ == "__main__":
    main()
