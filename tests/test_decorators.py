import os.path
from datetime import datetime
from typing import Any

import pytest

from src.decorators import log


@pytest.mark.parametrize("arg_1, arg_2, expected_result", [(1, 0, " foo error: ZeroDivisionError. Inputs: (1, 0), {}"),
                                                           (1, 2, " foo ok")
                                                           ])
def test_log_decorator(arg_1: int, arg_2: int, expected_result: str) -> None:
    """
    Тестирование декоратора log с записью в файл.
    :param arg_1: Первый аргумент функции foo.
    :param arg_2: Второй аргумент функции foo.
    :param expected_result: Ожидаемый результат выполнения функции foo.
    :return: None
    """
    filename = 'test.txt'
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename)
    def foo(x: int, y: int) -> float:
        return x / y

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    foo(arg_1, arg_2)

    with open(filename) as file:
        log_mess = file.read().strip()

    expected_log = now + expected_result

    assert log_mess == expected_log


@pytest.mark.parametrize("arg_1, arg_2, expected_result", [(1, 0, " foo error: ZeroDivisionError. Inputs: (1, 0), {}"),
                                                           (1, 2, " foo ok")
                                                           ])
def test_console_log(capsys: Any, arg_1: int, arg_2: int, expected_result: str) -> None:
    """
    Тестирование декоратора log с выводом в консоль.
    :param capsys: Фикстура pytest для перехвата вывода в консоль.
    :param arg_1: Первый аргумент функции foo.
    :param arg_2: Второй аргумент функции foo.
    :param expected_result: Ожидаемый результат выполнения функции foo.
    :return: None
    """
    @log()
    def foo(x: int, y: int) -> float:
        return x / y

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    foo(arg_1, arg_2)

    expected_log = now + expected_result

    log_mess = capsys.readouterr()

    assert log_mess.out.strip() == expected_log
