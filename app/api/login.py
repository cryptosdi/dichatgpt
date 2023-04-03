from flask import Flask, request
from app.api import lg
from app.model.user import user
from app.utils import jsonify_with_data
from app.utils import jsonify_with_error
from app.api.api_res import ApiRes


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
    return jsonify_with_data(ApiRes.OK)