import logging

logger = logging.getLogger(__name__)


def get_mask_the_bankcard(card_number: str) -> str:
    """
    Функция принимает номер банковской карты,
    возвращает замаскированый номер карты.
    """

    card_number = "".join(filter(str.isdigit, card_number))
    if len(card_number) != 16:
        logger.error("Не верный номер карты")
        return "Не верный номер карты"

    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    logger.info("Номер карты успешно замаскирован")

    return masked_number


def get_mask_the_bank_account(account_number: str) -> str:
    """
    Функция принимает номер банковского счета,
    возвращает замаскированый номер счета.
    """

    account_number = "".join(filter(str.isdigit, account_number))
    if len(account_number) != 20:
        logger.error("Неверный номер счета")
        return "Не верный номер счета"

    masked_number = f"**{account_number[-4:]}"
    logger.info("Номер счета успешно замаскирован")

    return masked_number
