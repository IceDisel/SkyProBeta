from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, который записывает выполнение функции в лог.

    :param filename: (Optional[str]): Имя файла лога для записи.
    Если не указано, сообщение лога будет выведено в консоль.

    :return: Callable: Декорированная функция.
    """
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                log_message = f"{now} {func.__name__} ok\n"
            except Exception as err:
                log_message = f"{now} {func.__name__} error: {type(err).__name__}. Inputs: {args}, {kwargs}\n"
                result = None
            if filename:
                with open(filename, "a") as file:
                    file.write(log_message)
            else:
                print(log_message)
            return result

        return inner

    return wrapper
