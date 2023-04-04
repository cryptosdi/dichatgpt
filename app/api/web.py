from flask import Flask, request
from app.api import bp
from app.model.user import user
from app.utils import jsonify_with_data
from app.utils import jsonify_with_error
from app.api.api_res import ApiRes
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from app.utils import logger

@bp.route("/")
@jwt_required()
def index():
    user_id = get_jwt_identity()
    logger.info("[gpt] index user_id=%s", user_id)
    return jsonify_with_data(ApiRes.OK, user_id=user_id)

