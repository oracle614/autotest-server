#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 15:20
# @Author  : KelvinYe

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'
login_manager.login_message = '请先登录'
login_manager.login_message_category = 'info'


def create_app():
    db_info = config.get('db')
    username = db_info.get('username')
    password = db_info.get('password')
    host = db_info.get('host')
    port = db_info.get('port')
    databasename = db_info.get('databasename')
    dburi = rf'postgresql://{username}:{password}@{host}:{port}/{databasename}'

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = dburi
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 密钥，CSRF（跨站请求伪造）保护，通过os.urandom(24)生成
    app.config['SECRET_KEY'] = config.get('SECRET_KEY')

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
