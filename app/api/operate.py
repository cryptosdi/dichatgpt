import asyncio
import json
from app.model import message
from app.utils import logger
from app import app


def save_message(user_id, role, content, reply_content):
    with app.app_context():
        save(user_id, role, content, reply_content)


def save(user_id, role, content, reply_content):
    messages = [{"role": "user", "content": content},
                {"role": role, "content": reply_content}]
    message.save(user_id, json.dumps(messages))
    logger.info('[gpt] save message')

def merge_history_message(user_id, content):
    messages =  message.query(user_id, 3)
    merge_his_messages = [{"role": "user", "content": content}]
    for item in messages:
        merge_his_messages.append(json.loads(item.message))
    return merge_his_messages

def query_history_message(user_id, count):
    history_messages = []
    messages =  message.query(user_id, count) 
    for item in messages:
        history_messages.append(json.loads(item.message))
    return history_messages