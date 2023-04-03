from flask import Flask, request
from app.api import bp
from app.user import user
from app.utils import generate_random_string
from app.utils import jsonify_with_data
from app.utils import jsonify_with_error
from app.api.api_res import ApiRes

@bp.route("/")
def index():
    return jsonify_with_data(ApiRes.OK)

@bp.route("/reg", methods=['POST'])
def reg():
    user_name = request.json.get('un')
    password = request.json.get('pw')
    usr = user.query(user_name)
    if usr is not None:
        return jsonify_with_data(ApiRes.BAD_REQUEST) 
    user.save(generate_random_string(6), user_name, password)
    return jsonify_with_data(ApiRes.OK)