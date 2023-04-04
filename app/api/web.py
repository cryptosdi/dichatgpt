from flask import Flask, request
from app.api import bp
from app.model.user import user
from app.utils import generate_random_string
from app.utils import jsonify_with_data
from app.utils import jsonify_with_error
from app.api.api_res import ApiRes
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token

@bp.route("/")
@jwt_required()
def index():
    user_id = get_jwt_identity()
    return jsonify_with_data(ApiRes.OK, user_id=user_id)


@bp.route("/reg", methods=['POST'])
def reg():
    user_name = request.json.get('un').strip()
    if len(user_name) == 0:
       return jsonify_with_error(ApiRes.BAD_USER_NAME)  
    password = request.json.get('pw').strip()
    if len(password) == 0:
       return jsonify_with_error(ApiRes.BAD_USER_PASSWORD)  
    usr = user.query(user_name)
    if usr is not None:
        return jsonify_with_error(ApiRes.BAD_REQUEST) 
    user_id = generate_random_string(6)
    user.save(user_id, user_name, password)
    access_token = create_access_token(identity=user_id)
    return jsonify_with_data(ApiRes.OK, access_token=access_token)