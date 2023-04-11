import os
import json
from app.model import Dbmessage
from app.utils import logger
from app import app
from app.service import Message


class Opmessage:
    def __init__(self):
        return

    def save_message(self, user_id, role, content, reply_content):
        with app.app_context():
            self.save(user_id, role, content, reply_content)

    def save(self, user_id, role, content, reply_content):
        messages = [self.get_message(
            "user", content), self.get_message(role, reply_content)]
        Dbmessage.save(user_id, json.dumps(messages))

    def merge_history_message(self, user_id, role, content):
        with app.app_context():
            merge_his_messages = [self.get_message(
                'system', 'You are a helpful assistant.')]
            messages = Dbmessage.query(user_id, 3)
            if messages is None:
                merge_his_messages.append(self.get_message(role, content))
                return merge_his_messages
            messages = messages[::-1]
            for item in messages:
                j_item = json.loads(item.message)
                for m_item in j_item:
                    merge_his_messages.append(self.get_message(
                        m_item['role'], m_item['content']))
            merge_his_messages.append(self.get_message(role, content))
            return merge_his_messages

    def query_history_message(user_id, count):
        history_messages = []
        messages = Dbmessage.query(user_id, count)
        for item in messages:
            merge_message = {"create_time": item.create_time.strftime(
                '%Y-%m-%d %H:%M:%S'), "messages": json.loads(item.message)}
            history_messages.append(merge_message)
        return history_messages

    def get_message(role, content):
        message_obj = Message(role, content)
        return message_obj.to_json_obj()
