# !/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME : 2019/3/21 16:39
# @Author :garyhost
# @File :app.py
import flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_migrate import Migrate

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    app = flask.Flask(__name__)
    bootstrap.init_app(app)
    db.init_app(app)
    migrate = Migrate(db=db)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # 注册路由

    # 错误处理

    return app