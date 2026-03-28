import typer
from typing import Optional
from validators import validate_order_input
from orders import execute_order
from logging_config import logger
from rich.console import Console
from rich.table import Table

# Initialize the Typer app and Rich console
app = typer.Typer(help="Simplified Trading Bot for Binance Futures Testnet")
console = Console()

@app.command()
def trade(
    symbol: str = typer.Option(..., prompt="Symbol (e.g. BTCUSDT)", help="Trading pair"),
    side: str = typer.Option(..., prompt="Side (BUY/SELL)", help="Trade direction"),
    order_type: str = typer.Option(..., prompt="Order Type (MARKET/LIMIT)", help="Type of order"),
    quantity: float = typer.Option(..., prompt="Quantity", help="Amount to trade"),
    price: Optional[float] = typer.Option(None, help="Price (Required for LIMIT orders)")
):
    """Place a trade on Binance Futures Testnet."""
    try:
        # 1. Validate Input (this will raise an error if they typed something wrong)
        sym, sde, typ, qty, prc = validate_order_input(symbol, side, order_type, quantity, price)
        
        console.print(f"\n[bold yellow]Processing {typ} order: {sde} {qty} {sym}...[/bold yellow]")
        
        # 2. Execute Order
        response = execute_order(sym, sde, typ, qty, prc)
        
        # 3. Print Beautiful Output if successful
        if response:
            table = Table(title="✅ Order Successfully Placed!", style="green")
            table.add_column("Order ID", justify="center")
            table.add_column("Status", justify="center")
            table.add_column("Executed Qty", justify="center")
            
            table.add_row(
                str(response.get('orderId', 'N/A')),
                str(response.get('status', 'N/A')),
                str(response.get('executedQty', 'N/A'))
            )
            console.print(table)
        else:
            console.print("[bold red]❌ Order Failed! Check trading_bot.log for details.[/bold red]")

    except ValueError as e:
        console.print(f"[bold red]Input Error:[/bold red] {e}")
        logger.warning(f"User input error: {e}")

if __name__ == "__main__":
    app()