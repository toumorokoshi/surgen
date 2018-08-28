import coloredlogs
import logging

def setup_logging(level=logging.INFO):
    root_logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setLevel(level)
    formatter = coloredLogs.ColoredFormatter()
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
