import logging
import sys
from logging import FileHandler, Formatter, StreamHandler


def logger_init(app_mode):
    logger = logging.getLogger(__name__)
    if app_mode == "DEBUG":
        logger.setLevel(logging.DEBUG)
    elif app_mode == "PROD":
        logger.setLevel(logging.INFO)
    else:
        raise ValueError("not recognized app_mode... (DEGUG or PROD needed)")
    s_handler = StreamHandler(stream=sys.stdout)
    s_handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
    f_handler = FileHandler(filename="logs.log")
    f_handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))

    logger.addHandler(s_handler)
    logger.addHandler(f_handler)
    return logger
