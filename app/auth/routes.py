from . import auth_rest
from .import views

auth_rest.add_resource(views.new_user, '/users')  # 添加用户
auth_rest.add_resource(views.get_user, '/users/<int:id>')  # 获取用户信息
auth_rest.add_resource(views.get_auth_token, '/token')  # 获取token
auth_rest.add_resource(views.login, '/login')  # 登录
auth_rest.add_resource(views.logout, '/logout')  # 注销
