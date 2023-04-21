from app.model import DbChat
from app.utils import logger, generate_random_string
from app.service import Chatvo
import json

class Opchat:
    def __init__(self):
        return

    def save_chat(user_id, chat_name):
        chat_id = user_id + generate_random_string(4)
        DbChat.save(user_id, chat_name, chat_id)
        return chat_id

    def query_chat(user_id):
        q_chats = DbChat.query(user_id)
        chats = []
        for item in q_chats:
            chat = Chatvo(item.id, item.user_id, item.chat_name, item.chat_id)
            chats.append(chat.to_json_obj())
        return chats

    def update_name(chat_id, chat_name):
        DbChat.update(chat_id, chat_name)

    def delete(chat_id):
        DbChat.delete(chat_id)
