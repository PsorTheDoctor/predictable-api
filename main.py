from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from status import *
from subscribers import *
from future_prices import *
from mail_service import *

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscribers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

api.add_resource(ServerStatus, '/')

api.add_resource(SubscriberList, '/subscribers')
api.add_resource(Subscriber, '/subscribers/<string:sub_id>')

api.add_resource(FuturePriceList, '/prices')
api.add_resource(FuturePrice, '/prices/<string:currency>')

api.add_resource(InstantMailService, '/mail/<string:recipient>')
api.add_resource(NewsletterService, '/newsletter/<string:recipient>')


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
