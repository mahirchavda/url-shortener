import logging
import logging.handlers as handlers

import const


class Logger:
    _loggers = {}

    @staticmethod
    def get_logger(name, level=logging.INFO):
        if name in Logger._loggers:
            return Logger._loggers[name]

        logger = logging.getLogger(name)

        file_handler = logging.FileHandler(const.LOG_FILE)
        formatter = logging.Formatter(
            "%(asctime)s - %(process)d - %(threadName)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(level)
        logger.propagate = False

        Logger._loggers[name] = logger
        return logger
