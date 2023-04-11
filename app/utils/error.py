from flask_limiter.errors import RateLimitExceeded
from app import app
from app import jwt
from app.utils import jsonify_with_error
from app.service.api_res import ApiRes

@app.errorhandler(RateLimitExceeded)
def handle_limiter(e: RateLimitExceeded):
    return jsonify_with_error(ApiRes.LIMIT_API)

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify_with_error(ApiRes.EXPIRED_TOKEN)