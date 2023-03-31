from flask import Flask, request
from app.api import bp

@bp.route("/")
def index():
    return 'Hi, welcome~'

@bp.route("/reg", methods=['POST'])
def reg():
    user_name = request.json.get('un')
    password = request.json.get('pw')
    return 'ok'