# coding=utf-8
#! /usr/bin/env python
import os
from app import create_app,db
from app.models import User

#如果已经定义了环境变量FLASK——CONFIG，则从中读取配置名，否则使用默认配置
app=create_app(os.getenv('FLASK_CONFIG') or 'dev') 

@app.shell_context_processor
def make_shell_context():
    """
    集成python shell，除了默认导入app,该shell上下文处理器还会导入数据库实例db和模型User,避免重复导入
    :flask shell
    >>>app
    <Flask 'app'>
    >>>User
    <class 'app.models.User'>
    """
    return dict(db=db,User=User)

if __name__ == "__main__":
    '''
    启动项目的方式之一：python3 server.py(不建议在生产环境下使用此方式)
    host为0.0.0.0可以让所有ip访问，默认127.0.0.1
    port默认5000
    '''
    app.run(host='127.0.0.1',port=5000,debug=True)