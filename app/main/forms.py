#coding=utf-8
from flask_wtf import Form
from wtforms import StringField,SubmitField,SelectField,IntegerField
from wtforms.validators import Required,Length
from ..models import Student
HOUR_CHOICES = [('0',u'计科师范1班'),('1',u'计科师范2班'),('2', u'计科师范3班'),('3',u'计科1班'), ('4', u'计科2班'),('5',u'网工1班'),('6',u'网工2班'),('7',u'物联网1班'),('8',u'物联网2班'),('9',u'软件学院'),('10',u'其他院系')]
class StudentForm(Form):
    stu_id = IntegerField(u'学号')
    name = StringField(u'姓名')
    stu_class = SelectField(u'班级',choices=HOUR_CHOICES)
    qq = StringField('QQ')
    submit = SubmitField(u'确认')



