from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_admin import Admin
from flask_babelex import Babel
from flask_login import LoginManager

from config import config

db = SQLAlchemy()
csrf = CSRFProtect()
admin = Admin()
babel = Babel()
login_manager = LoginManager()

login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    csrf.init_app(app)
    admin.init_app(app)
    babel.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
