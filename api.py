from flask_restful import Api

from resources.status import *
from resources.subscribers import *
from resources.future_prices import *
from resources.mail_service import *


def create_api(app):
    api = Api(app)
    api.add_resource(ServerStatus, '/')

    api.add_resource(SubscriberList, '/subscribers')
    api.add_resource(Subscriber, '/subscribers/<string:email>')

    api.add_resource(FuturePriceList, '/prices')
    api.add_resource(FuturePrice, '/prices/<string:currency>')

    api.add_resource(InstantMailService, '/mail/<string:recipient>')
    api.add_resource(NewsletterService, '/newsletter/<string:recipient>')
    return api
