from flask_restful import Resource
from subscribers import abort_if_subscriber_doesnt_exist
from utils.mail_sender import *


def abort_if_address_isnt_valid(address):
    # TODO!
    pass


class InstantMailService(Resource):
    def get(self, recipient):
        abort_if_address_isnt_valid(recipient)
        send_email(recipient)
        return {'status': 'sent'}


class NewsletterService(Resource):
    def get(self, recipient):
        abort_if_address_isnt_valid(recipient)
        abort_if_subscriber_doesnt_exist(recipient)
        send_email_repeatedly(recipient, 24 * 3600)
        return {'status': 'sent'}
