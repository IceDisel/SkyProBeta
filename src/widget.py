from datetime import datetime

from src.masks import get_mask_the_bank_account, get_mask_the_bankcard


def get_mask_bankcard_account(number_name: str) -> str:
    """
    Принимает на вход строку информацией тип карты/счета и номер карты/счета
    :return: возвращает эту строку с замаскированным номером карты/счета.
    """

    split_number_name = number_name.split()

    if "Счет" in split_number_name:
        mask_bank_account = get_mask_the_bank_account(split_number_name[-1])
        return ' '.join(split_number_name[:-1]) + " " + mask_bank_account
    else:
        mask_bankcard = get_mask_the_bankcard(split_number_name[-1])
        return ' '.join(split_number_name[:-1]) + " " + mask_bankcard


def convert_date(date_string: str) -> str:
    """
    Принимает на вход строку, вида "2018-07-11T02:26:18.671407"
    :return: возвращает строку с датой в виде "11.07.2018"
    """

    date_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date
