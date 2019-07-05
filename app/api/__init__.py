from flask_restful import Api
from flask import Blueprint


from .views import Register, Simulate


version1 = Blueprint('api2', __name__, url_prefix='/api/v1')


api = Api(version1)


api.add_resource(Register, '/register')
api.add_resource(Simulate, '/simulate')