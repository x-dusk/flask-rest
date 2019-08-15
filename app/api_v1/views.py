from . import api
from flask_restful import abort, Resource
from flask import jsonify,request,redirect,url_for,g,current_app
import pymysql
from .commonfunc import *
from app.models import Attr
import datetime
from app import db,myauth
from sqlalchemy import func,and_

class Attrs(Resource):
    """
    REST风格的对资源的增删改查，Attrs对应数据库中的attr表
    """
    def get(self):
        '''
        查询某条数据
        '''
        data=request.values
        try:
            id=data['id']
        except KeyError:
            return abort(400)
        attr=Attr.query.filter_by(id=id).first()
        if attr is None:
            return jsonify(isExist=False,msg='attr of the id doesnt exist')
        else:
            attr_dict=serialize(attr)
            return jsonify(attr=attr_dict,isExist=True,msg='attr has been sent successfully')
    def post(self):
        """
        修改数据
        """
        try:
            attr=request.json['attr']
        except KeyError:
            return abort(400)
        id=attr['id']
        attr_=Attr.query.filter_by(id=id).first()
        if attr_ is not None:
            for key, value in attr.items():
                if key == 'id':
                    continue
                attr_.__setattr__(key, value)
            db.session.add(attr_)
            db.session.commit()
            return jsonify(isUpdate=True,msg='update resource success')
        else:
            return jsonify(isUpdate=False,msg='resource does not exist')
    def put(self):
        """
        添加单条数据
        """
        try:
            attr=request.json['attr']
        except KeyError:
            return abort(400)
        id=attr['id']
        attr_=Attr.query.filter_by(id=id).first()
        if attr_ is None:
            attr_=Attr(id=id)
            for key, value in attr.items():
                if key == 'id':
                    continue
                attr_.__setattr__(key, value)
            db.session.add(attr_)
            db.session.commit()
            # attr_=Attr(a=attr['a'],b=attr['b'],c=attr['c'],d=attr['d'],e=attr['e'],y=attr['y'])
            return jsonify(putstatus=True,msg='add resource success')
        else:
            return jsonify(putstatus=False,msg='resource has existed')
    def delete(self):
        '''
        删除单条数据
        '''
        try:
            id=request.values['id']
        except KeyError:
            return abort(400)
        attr=Attr.query.filter_by(id=id).first()
        if attr is None:
            return jsonify(isDeleted=False,msg='attr of the id doesnt exist')
        else:
            db.session.delete(attr)
            db.session.commit()
            return jsonify(isDeleted=True,msg='the attr has been deleted')

