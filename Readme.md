# Binance Futures Testnet Trading Bot

## Overview
A modular, lightweight Python CLI application designed to securely place Market and Limit orders on the Binance Futures Testnet (USDT-M).

## Project Structure
The code follows a strict separation of concerns, decoupling the API logic from the CLI interface:
* `bot/client.py`: Handles secure authentication.
* `bot/validators.py`: Ensures strict user input validation before API execution.
* `bot/orders.py`: Manages request payloads and exception handling.
* `bot/logging_config.py`: Dual-logging system (terminal output and persistent `app.log`).
* `cli.py`: The main entry point using `argparse`.

## Setup & Installation
1. Ensure Python 3.8+ is installed.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt


CRITICAL: Create a .env file in the root directory and add your Testnet keys:

    BINANCE_TESTNET_API_KEY=your_api_key_here
    BINANCE_TESTNET_SECRET_KEY=your_secret_key_here


How to Run Examples:

Placing a Market Order (BUY):

    python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Placing a Limit Order (SELL):

    python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000


Assumptions:

The user has activated a Binance Futures Testnet account and has a sufficient USDT test balance.

The application assumes a standard Windows/Linux terminal environment for CLI execution.