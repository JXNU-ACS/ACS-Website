#coding=utf-8
from flask_wtf import Form
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import Required,Length
from ..models import Student
HOUR_CHOICES = [('0',u'计科师范班'),('1',u'计科1班'), ('2', u'计科2班'),('2',u'网工1班'),('3',u'网工2班'),('4',u'软件学院'),('5',u'其他院系')]
class StudentForm(Form):
    stu_id = StringField(u'学号')
    name = StringField(u'姓名')
    stu_class = SelectField(u'班级',choices=HOUR_CHOICES)
    qq = StringField('QQ')
    submit = SubmitField(u'确认')



