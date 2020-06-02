import inspect
import logging
from pathlib import Path


def custom_logger(log_level=logging.DEBUG):
    # gets the name of the class or method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # By default, log all events
    logger.setLevel(logging.DEBUG)

    Path("./tests/logs").mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(f'./tests/logs/{logger_name}.log', mode='a+')
    # file_handler = logging.FileHandler('automation.log', mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
