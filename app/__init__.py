from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)

from app.api import bp
app.register_blueprint(bp, url_prefix='/')
from app.api import lg
app.register_blueprint(lg, url_prefix='/login')



