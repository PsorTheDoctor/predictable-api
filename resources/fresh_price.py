from flask_restful import Resource

from utils.coin_gecko import get_fresh_price


class FreshPrice(Resource):
    def get(self, currency):
        price = get_fresh_price(currency)
        return {'price': price}
