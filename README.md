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
	    BABEL_DEFAULT_LOCALE = 'zh_CN'
	    QINIU_ACCESS_KEY = '*****************' # 七牛云access key
	    QIUNU_SECRETE_KEY = '**********' # 七牛云secrete key
	    UPLOAD_DOMAIN = '**********' # 七牛云上传domain
	    WTF_CSRF_CHECK_DEFAULT = False

	class CacheConfig:
	    CACHE_TYPE = 'redis'
	    CACHE_REDIS_HOST = 'localhost'
	    CACHE_REDIS_PORT =  6379
	    CACHE_REDIS_DB = ''
	    CACHE_REDIS_PASSWORD = ''



	class DevelopmentConfig(CacheConfig,Config):
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