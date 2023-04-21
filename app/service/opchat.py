from app.model import DbChat
from app.utils import logger, generate_random_string


class Opchat:
    def __init__(self):
        return

    def save_chat(user_id, chat_name):
        chat_id = user_id + generate_random_string(4)
        DbChat.save(user_id, chat_name, chat_id)
        return chat_id

    def query_chat(user_id):
        return DbChat.query(user_id)

    def update_name(chat_id, chat_name):
        DbChat.update(chat_id, chat_name)

    def delete(chat_id):
        DbChat.delete(chat_id)
