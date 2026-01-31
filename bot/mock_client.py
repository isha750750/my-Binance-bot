import uuid
import time

class MockBinanceFuturesClient:
    def futures_create_order(self, **kwargs):
        time.sleep(0.5)  # simulate network delay

        return {
            "orderId": str(uuid.uuid4()),
            "symbol": kwargs.get("symbol"),
            "side": kwargs.get("side"),
            "type": kwargs.get("type"),
            "status": "FILLED",
            "price": kwargs.get("price", "0"),
            "avgPrice": kwargs.get("price", "0"),
            "origQty": kwargs.get("quantity"),
            "executedQty": kwargs.get("quantity"),
            "timeInForce": kwargs.get("timeInForce", "GTC")
        }
