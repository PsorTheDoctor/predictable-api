from flask_restful import Resource, reqparse, abort, fields, marshal_with
from datetime import datetime
from main import db


class SubscriberModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    enrolling_date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    def __repr__(self):
        return self.email


parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True)
parser.add_argument('enrolling_date', type=str, required=True)

resource_fields: {
    'id': fields.Integer,
    'email': fields.String,
    'enrolling_date': fields.String
}


class Subscriber(Resource):
    @marshal_with(resource_fields)
    def get(self, sub_id):
        response = SubscriberModel.query.filter_by(id=sub_id).first()
        if not response:
            abort(404, message="Subscriber {} doesn't exist.".format(sub_id))
        return response

    @marshal_with(resource_fields)
    def put(self, sub_id):
        args = parser.parse_args()
        response = SubscriberModel.query.filter_by(id=sub_id).first()
        if response:
            abort(409, message="Subscriber {} already exists.".format(sub_id))
        subscriber = SubscriberModel(id=sub_id, email=args['email'])
        db.session.add(subscriber)
        db.session.commit()
        return subscriber, 201

    @marshal_with(resource_fields)
    def delete(self, sub_id):
        response = SubscriberModel.query.filter_by(id=sub_id).first()
        if not response:
            abort(404, message="Subscriber {} doesn't exist.".format(sub_id))
        subscriber = SubscriberModel.query.get_or_404(id=sub_id).first()
        db.session.delete(subscriber)
        db.session.commit()
        return '', 204


class SubscriberList(Resource):
    def get(self):
        return SubscriberModel.query.all()

    def post(self):
        # TODO!
        return '', 201
