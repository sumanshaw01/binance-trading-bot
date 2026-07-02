import os
from dotenv import load_dotenv
from binance.client import Client
from bot.logging_config import logger

def get_binance_client() -> Client:
    load_dotenv()
    api_key = os.getenv("BINANCE_TESTNET_API_KEY")
    secret_key = os.getenv("BINANCE_TESTNET_SECRET_KEY")
    
    if not api_key or not secret_key:
        logger.error("API keys missing from .env file.")
        raise ValueError("Missing API keys. Please check your .env file.")
        
    logger.info("Authenticating with Binance Futures Testnet...")
    return Client(api_key, secret_key, testnet=True)