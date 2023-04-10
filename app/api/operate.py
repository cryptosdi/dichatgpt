import os
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
        messages = messages[::-1]
        for item in messages:
            j_item = json.loads(item.message)
            for m_item in j_item:
                merge_his_messages.append(
                    {"role": m_item['role'], "content": m_item['content']})
        merge_his_messages.append({"role": role, "content": content})
        return merge_his_messages


def query_history_message(user_id, count):
    history_messages = []
    messages = message.query(user_id, count)
    for item in messages:
        merge_message = {"create_time": item.create_time.strftime(
            '%Y-%m-%d %H:%M:%S'), "messages": json.loads(item.message)}
        history_messages.append(merge_message)
    return history_messages
