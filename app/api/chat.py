from flask import Flask, request, Response
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from app.utils import jsonify_with_data
from app.utils import jsonify_with_error
from app.api import ct
from app import limiter
from app.api.api_res import ApiRes
from app.api.gpt import ask_chat_stream_gpt, ask_gpt
from app.utils import logger
from app.api.operate import query_history_message


@ct.route('/ask', methods=['POST'])
@jwt_required()
@limiter.limit("5/minute")
def chat():
    user_id = get_jwt_identity()
    content = request.json.get('content')
    logger.info('[gpt] user_id=%s, content=%s', user_id, content)
    if len(content) == 0:
        return jsonify_with_error(ApiRes.CONTENT_EMPTY)
    try:
        rsp = ask_chat_stream_gpt(user_id, content)
    except Exception as e:
        return jsonify_with_error(ApiRes.SERVICE_ERROR)
    return Response(rsp, mimetype='text/event-stream')


@ct.route('/get', methods=['POST'])
@jwt_required()
@limiter.limit("5/minute")
def get():
    user_id = get_jwt_identity()
    count = request.json.get('count')
    if count is None:
        count = 3
    logger.info('[gpt] get messages user_id=%s', user_id)
    messages = query_history_message(user_id, count)
    return jsonify_with_data(ApiRes.OK, messages=messages[::-1])
