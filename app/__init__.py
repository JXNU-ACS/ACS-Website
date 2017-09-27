# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_admin import Admin, AdminIndexView
from flask_babelex import Babel
from flask_login import LoginManager
from flask_cache import Cache

from config import config

db = SQLAlchemy()
csrf = CSRFProtect()
admin = Admin()
babel = Babel()
cache = Cache()
login_manager = LoginManager()

login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    csrf.init_app(app)
    admin.init_app(app, index_view=AdminIndexView(name=u'首页', template='admin.html', url='/admin'))
    babel.init_app(app)
    login_manager.init_app(app)
    cache.init_app(app)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
