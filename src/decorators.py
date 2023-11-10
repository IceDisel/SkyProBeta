from datetime import datetime
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    def wrapper(func: Callable) -> Callable:
        def inner(*args: Any, **kwargs: Any) -> Any:

            try:
                result = func(*args, **kwargs)
                log_message = f"{datetime.now()} {func.__name__} ok\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message)
                else:
                    print(log_message)
                return result
            except Exception as err:
                log_mess = f"{datetime.now()} {func.__name__} error: {type(err).__name__}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_mess)
                else:
                    print(log_mess)

        return inner

    return wrapper
