import os
import MySQLdb

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DUBUG =True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')  or \
    'mysql://root:123@localhost:3306/acsk?charset=utf8'
config = {
	
	'default':DevelopmentConfig
}