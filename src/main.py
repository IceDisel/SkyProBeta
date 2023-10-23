from src.masks import get_mask_the_bank_account, get_mask_the_bankcard


def main():
    """Данный код для проверки"""
    print(get_mask_the_bankcard("7000 7922 8960 6361"))

    print(get_mask_the_bank_account("73654108430135874305"))


if __name__ == "__main__":
    main()
