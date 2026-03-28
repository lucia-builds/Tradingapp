import logging
import sys

def setup_logger():
    # Create a custom logger
    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)

    # Create handlers (Console and File)
    c_handler = logging.StreamHandler(sys.stdout)
    f_handler = logging.FileHandler('trading_bot.log')

    # Create formatters and add it to handlers
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(log_format)
    f_handler.setFormatter(log_format)

    # Add handlers to the logger (check to avoid duplicate lines)
    if not logger.handlers:
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

    return logger

# We initialize it here so other files can just import `logger`
logger = setup_logger()