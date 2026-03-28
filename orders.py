from binance.exceptions import BinanceAPIException
from client import get_client
from logging_config import logger

def execute_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """Sends the validated order request to Binance Futures."""
    client = get_client()
    if not client:
        return None

    try:
        # Build the base order parameters
        params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity,
        }

        # If it's a LIMIT order, Binance requires a price and a timeInForce
        if order_type == 'LIMIT':
            params['price'] = price
            params['timeInForce'] = 'GTC'  # GTC = Good Till Canceled

        logger.info(f"Sending Request: {side} {quantity} {symbol} | Type: {order_type}")
        
        # Place the order via the python-binance library
        response = client.futures_create_order(**params)
        
        # Log and return the successful response
        logger.info(f"Order Success! ID: {response.get('orderId')} | Status: {response.get('status')} | Executed Qty: {response.get('executedQty')}")
        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.message} (Code: {e.code})")
        return None
    except Exception as e:
        logger.error(f"Unexpected System Error: {e}")
        return None