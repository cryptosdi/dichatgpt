from flask import Flask, request
from app.api import bp
from app.model.user import user
from app.utils import jsonify_with_data
from app.utils import jsonify_with_error
from app.api.api_res import ApiRes
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


@bp.route("/")
@jwt_required()
def index():
    user_id = get_jwt_identity()
    return jsonify_with_data(ApiRes.OK, user_id=user_id)

