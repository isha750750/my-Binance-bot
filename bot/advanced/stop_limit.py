from bot.client import client
from bot.logging_config import logger

def place_stop_limit_order(symbol, side, quantity, stop_price, limit_price):
    try:
        logger.info(
            f"Placing STOP-LIMIT order: {side} {quantity} {symbol} "
            f"stop={stop_price} limit={limit_price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=quantity,
            stopPrice=stop_price,
            price=limit_price,
            timeInForce="GTC"
        )

        logger.info(f"Stop-Limit order response: {order}")
        return order

    except Exception as e:
        logger.error(f"Stop-Limit order failed: {e}")
        return None
