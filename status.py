from flask_restful import Resource


class ServerStatus(Resource):
    def get(self):
        return {'status': 'ok'}
