from flask import Flask, request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from app.utils import jsonify_with_data
from app.utils import jsonify_with_error
from app.api import ct
from app import limiter
from app.api.api_res import ApiRes


@ct.route('/send', methods=['POST'])
@jwt_required()
@limiter.limit("5/minute")
def chat():
    return jsonify_with_data(ApiRes.OK)
