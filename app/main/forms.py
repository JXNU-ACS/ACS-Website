# coding=utf-8
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length
from app.models import Student


class StudentForm(Form):
    stuid = StringField(u'学号', validators=[Required(), Length(0,12)])
    name = StringField(u'姓名', validators=[Required(), Length(1,10)])
    banji = StringField(u'班级', validators=[Required()])
    qq = StringField('QQ')
    submit = SubmitField(u'确认')