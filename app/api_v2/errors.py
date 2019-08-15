from . import api
from flask import jsonify
@api.app_errorhandler(404)
def page_not_found(e):
    return jsonify(code=404, error='url error')
