import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException
from logging_config import logger

# Load the secret keys from the .env file
load_dotenv()

API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')

def get_client():
    """Initializes and returns the Binance Futures Testnet client."""
    try:
        if not API_KEY or not API_SECRET:
            logger.error("API keys are missing! Check your .env file.")
            return None

        # testnet=True is CRITICAL. Without it, you connect to the real exchange!
        client = Client(API_KEY, API_SECRET, testnet=True)
        
        # Test the connection by pinging the futures server
        client.futures_ping()
        logger.info("Successfully connected to Binance Futures Testnet.")
        return client
        
    except BinanceAPIException as e:
        logger.error(f"Failed to connect to Binance: {e.message}")
        return None
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None

# This block allows us to run this file directly to test the connection
if __name__ == "__main__":
    logger.info("Testing Binance connection...")
    test_client = get_client()