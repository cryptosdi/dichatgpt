from flask import Flask, redirect, url_for
from app.api import bp
from app.utils import jsonify_with_data
from app.utils import jsonify_with_error
from app.service import ApiRes
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from app import limiter
import time

@bp.route("/")
@jwt_required(optional=True)
@limiter.limit("5/minute")
def index():
    #user_id = get_jwt_identity()
    return redirect('/home')
    #return Response(generate_text(), mimetype='application/octet-stream')
def generate_text():
    yield "Hello "
    time.sleep(1)
    yield "cryptodi!"
    time.sleep(1)
    yield " This is a stream response."
    time.sleep(1)
    yield "ok"

