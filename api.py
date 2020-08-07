from flask_restful import Api

from resources.status import *
from resources.subscribers import *
from resources.past_prices import *
from resources.fresh_price import *
from resources.future_prices import *
from resources.mail_service import *


def create_api(app):
    api = Api(app)
    api.add_resource(ServerStatus, '/', '/ping')

    api.add_resource(SubscriberList, '/subscribers', '/subscribers&confirm=<int:code>')
    api.add_resource(Subscriber, '/subscribers/<string:email>')
    api.add_resource(SubscriberQty, '/subscribers-qty')

    api.add_resource(PastPriceList, '/past-prices/<string:currency>')
    api.add_resource(PastPriceByDate, '/past-prices/<string:currency>&<string:date>')

    api.add_resource(FreshPrice, '/price/<string:currency>')

    api.add_resource(FuturePriceList, '/future-prices/<string:currency>')
    api.add_resource(FuturePrice, '/future-prices/<string:currency>&<string:date>')

    api.add_resource(InstantMailService, '/mail/<string:recipient>')
    api.add_resource(AuthMailService, '/auth/<string:recipient>')
    api.add_resource(NewsletterService, '/newsletter/<string:recipient>')
    return api
