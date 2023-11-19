import logging


def setup_logging() -> logging.Logger:
    """
    Установка уровня логирования
    :return: logging Logger
    """
    logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', encoding='UTF-8',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger()

    return logger
