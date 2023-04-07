from flask import Flask, request
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.config import Config
from datetime import timedelta
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import openai

# 加载 .env 文件中的配置信息
load_dotenv()

app = Flask(__name__)

limiter = Limiter(
    key_func=lambda: request.method + request.path,
    app=app, 
    default_limits=["200 per day", "2 per minute"])

app.config.from_object(Config)
db = SQLAlchemy(app)

jwt = JWTManager()
app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
hs = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES_HOURS'))
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=hs)
days = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES_DAYS'))
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=days)
jwt.init_app(app)

openai.api_key = os.getenv('OPENAI_API_KEY')

#设置本地代理
#os.environ['HTTP_PROXY'] = 'http://127.0.0.1:8001'        
#os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:8001'

from app.api import bp
app.register_blueprint(bp, url_prefix='/')
from app.api import lg
app.register_blueprint(lg, url_prefix='/login')
from app.api import ct
app.register_blueprint(ct, url_prefix='/chat')



