from flask import Flask, request
from app.api import lg
from app import jwt
from app.model.user import user
from app.utils import jsonify_with_data
from app.utils import jsonify_with_error
from app.api.api_res import ApiRes
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_refresh_token
from app.utils import generate_random_string
from app.utils import logger

@lg.route('', methods=['POST'])
def login():
    user_name = request.json.get('un').strip()
    if len(user_name) == 0:
       return jsonify_with_error(ApiRes.BAD_USER_NAME)  
    password = request.json.get('pw').strip()
    if len(password) == 0:
       return jsonify_with_error(ApiRes.BAD_USER_PASSWORD)
    usr = user.query(user_name)
    if usr is None:
        return jsonify_with_error(ApiRes.BAD_REQUEST) 
    if usr.password != password:
        return jsonify_with_error(ApiRes.ERROR_USER_PASSWORD)  
    access_token = create_access_token(identity=usr.user_id)
    refresh_token = create_refresh_token(identity=usr.user_id)
    return jsonify_with_data(ApiRes.OK, access_token=access_token, refresh_token=refresh_token)

@lg.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify_with_data(ApiRes.OK, access_token=access_token)


@lg.route("/reg", methods=['POST'])
def reg():
    user_name = request.json.get('un').strip()
    if len(user_name) == 0:
       return jsonify_with_error(ApiRes.BAD_USER_NAME)  
    password = request.json.get('pw').strip()
    if len(password) == 0:
       return jsonify_with_error(ApiRes.BAD_USER_PASSWORD)  
    logger.info('[gpt] reg user_name=%s, pw=%s', user_name, password)
    usr = user.query(user_name)
    if usr is not None:
        return jsonify_with_error(ApiRes.BAD_REQUEST) 
    user_id = generate_random_string(6)
    try:
        user.save(user_id, user_name, password)
    except Exception as e:
        logger.error('[gpt] reg exception=%s', e)
        return jsonify_with_error(ApiRes.NO_ACCESS) 
    access_token = create_access_token(identity=user_id)
    refresh_token = create_refresh_token(identity=user_id)
    return jsonify_with_data(ApiRes.OK, access_token=access_token, refresh_token=refresh_token)