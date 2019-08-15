from . import auth
from app import myauth
from flask import jsonify, make_response


@myauth.error_handler
def old_token():
    '''
    token过期或错误的错误处理，只在该蓝本下生效
    '''
    response = jsonify(code=401, msg='you not login or you old token')
    response.status_code = 200
    return response
