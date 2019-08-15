from flask import Blueprint
from flask_restful import Api
# 配置auth蓝本，该蓝本下面的接口访问前缀统一为127.0.0.1:5000/auth/xxx
auth = Blueprint('auth', __name__, url_prefix='/auth')
auth_rest = Api(auth)  # 使用RESTful扩展实现REST风格的接口
from . import routes, errors
