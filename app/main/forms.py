#coding=utf-8
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required,Length
from ..models import Student

class StudentForm(Form):
    stu_id = StringField(u'学号',validators=[Required(),Length(0,12)])
    name = StringField(u'姓名',validators=[Required(),Length(1,10)])
    stu_class = StringField(u'班级',validators=[Required()])
    qq = StringField('QQ')
    submit = SubmitField(u'确认')