#encoding:utf-8
import os


DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'mycms'


# PERMANENT_SESSION_LIFETIME =

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

CMS_USER_ID = '5'
FRONT_USER_ID = 'xxxxasfasfacxhgf'



# 邮箱
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')
MAIL_SERVER = os.environ.get('MAIL_SERVER', "smtp.qq.com")
MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')




SECRET_KEY = '123'

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False


START = 0
PERPAGE = 10

Album_PERPAGE = 10


CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'

# aliyun oss
ALIYUN_OSS_ID = os.environ.get('ALIYUN_OSS_ID')
ALIYUN_OSS_SECRET = os.environ.get('ALIYUN_OSS_SECRET')
URL_PREFIX = 'https://flask-cms.oss-cn-hangzhou.aliyuncs.com/'# 外网访问
