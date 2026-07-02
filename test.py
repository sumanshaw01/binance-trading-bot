import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()
api_key = os.getenv("BINANCE_TESTNET_API_KEY")
secret_key = os.getenv("BINANCE_TESTNET_SECRET_KEY")

client = Client(api_key, secret_key, testnet=True)

try:
    print("Attempting to place a MARKET BUY order for BTCUSDT...")
    
    response = client.futures_create_order(
        symbol='BTCUSDT',
        side='BUY',
        type='MARKET',
        quantity=0.001
    )
    
    print("\nSUCCESS! Order placed. Here is the data from Binance:")
    print(response)

except Exception as e:
    print(f"\nFAILED! The error is: {e}")