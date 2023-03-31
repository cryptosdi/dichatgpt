from app import app
from flask import Flask, request

@app.route("/")
def index():
    return 'Hi, welcome~'

@app.route("/reg", methods=['POST'])
def reg():
    user_name = request.json.get('un')
    password = request.json.get('pw')
    return 'ok'