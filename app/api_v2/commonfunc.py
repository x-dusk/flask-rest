
from sklearn.linear_model import (LinearRegression, Ridge, Lasso)
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm
import numpy
import pymysql
import pickle
import math
import numpy as np
import datetime
import time
import random
import copy
import pandas as pd
from sklearn import linear_model
from flask import current_app
# from app.models import Dailyprice,Factor,SFStatus,SpecialFactor,DailyTransport,Transport,PeriodAndType,Contract
from sqlalchemy.sql import func,and_,alias,label,desc
from app import db

def serialize(model):
    '''
    将数据库model转化为python字典
    '''
    from sqlalchemy.orm import class_mapper
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)
