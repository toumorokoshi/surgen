import coloredlogs
import logging


def setup_logging(level):
    level = logging.getLevelName(level)
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setLevel(level)
    formatter = coloredlogs.ColoredFormatter("%(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
