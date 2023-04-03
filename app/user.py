from datetime import datetime
from app import db
class user(db.Model):
    __tablename__ = 'di_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(20), unique=True, nullable=False)
    user_name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=False, nullable=False)
    del_flag = db.Column(db.Integer)
    create_time=db.Column(db.DateTime, default=datetime.utcnow)
    update_time=db.Column(db.DateTime, default=datetime.utcnow)

    def save(userId, userName, pw):
        s_user = user(user_id=userId, user_name=userName, password=pw,
                 del_flag=0, create_time=datetime.now(), update_time=datetime.now())
        db.session.add(s_user)
        db.session.commit()
    
    def query(userName):
        q_user = db.session.query(user).filter_by(user_name=userName).first()
        return q_user


    def __repr__(self):
        return '<user %r>' % self.username