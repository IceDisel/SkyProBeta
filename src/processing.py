def get_dictionary_search(strings: list, state: str = "EXECUTED") -> list:
    """
    Функция принимает на вход список словарей и значение для ключа state
    (опциональный параметр со значением по умолчанию EXECUTED).
    :param strings:
    :param state:
    :return: Возвращает новый список, содержащий только те словари,
     у которых ключ state содержит переданное в функцию значение.
    """
    list_of_found = [dict_ for dict_ in strings if dict_["state"] == state]
    return list_of_found


def dictionary_sorted(strings: list, sorting_order: bool = True) -> list:
    """
    Функция принимает на вход список словарей, необязательный аргумент
    который задает порядок сортировки (убывание, возрастание).
    :param strings:
    :param sorting_order:
    :return: Возвращает новый список, в котором исходные словари отсортированы по убыванию даты.
    """

    sort_list = sorted(strings, key=lambda date: date["date"], reverse=sorting_order)
    return sort_list
