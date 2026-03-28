# Binance Futures Testnet Trading Bot 🚀

Hey there! This is my submission for the Python Developer application task. It's a modular CLI tool that lets you fire off Market and Limit orders directly to the Binance Futures Testnet (USDT-M).

I wanted to keep the codebase clean, readable, and easy to run. Instead of just dumping raw JSON responses into the terminal, I added a bit of polish to the user experience.

## What's Inside?
* **Core Trading:** Safely executes `MARKET` and `LIMIT` orders for both BUY and SELL sides.
* **Interactive CLI:** I used `Typer` and `Rich` for the interface. If you forget to pass an argument, it will prompt you interactively rather than just crashing. Plus, successful trades print out in a clean, colorized terminal table.
* **Input Validation:** Catches bad inputs (like negative quantities or missing prices) before making unnecessary API calls.
* **Logging:** Everything is tracked. All API requests, successful orders, and exceptions are printed to the console and appended to `trading_bot.log`.

---

## Getting Started

Getting this running locally is pretty straightforward. 

**1. Clone the repo:**
\`\`\`bash
git clone <your-repo-url>
cd Trade_Bot
\`\`\`

**2. Spin up a virtual environment (recommended):**
\`\`\`bash
python -m venv venv
source venv/bin/activate  # Windows users: venv\Scripts\activate
\`\`\`

**3. Install the dependencies:**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

**4. Hook up your API keys:**
Create a `.env` file right in the root directory. Grab your keys from the Binance Testnet dashboard and drop them in like this:
\`\`\`text
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_api_secret_here
\`\`\`

---

## Firing Off Trades

You can either let the CLI guide you interactively, or pass everything as flags if you want to do it in one line.

### Option A: Interactive Mode (Easiest)
Just run the script and let it ask you for the details.
\`\`\`bash
python cli.py
\`\`\`

### Option B: One-Line Commands
Great for quick testing. 

**Market Order:**
\`\`\`bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.01
\`\`\`

**Limit Order:**
*(Note: Limit orders require the `--price` flag to be passed)*
\`\`\`bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 65000
\`\`\`

---

## Design Choices & Notes

Just a few quick notes on how I approached this build:

* **Safety First:** I hardcoded `testnet=True` inside the Binance client initialization (`client.py`). I didn't want any risk of this accidentally pointing to a live production account.
* **python-binance vs Raw Requests:** I opted to use the `python-binance` wrapper instead of writing raw HTTP requests. It handles the HMAC SHA256 request signing under the hood, which keeps the client layer a lot cleaner and easier to scale.
* **Futures vs Spot:** Since the prompt specifically requested USDT-M, the bot strictly uses the `futures_create_order` endpoints.
* **Time In Force:** For the Limit orders, I defaulted the `timeInForce` parameter to `GTC` (Good Till Canceled) as it's the standard for basic limit setups.
* **Zero Executed Qty:** If you check the logs and see an `Executed Qty` of `0.000` on a Market order, it's just because the Testnet liquidity is very low. The API immediately returns a status of `NEW` while it waits for a fake market maker to fill the other side of the trade!