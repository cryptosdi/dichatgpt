
import os
import sqlalchemy as sa
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    user = os.getenv('DB_ACCOUNT')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATA_NAME')
    connection_url = sa.engine.URL.create(
        drivername="mysql+pymysql",
        username=user,
        password=password,
        host="127.0.0.1",
        database=database,
    )
    SQLALCHEMY_DATABASE_URI = connection_url 
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
