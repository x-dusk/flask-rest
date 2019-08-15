from flask import Blueprint
# 配置main蓝本，该蓝本下面的接口访问前缀统一为127.0.0.1:5000/main/xxx
main = Blueprint('main', __name__, url_prefix='/')
from . import views, errors
