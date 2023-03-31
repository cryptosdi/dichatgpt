
import os
from urllib.parse import quote_plus

class Config(object):
    user = os.getenv('DB_ACCOUNT')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATA_NAME')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@127.0.0.1:3306/%s' % (
        user, password, database)
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False