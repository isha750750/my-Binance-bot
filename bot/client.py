import os
from bot.logging_config import logger

USE_MOCK = True  # 👈 IMPORTANT FLAG

if USE_MOCK:
    from bot.mock_client import MockBinanceFuturesClient
    client = MockBinanceFuturesClient()
    logger.warning("Using MOCK Binance Futures client (KYC-free)")
else:
    from binance.client import Client
    from dotenv import load_dotenv

    load_dotenv()
    API_KEY = os.getenv("BINANCE_API_KEY")
    API_SECRET = os.getenv("BINANCE_API_SECRET")

    client = Client(API_KEY, API_SECRET, testnet=True)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi/v1"
    logger.info("Using REAL Binance Futures Testnet client")
