from flask import Blueprint
bp = Blueprint('/', __name__)
lg = Blueprint('/login', __name__)
from app.api import web
from app.api import login