from flask_restful import Resource, reqparse, abort, fields, marshal_with

from models.subscriber import SubscriberModel
from utils.mail_sender import send_email
from db import db_session

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True)
parser.add_argument('since', type=str, required=True)
parser.add_argument('code', type=int, required=True)

resource_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'since': fields.String,
    'code': fields.Integer
}


class Subscriber(Resource):
    @marshal_with(resource_fields)
    def get(self, email):
        response = SubscriberModel.query.filter_by(email=email).first()
        if not response:
            abort(404, message="Subscriber {} doesn't exist.".format(email))
        return response

    @marshal_with(resource_fields)
    def delete(self, email):
        response = SubscriberModel.query.filter_by(email=email).first()
        if not response:
            abort(404, message="Subscriber {} doesn't exist.".format(email))
        else:
            send_email(email)

        subscriber = SubscriberModel.query.filter_by(email=email).first()
        db_session.delete(subscriber)
        db_session.commit()
        return '', 204


class SubscriberList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return SubscriberModel.query.all()

    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        response = SubscriberModel.query.filter_by(email=args['email']).first()
        if response:
            abort(409, message='Subscriber {} already exists.'.format(args['email']))
        else:
            # !!Imports code set by send_confirmation_email() method
            from utils.mail_sender import code

            if args['code'] == code:
                subscriber = SubscriberModel(email=args['email'],
                                             since=args['since'],
                                             code=args['code'])
                db_session.add(subscriber)
                db_session.commit()
            else:
                abort(401, message='The code is not valid.')
        return '', 201


class SubscriberQty(Resource):
    def get(self):
        return len(SubscriberModel.query.all())
