from flask import Flask
# from flask_cors import CORS

from api import create_api
from db import db_session

app = Flask(__name__)
create_api(app)
# CORS(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# Enabling CORS
# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE')
#     return response


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
