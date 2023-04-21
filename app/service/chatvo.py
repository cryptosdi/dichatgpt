class Chatvo:
     def __init__(self, id=0, user_id="", chat_name="", chat_id=""):
        self.id = id
        self.user_id = user_id
        self.chat_name = chat_name
        self.chat_id = chat_id

     def to_json_obj(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "chat_name":self.chat_name,
            "chat_id":self.chat_id
        }