from flask_restful import Resource, reqparse, abort
from utils.machine_learning import predict_prices

FUTURE_PRICES = {
    'bitcoin': {'01-08-2020': 1.0},
    'ethereum': {'01-08-2020': 2.0},
    'ripple': {'01-08-2020': 3.0}
}


def abort_if_currency_doesnt_exist(currency):
    if currency not in FUTURE_PRICES:
        abort(404, message="Currency {} doesn't exist".format(currency))


parser = reqparse.RequestParser()
parser.add_argument('currency', type=str, required=True)


class FuturePrice(Resource):
    def get(self, currency):
        abort_if_currency_doesnt_exist(currency)
        prices = predict_prices(currency)
        FUTURE_PRICES[currency] = prices
        return FUTURE_PRICES[currency]


class FuturePriceList(Resource):
    def get(self):
        return FUTURE_PRICES
