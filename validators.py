def validate_order_input(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """Validates and formats the input before sending to Binance."""
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    if side not in ['BUY', 'SELL']:
        raise ValueError("Side must be either 'BUY' or 'SELL'.")
    
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValueError("Order type must be either 'MARKET' or 'LIMIT'.")
        
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
        
    if order_type == 'LIMIT' and (price is None or price <= 0):
        raise ValueError("A valid price>0 is required for LIMIT orders.")
        
    return symbol, side, order_type, quantity, price