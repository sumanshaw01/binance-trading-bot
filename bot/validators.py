from bot.logging_config import logger

def validate_order_input(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    if side.upper() not in ['BUY', 'SELL']:
        raise ValueError("Side must be either 'BUY' or 'SELL'.")
    
    if order_type.upper() not in ['MARKET', 'LIMIT']:
        raise ValueError("Order type must be either 'MARKET' or 'LIMIT'.")
    
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
    
    if order_type.upper() == 'LIMIT' and (price is None or price <= 0):
        raise ValueError("LIMIT orders require a price greater than 0.")
    
    logger.info(f"Input validated: {order_type.upper()} {side.upper()} {quantity} {symbol.upper()}")
    return True