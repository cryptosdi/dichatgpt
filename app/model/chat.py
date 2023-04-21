from datetime import datetime
from app import db


class DbChat(db.Model):
    __tablename__ = 'di_chat'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(20),  nullable=False)
    chat_name = db.Column(db.String(30), nullable=False)
    chat_id = db.Column(db.String(20),  nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    del_flag = db.Column(db.Integer)

    def save(userId, chatName, chatId):
        s_chat = DbChat(user_id=userId, chat_name=chatName,
                        chat_id=chatId, del_flag=0, create_time=datetime.now())
        db.session.add(s_chat)
        db.session.commit()

    def query(userId):
        q_chat = db.session.query(DbChat).filter_by(
            user_id=userId).order_by(DbChat.id.asc()).all()
        return q_chat

    def update(chatId, chatName):
        u_chat = db.session.query(DbChat).filter_by(
            chat_id=chatId).first()
        u_chat.chat_name = chatName
        db.session.commit()

    def delete(chatId):
        u_chat = db.session.query(DbChat).filter_by(
            chat_id=chatId).first()
        u_chat.del_flag = 1
        db.session.commit() 

    def __repr__(self):
        return '<user %r>' % self.chat_id
