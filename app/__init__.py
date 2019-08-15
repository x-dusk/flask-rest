# coding=utf-8
from flask import Flask, render_template, make_response
from config import config  # 导入配置文件
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth  # 使用HTTP基本认证方式

# 数据库迁移框架，能跟踪数据库模式的变化，model变化，然后以增量方式将变化应用到数据库中，并提供回到历史版本的功能
from flask_migrate import Migrate
from flask_cors import CORS  # 解决前后端开发过程中跨域问题的扩展

myauth = HTTPBasicAuth()
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    '''
    创建应用实例的地方,初始化相关扩展
    '''
    app = Flask(__name__, static_folder="./dist/static",
                template_folder="./dist")  # 设置前端静态资源的目录
    app.config.from_object(config[config_name])  # 加载配置
    config[config_name].init_app(app)  # 初始化配置类
    CORS(app)  # 初始化CORS
    db.init_app(app)  # 初始化SQLAlchemy
    migrate.init_app(app, db)  # 初始化数据库迁移框架

    # 注册main蓝本(blueprint),相当于加载一个子系统
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # 注册api_v1蓝本
    from .api_v1 import api as apiv1_blueprint
    app.register_blueprint(apiv1_blueprint)
    # 注册api_v2蓝本
    from .api_v2 import api as apiv2_blueprint
    app.register_blueprint(apiv2_blueprint)
    # 注册auth蓝本
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
