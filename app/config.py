
import os
from urllib.parse import quote_plus
import sqlalchemy as sa
class Config(object):
    user = os.getenv('DB_ACCOUNT')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATA_NAME')
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@127.0.0.1:3306/%s' % (
    #    user, parPw, database)
    connection_url = sa.engine.URL.create(
        drivername="mysql+pymysql",
        username=user,
        password=password,
        host="127.0.0.1",
        database=database,
    )
    SQLALCHEMY_DATABASE_URI = connection_url 
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False