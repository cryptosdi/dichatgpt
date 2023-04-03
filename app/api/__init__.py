from flask import Blueprint
bp = Blueprint('/', __name__)
from app.api import web