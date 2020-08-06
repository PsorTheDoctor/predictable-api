from flask import Flask

from api import create_api
from db import db_session
from cors import enable_cors

app = Flask(__name__)
create_api(app)
enable_cors(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
