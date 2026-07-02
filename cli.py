import argparse
from bot.client import get_binance_client
from bot.validators import validate_order_input
from bot.orders import place_order
from bot.logging_config import logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", type=str, required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL", "buy", "sell"], help="Order side (BUY/SELL)")
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT", "market", "limit"], help="Order type (MARKET/LIMIT)")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Order price (required for LIMIT)")

    args = parser.parse_args()

    try:
        validate_order_input(args.symbol, args.side, args.type, args.quantity, args.price)
        
        client = get_binance_client()
        
        place_order(client, args.symbol, args.side, args.type, args.quantity, args.price)
        
    except ValueError as e:
        logger.error(f"Validation Error: {e}")
    except Exception as e:
        logger.error(f"Application Error: {e}")

if __name__ == "__main__":
    main()