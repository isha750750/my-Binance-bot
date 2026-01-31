from rich.console import Console
from rich.prompt import Prompt, FloatPrompt
from bot.orders import place_market_order, place_limit_order
from bot.orders import place_market_order, place_limit_order

console = Console()

def start_menu():
    console.rule("[bold cyan]Binance Futures Testnet Bot[/bold cyan]")

    symbol = Prompt.ask("Symbol", default="BTCUSDT")
    side = Prompt.ask("Side", choices=["BUY", "SELL"])
    order_type = Prompt.ask(
        "Order Type",
        choices=["MARKET", "LIMIT", "STOP_LIMIT"]
    )
    quantity = FloatPrompt.ask("Quantity")

    if order_type == "MARKET":
        order = place_market_order(symbol, side, quantity)

    elif order_type == "LIMIT":
        price = FloatPrompt.ask("Limit Price")
        order = place_limit_order(symbol, side, quantity, price)

    else:
        stop_price = FloatPrompt.ask("Stop Price")
        limit_price = FloatPrompt.ask("Limit Price")
        order = place_stop_limit_order(
            symbol, side, quantity, stop_price, limit_price
        )

    if order:
        console.print("[green]Order placed successfully![/green]")
        console.print(order)
    else:
        console.print("[red]Order failed. Check logs.[/red]")

if __name__ == "__main__":
    start_menu()
