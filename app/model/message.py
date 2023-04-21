from datetime import datetime
from app import db


class Dbmessage(db.Model):
    __tablename__ = 'di_message'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    chat_id = db.Column(db.String(20))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)

    def save(userId, msg, chatId):
        s_message = Dbmessage(user_id=userId, message=msg, chat_id = chatId)
        db.session.add(s_message)
        db.session.commit()

    def query(userId, count):
        q_message = db.session.query(Dbmessage).filter_by(
            user_id=userId).order_by(Dbmessage.id.desc()).limit(count)
        return q_message

    def query(userId, chatId, count):
        q_message = db.session.query(Dbmessage).filter_by(
            user_id=userId, chat_id = chatId).order_by(Dbmessage.id.desc()).limit(count)
        return q_message

    def __repr__(self):
        return '<user %r>' % self.user_id
