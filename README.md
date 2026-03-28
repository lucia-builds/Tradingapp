# Binance Futures Testnet Trading Bot
A simplified Python Command Line Interface (CLI) application to execute Market and Limit orders on the Binance Futures Testnet (USDT-M).
## Features
* **Order Execution:** Place MARKET and LIMIT orders (BUY/SELL).
* **Validation:** Strict input validation for quantities, prices, and order types.
* **Error Handling:** Graceful handling of Binance API exceptions.
* **Logging:** Console and file-based logging (`trading_bot.log`).
* **Interactive CLI:** Built with `Typer` and `Rich` for a clean, user-friendly terminal experience.
## Setup Instructions

1. **Clone the repository:**
   \`\`\`bash
   git clone <your-repo-url>
   cd Trade_Bot
   \`\`\`
2. **Set up a virtual environment (optional but recommended):**
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   \`\`\`

3. **Install dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your Binance Futures Testnet API credentials:
   \`\`\`text
   BINANCE_API_KEY=your_testnet_api_key
   BINANCE_API_SECRET=your_testnet_api_secret
   \`\`\`

## How to Run Examples

You can run the bot interactively or pass arguments directly via the CLI.

**Example 1: Interactive Market Order**
If you run the script without arguments, it will prompt you for the required fields:
\`\`\`bash
python cli.py
\`\`\`

**Example 2: One-Line Market Order**
\`\`\`bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.01
\`\`\`

**Example 3: One-Line Limit Order**
*(Note: LIMIT orders require the `--price` flag)*
\`\`\`bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 65000
\`\`\`

## Assumptions Made
* **Futures Trading:** The prompt specified USDT-M, so the bot uses the `futures_create_order` endpoints, not Spot endpoints.
* **Time in Force:** All LIMIT orders default to `GTC` (Good Till Canceled).
* **Testnet Exclusivity:** The client is hardcoded to `testnet=True` to prevent accidental trades on live accounts.