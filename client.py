import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException
from logging_config import logger

# secret key loading from .env file
load_dotenv()

API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')

def get_client():
    """Initializes and returns the Binance Futures Testnet client."""
    try:
        if not API_KEY or not API_SECRET:
            logger.error("API keys are missing! Check your .env file.")
            return None

        client = Client(API_KEY, API_SECRET, testnet=True)
        
        # Testing the connection
        client.futures_ping()
        logger.info("Successfully connected to Binance Futures Testnet.")
        return client
        
    except BinanceAPIException as e:
        logger.error(f"Failed to connect to Binance: {e.message}")
        return None
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    logger.info("Testing Binance connection...")
    test_client = get_client()