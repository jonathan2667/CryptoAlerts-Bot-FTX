# Crypto Alert Bot 🚨💹

This Python script utilizes the `telebot` library to interact with Telegram Bot API, and leverages financial data APIs like `yfinance`, `ccxt`, and `ftx` to monitor and alert users on cryptocurrency price movements. It's designed to send alerts via Telegram when specific cryptocurrencies cross predefined price thresholds.

## Features

- **Live Price Checks**: Use `/price` command to get the current price of any cryptocurrency.
- **Price Alerts**: Set alerts for when the price of a cryptocurrency goes above or below a certain point using the `/alert` command.
- **Automatic Updates**: The bot continually checks for price thresholds being crossed and sends updates.

## How to Use

1. **Start the Bot**: Interact with the bot on Telegram using the provided `API_KEY`.
2. **Check Prices**: Send `/price [cryptocurrency]` to get the current USD price of the cryptocurrency.
3. **Set Alerts**: Use `/alert [cryptocurrency] [symbol] [price]` to set an alert for when the cryptocurrency reaches the specified price.
4. **Receive Alerts**: The bot will automatically message you when your set price points are reached.

## Setup

1. **Dependencies**: Ensure you have `telebot`, `yfinance`, `ccxt`, `pandas`, and `requests` installed.
2. **API Key**: Insert your Telegram Bot API key and chat ID in the script.
3. **Keep Alive**: The `keep_alive` function is used to keep the bot running continuously.

## Commands

- `/price [cryptocurrency]`: Retrieves the current price of the specified cryptocurrency in USD.
- `/alert [cryptocurrency] [symbol] [price]`: Sets an alert for when the cryptocurrency reaches the specified price.

## Contributing

Feel free to fork this project and submit pull requests with new features or improvements. Please ensure your code adheres to the project's coding standards.

## License

This project is released under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Uses [FTX API](https://ftx.com/api) for fetching cryptocurrency prices.
- Utilizes [Telebot](https://github.com/eternnoir/pyTelegramBotAPI) for Telegram Bot interactions.
- Financial data fetched using [yfinance](https://pypi.org/project/yfinance/) and [ccxt](https://github.com/ccxt/ccxt).

**Happy Trading!** 📈🔔
