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
