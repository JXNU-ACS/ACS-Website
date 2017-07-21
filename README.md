# ACS-Website
the website of JXNU-ACS


# 环境准备
配置
config.py
	
	import os


	class Config:
	    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	    SQLALCHEMY_TRACK_MODIFICATIONS = True


	class DevelopmentConfig(Config):
	    DEBUG = True
	    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
	                              'mysql://root:passwd@localhost:3306/acs?charset=utf8'  # config your db url
	
	
	config = {
	    'default': DevelopmentConfig
	}


```
    pip install -r requirements.txt
    python manage.py runserver
```