Flask搭建的RESTful API服务器，使用包和模块，结构清晰，可在此基础上开发大型应用

export FLASK_APP='server.py'

python3 -m flask db init
python3 -m flask db migrate
python3 -m flask db upgrade
python3 -m flask db downgrade
