from flask_restful import abort, Resource
from flask import jsonify, request, g, current_app, render_template,make_response
from . import main
from app import db, auth
# from app.models import Factor
import datetime


@main.route('/', methods=['get', 'post'])
def index():
    '''
    设置web主页，在没有前端需求时也可以不设置，做纯REST api服务器
    index.html放在dist目录下
    '''
    resp = make_response(render_template("index.html"))
    return resp

@main.route('/test', methods=['get','POST'])
def test():
    return 'hello world!'
