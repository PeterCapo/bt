import os
from flask import Flask, Blueprint
from flask_restful import Api

from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config['development'])
    app.secret_key = os.getenv("SECRET_KEY")
    

    from .api import version1 as v1
    app.register_blueprint(v1)

    return app