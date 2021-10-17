# coding=utf-8
import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    '''
    开发、测试、生产要使用不同的配置，如数据库配置等，保证不会彼此影响
    基类Config中包含通用配置，各个子类分别配置专用配置
    注意，配置项变量都应大写
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'some secret key string'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    TRANSPORT_URL='http://www.test.com'
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABASE_URL') or \
        'mysql+pymysql://root:password@localhost:3306/data-dev'

class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI=os.environ.get('TEST_DATABASE_URL') or \
        'mysql+pymysql://root:password@localhost:3306/data-test'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:password.mysql@47.97.20.3:3306/patient'

config={
    'dev':DevelopmentConfig,
    'test':TestingConfig,
    'prod':ProductionConfig,
    'default':DevelopmentConfig
}
