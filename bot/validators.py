def validate_order_type(order_type):
    if order_type.upper() not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Order type must be MARKET, LIMIT or STOP_LIMIT")
