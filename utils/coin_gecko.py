from pycoingecko import CoinGeckoAPI

api = CoinGeckoAPI()


def get_single_price(currency, date, vs_currency='usd'):
    history = api.get_coin_history_by_id(currency, date)
    return history['market_data']['current_price'][vs_currency]


def get_fresh_price(currency, vs_currency='usd'):
    price = api.get_price(currency, vs_currency)
    return price[currency][vs_currency]
