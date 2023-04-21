from flask import Flask, request, Response
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from app.utils import jsonify_with_data
from app.utils import jsonify_with_error
from app.api import ct
from app import limiter
from app.service import ApiRes
from app.service import Gpt
from app.utils import logger
from app.service import Opmessage
from app.service import Opchat


@ct.route('/chat', methods=['POST'])
@jwt_required()
@limiter.limit("5/minute")
def chat():
    user_id = get_jwt_identity()
    content = request.json.get('content')
    logger.info('[gpt] user_id=%s, content=%s', user_id, content)
    if len(content) == 0:
        return jsonify_with_error(ApiRes.CONTENT_EMPTY)
    try:
        rsp = Gpt.ask_chat_stream_gpt(user_id, content)
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
    messages = Opmessage.query_history_message(user_id, count)
    return jsonify_with_data(ApiRes.OK, messages=messages[::-1])


@ct.route('/get/chats', methods=['POST'])
@jwt_required()
@limiter.limit("5/minute")
def getChats():
    user_id = get_jwt_identity()
    logger.info('[gpt] get chats user_id=%s', user_id)
    chats = Opchat.query_chat(user_id)
    if chats is None:
        return jsonify_with_data(ApiRes.OK, chats=[])
    return jsonify_with_data(ApiRes.OK, chats=chats)


@ct.route('/add/chat', methods=['POST'])
@jwt_required()
@limiter.limit("5/minute")
def addChats():
    user_id = get_jwt_identity()
    chat_name = request.json.get('chat_name')
    if chat_name is None:
        chat_name = 'NewChat'
    logger.info('[gpt] add chats user_id=%s', user_id)
    chat_id = Opchat.save_chat(user_id, chat_name)
    return jsonify_with_data(ApiRes.OK, chat_id=chat_id)
