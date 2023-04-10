from flask import Blueprint
bp = Blueprint('/', __name__)
lg = Blueprint('/login', __name__)
ct = Blueprint('/gpt', __name__) 
from app.api import web
from app.api import login
from app.api import chat