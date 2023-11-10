from datetime import datetime


def log(filename=None):
    def wrapper(func):
        def inner(*args, **kwargs):
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
                log_message = f"{datetime.now()} {func.__name__} error: {type(err).__name__}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message)
                else:
                    print(log_message)

        return inner

    return wrapper
