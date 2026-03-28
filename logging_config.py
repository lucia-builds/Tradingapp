import logging
import sys

def setup_logger():
    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)

    c_handler = logging.StreamHandler(sys.stdout)
    f_handler = logging.FileHandler('trading_bot.log')

    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(log_format)
    f_handler.setFormatter(log_format)

    if not logger.handlers:
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

    return logger

# initializing it so that others can import `logger`
logger = setup_logger()