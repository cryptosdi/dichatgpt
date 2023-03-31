from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.api import bp

app = Flask(__name__)
app.register_blueprint(bp)

app.config.from_object(Config)
db = SQLAlchemy(app)

