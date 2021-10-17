from flask.globals import session
from . import api
from flask_restful import abort, Resource
from flask import jsonify,request,redirect,url_for,g,current_app
import pymysql
from .commonfunc import *
from app.models import Patients,User
import datetime
from app import db,myauth
from sqlalchemy import func,and_

class PatientInfos(Resource):
    """
    REST风格的对资源的增删改查，Patients对应数据库中的patients表
    """
    # def get(self):
    #     '''
    #     查询某条数据
    #     '''
    #     data=request.values
    #     try:
    #         id=data['id']
    #     except KeyError:
    #         return abort(400)
    #     patient=Patients.query.filter_by(id=id).first()
    #     if patient is None:
    #         return jsonify(isExist=False,msg='patient id not exist')
    #     else:
    #         patient_dict=serialize(patient)
    #         return jsonify(patient=patient_dict,isExist=True,msg='patient info has been sent successfully')
    
    def get(self):
        '''
        查询全部数据
        '''
        data=request.values
        try:
            userId=data['userId']
        except KeyError:
            return abort(400)
        user = User.query.fliter_by(id=userId).first()
        if user is None:
            return jsonify(isExist=False,msg='user id not exist')
        if user['is_admin'] is not None and user['is_admin'] == 1:
            patients = Patients.query.all()
        else:
            patients=Patients.query.filter_by(userId=userId).all()
        if patients is None:
            return jsonify(isExist=False,msg='patient id not exist')
        else:
            patient_dict=serialize(patients)
            return jsonify(patient=patient_dict,isExist=True,msg='patient info has been sent successfully')

    def post(self):
        """
        修改数据
        """
        try:
            patient=request.json['patient']
        except KeyError:
            return abort(400)
        id=patient['id']
        patient_=Patients.query.filter_by(id=id).first()
        if patient_ is not None:
            for key, value in patient.items():
                if key == 'id':
                    continue
                patient_.__setattr__(key, value)
            db.session.add(patient_)
            db.session.commit()
            return jsonify(isUpdate=True,msg='update resource success')
        else:
            return jsonify(isUpdate=False,msg='resource does not exist')
    def put(self):
        """
        添加单条数据
        """
        try:
            patient=request.json['patient']
        except KeyError:
            return abort(400)
        id=patient['id']
        patient_=Patients.query.filter_by(id=id).first()
        if patient_ is None:
            patient_=Patients(id=id)
            for key, value in patient.items():
                if key == 'id':
                    continue
                patient_.__setattr__(key, value)
            try:
                if session['username'] is not None:
                    patient_.__setattr__("userId",session['username'])
            except Exception:
                return jsonify(putstatus=False,msg='user not login')
            db.session.add(patient_)
            db.session.commit()
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
        patient=Patients.query.filter_by(id=id).first()
        if patient is None:
            return jsonify(isDeleted=False,msg='patient id doesnt exist')
        else:
            db.session.delete(patient)
            db.session.commit()
            return jsonify(isDeleted=True,msg='the patient has been deleted')

