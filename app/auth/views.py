from flask_restful import abort, Resource
from flask import jsonify, request, g, current_app, session, redirect, render_template
from app import db, myauth
from app.models import User
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
import hashlib


@myauth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    print('token or username:', type(username_or_token), username_or_token)
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


class new_user(Resource):
    @myauth.login_required
    def post(self):
        username = request.json['username']
        password = request.json['password']
        if username is None or password is None:
            abort(400)  # missing arguments
        if User.query.filter_by(username=username).first() is not None:
            abort(400)  # existing user
        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify(username=user.username, success=True)


class get_user(Resource):
    def get(self, id):
        user = User.query.get(id)
        if not user:
            abort(400)
        return jsonify(username=user.username, role=['admin'])


class get_auth_token(Resource):
    @myauth.login_required
    def post(self):
        token = g.user.generate_auth_token(1200)
        return {'token': token.decode('ascii'), 'role': 'admin', 'duration': 300}


class login(Resource):
    def post(self):
        username = request.json['username']
        password = request.json['password']
        if username is None or password is None:
            abort(400)  # missing arguments
        if verify_password(username, password):
            session['username'] = username
            token = g.user.generate_auth_token(1200)
            return {'token': token, 'role': 'admin', 'duration': 1200}
        else:
            return {'err': 'login failed'}


class logout(Resource):
    def post(self):
        if 'username' in session:
            session.pop('username', None)
        return jsonify(msg='logout successfully')
