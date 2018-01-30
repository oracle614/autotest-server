#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 15:20
# @Author  : KelvinYe
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import *
from flask_socketio import SocketIO, emit

from config import config

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'
login_manager.login_message = '请先登录'
login_manager.login_message_category = 'info'

socketio = SocketIO()


def create_app():
    sqlite_path = config.get('db').get('path')
    dbname = config.get('db').get('name')
    dburi = rf'sqlite:///{sqlite_path}/{dbname}'

    app = Flask(__name__)
    CORS(app, supports_credentials=True)  # 跨域解决方案
    app.config['SQLALCHEMY_DATABASE_URI'] = dburi
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = config.get('SECRET_KEY')

    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
