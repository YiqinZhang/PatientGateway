import os

from flask import Flask
from Modules import home, auth

DB_NAME = "/DB/database.db"


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='key',
        DATABASE=os.path.join(app.instance_path, '/DB/database.db'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from DB import db
    db.init_app(app)

    from .home import h
    from .auth import auth
    app.register_blueprint(h, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')



    #
    # # a simple page that says hello
    # @app.route('/hello')
    # def hello():
    #     return 'Hello, World!'

    return app




