from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.logging_config import logger

def place_order(client, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    try:
        params = {
            'symbol': symbol.upper(),
            'side': side.upper(),
            'type': order_type.upper(),
            'quantity': quantity
        }
        
        # Limit orders require a price and a "Time in Force" (GTC = Good Till Canceled)
        if order_type.upper() == 'LIMIT':
            params['price'] = price
            params['timeInForce'] = 'GTC' 
            
        logger.info(f"Sending order payload to Binance: {params}")
        response = client.futures_create_order(**params)
        
        logger.info(f"SUCCESS! Order placed.")
        logger.info(f"Order ID: {response.get('orderId')} | Status: {response.get('status')} | Executed Qty: {response.get('executedQty')}")
        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.message}")
    except BinanceRequestException as e:
        logger.error(f"Network Error: {e}")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
    
    return None