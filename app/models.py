from . import db
from . import login_manager
from flask_login import UserMixin,AnonymousUserMixin

@login_manager.user_loader
def user_loader(user_id):
    return Manager.query.get(int(user_id))

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.BigInteger, unique=True)
    name = db.Column(db.String(16))
    stu_class = db.Column(db.String(64))
    qq = db.Column(db.String(20))

    def __repr__(self):
        return '<student %r>' % self.name


class Manager(UserMixin, db.Model):
    __tablename__ = 'manager'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))

    def verify_password(self,password):
        return self.password == password


class AnonymousUser(AnonymousUserMixin):
    pass

login_manager.anonymous_user = AnonymousUser