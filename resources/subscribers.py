from flask_restful import Resource, reqparse, abort, fields, marshal_with

from models.subscriber import SubscriberModel
from utils.mail_sender import send_email
from db import db_session

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True)
parser.add_argument('enrolling_date', type=str)

resource_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'enrolling_date': fields.String
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
        subscriber = SubscriberModel.query.get_or_404(email=email).first()
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
            abort(409, message="Subscriber {} already exists.".format(args['email']))
        subscriber = SubscriberModel(email=args['email'], enrolling_date=args['enrolling_date'])
        db_session.add(subscriber)
        db_session.commit()

        send_email(args['email'])
        return subscriber, 201
