from src.widget import convert_date, get_mask_bankcard_account


def main():
    """Данный код для проверки"""
    print(get_mask_bankcard_account("Visa Classic 6831982476737658"))
    print(get_mask_bankcard_account("Maestro 1596837868705199"))
    print(get_mask_bankcard_account("MasterCard 7158300734726758"))
    print(get_mask_bankcard_account("Счет 35383033474447895560"))

    print(convert_date("2018-07-11T02:26:18.671407"))


if __name__ == "__main__":
    main()
