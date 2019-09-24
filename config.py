# TODO: 程序配置文件
# created by codelion
# create-time 24th Sept.


DB_USER = 'root'
DB_PASSWORD = '123456'
DB_HOST = 'localhost'
DB_DB = 'acarepro'

DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URL = 'mysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB