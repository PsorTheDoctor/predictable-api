from flask_restful import Resource, abort, fields, marshal_with

from models.past_price import PastPriceModel
from db import db_session
from utils.coin_gecko import *

resource_fields = {
    'id': fields.Integer,
    'currency': fields.String,
    'date': fields.String,
    'value': fields.Float,
    # 'n_days_ago': fields.Integer
}


class PastPriceList(Resource):
    @marshal_with(resource_fields)
    def get(self, currency):
        response = PastPriceModel.query.filter_by(currency=currency).all()
        if not response:
            abort(404, message='No data')
        return response


class PastPriceByDate(Resource):
    @marshal_with(resource_fields)
    def get(self, currency, date):
        response = PastPriceModel.query.filter_by(currency=currency).filter_by(date=date).first()

        if not response:
            value = get_single_price(currency, date)
            price = PastPriceModel(currency, date, value)
            db_session.add(price)
            db_session.commit()
            response = price
        return response


# class AllPastPricesList(Resource):
#     def get(self):
#         return PastPriceModel.query.all()
