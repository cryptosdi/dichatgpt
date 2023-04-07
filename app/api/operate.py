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


def merge_history_message(user_id, role, content):
    with app.app_context():
        merge_his_messages = [
            {"role": "system", "content": "You are a helpful assistant."}]
        messages = message.query(user_id, 3)
        if messages is None:
            merge_his_messages.append({"role": role, "content": content})
            return merge_his_messages
        for item in messages:
            j_item = json.loads(item.message)[0]
            merge_his_messages.insert(1,
                                      {"role": j_item['role'], "content": j_item['content']})
        merge_his_messages.append({"role": role, "content": content})
        return merge_his_messages


def query_history_message(user_id, count):
    history_messages = []
    messages = message.query(user_id, count)
    for item in messages:
        history_messages.append(json.loads(item.message))
    return history_messages
