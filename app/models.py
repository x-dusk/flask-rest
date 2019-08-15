# coding=utf-8
from flask import current_app
from app import db
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
'''
定义数据模型，与数据库表一一对应
'''
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
    def generate_auth_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id}).decode('utf-8')
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Attr(db.Model):
    __tablename__ = 'attr'
    id = db.Column(db.Integer, primary_key=True)
    a = db.Column(db.Float, comment='特征A')
    b = db.Column(db.Float, comment='特征B')
    c = db.Column(db.Float, comment='特征C')
    d = db.Column(db.Float, comment='特征D')
    e = db.Column(db.Float, comment='特征E')
    y = db.Column(db.Float, comment='目标Y')

    def __repr__(self):
        return '<Attr {}>'.format(self.id)