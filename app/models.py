from . import db


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.BigInteger, unique=True)
    name = db.Column(db.String(16))
    stu_class = db.Column(db.String(64))
    qq = db.Column(db.String(20))

    def __repr__(self):
        return '<student %r>' % self.name
