from flask import Flask
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.config import Config
from datetime import timedelta

# 加载 .env 文件中的配置信息
load_dotenv()

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)

jwt = JWTManager()
app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
hs = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES_HOURS'))
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=hs)
days = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES_DAYS'))
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=days)
jwt.init_app(app)

from app.api import bp
app.register_blueprint(bp, url_prefix='/')
from app.api import lg
app.register_blueprint(lg, url_prefix='/login')



