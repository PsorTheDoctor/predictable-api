from pycoingecko import CoinGeckoAPI

api = CoinGeckoAPI()


def get_single_price(currency, date, vs_currency='usd'):
    history = api.get_coin_history_by_id(currency, date)
    return history['market_data']['current_price'][vs_currency]
