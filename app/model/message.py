from datetime import datetime
from app import db


class message(db.Model):
    __tablename__ = 'di_message'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(20), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)

    def save(userId, msg):
        s_message = message(user_id=userId, message=msg)
        db.session.add(s_message)
        db.session.commit()

    def query(userId, count):
        q_message = db.session.query(message).filter_by(
            user_id=userId).order_by(message.id.desc()).limit(count)
        return q_message

    def __repr__(self):
        return '<user %r>' % self.user_id
