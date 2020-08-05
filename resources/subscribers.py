from flask_restful import Resource, reqparse, abort, fields, marshal_with

from models.subscriber import SubscriberModel
from db import db_session

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True)
parser.add_argument('enrolling_date', type=str, required=True)

resource_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'enrolling_date': fields.DateTime
}


class Subscriber(Resource):
    @marshal_with(resource_fields)
    def get(self, email):
        response = SubscriberModel.query.filter_by(email=email).first()
        if not response:
            abort(404, message="Subscriber {} doesn't exist.".format(email))
        return response

    @marshal_with(resource_fields)
    def put(self, email):
        # args = parser.parse_args()
        response = SubscriberModel.query.filter_by(email=email).first()
        if response:
            abort(409, message="Subscriber {} already exists.".format(email))
        subscriber = SubscriberModel(email=email)
        db_session.add(subscriber)
        db_session.commit()
        return subscriber, 201

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
    def get(self):
        return SubscriberModel.query.all()

    def post(self):
        # TODO!
        return '', 201
