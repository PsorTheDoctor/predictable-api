from flask_restful import Resource, reqparse, abort

SUBSCRIBERS = {
    'sub1': {
        'email': 'psor2.01@gmail.com',
        'enrolling_date': '24-07-2020'
    }
}


def abort_if_subscriber_doesnt_exist(sub_id):
    if sub_id not in SUBSCRIBERS:
        abort(404, message="Subscriber {} doesn't exist".format(sub_id))


parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True)
parser.add_argument('enrolling_date', type=str, required=True)


class Subscriber(Resource):
    def get(self, sub_id):
        abort_if_subscriber_doesnt_exist(sub_id)
        return SUBSCRIBERS[sub_id]

    def put(self, sub_id):
        args = parser.parse_args()
        subscriber = {'subscriber': args['email']}
        SUBSCRIBERS[sub_id] = subscriber
        return subscriber, 201

    def delete(self, sub_id):
        abort_if_subscriber_doesnt_exist(sub_id)
        del SUBSCRIBERS[sub_id]
        return '', 204


class SubscriberList(Resource):
    def get(self):
        return SUBSCRIBERS

    def post(self):
        args = parser.parse_args()
        sub_id = int(max(SUBSCRIBERS.keys()).lstrip('sub')) + 1
        sub_id = 'sub%i' % sub_id
        SUBSCRIBERS[sub_id] = {'subscriber': args['email']}
        return SUBSCRIBERS[sub_id], 201
