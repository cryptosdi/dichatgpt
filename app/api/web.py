from flask import Flask, request
from app.api import bp
from app.user import user
from app.utils import generate_random_string

@bp.route("/")
def index():
    return 'Hi, welcome~suc'

@bp.route("/reg", methods=['POST'])
def reg():
    user_name = request.json.get('un')
    password = request.json.get('pw')
    user.save(generate_random_string(6), user_name, password)
    return 'ok'