from flask_restful import Resource, abort

from resources.subscribers import SubscriberModel
from utils.mail_sender import *


def abort_if_address_isnt_valid(address):
    # TODO!
    pass


class InstantMailService(Resource):
    def get(self, recipient):
        abort_if_address_isnt_valid(recipient)
        send_email(recipient)
        return {'status': 'sent'}


class AuthMailService(Resource):
    def get(self, recipient, code):
        abort_if_address_isnt_valid(recipient)
        send_email(recipient, content=code)
        return {'status': 'sent'}


class NewsletterService(Resource):
    def get(self, recipient):
        abort_if_address_isnt_valid(recipient)
        response = SubscriberModel.query.filter_by(email=recipient).first()
        if not response:
            abort(404, message="Recipient {} doesn't exist.".format(recipient))
        send_email_repeatedly(recipient, 24 * 3600)
        return {'status': 'sent'}
