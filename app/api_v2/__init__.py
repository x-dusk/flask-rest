from flask import Blueprint
from flask_restful import Api
api = Blueprint('api_v2', __name__, url_prefix='/api_v2')
apii = Api(api)
from . import routes, errors
