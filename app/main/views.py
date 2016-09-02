#coding=utf-8
from flask import render_template,flash,url_for,redirect
from .forms import StudentForm
from ..models import Student,db
from . import main
import requests
import json




@main.route('/',methods=['GET','POST'])
def index():
    form = StudentForm()
    if form.validate_on_submit():
        if form.stu_id.data =='' or form.name.data =='' or form.qq.data =='':
            flash(u'请填写完整信息！！！')
            return redirect(url_for('main.index'))
        if form.stu_id.data < '1999999999':
            flash(u'学号加上20！！！')
            return redirect(url_for('main.index'))
        student = Student.query.filter_by(stu_id=form.stu_id.data).first()
        if student is  None:
            url = "http://www.jxnugo.com/api/is_jxnu_student"
            post_data = { 'student_id': form.stu_id.data }
            headers = {'content-type': 'application/json'}
            r = requests.post(url, data=json.dumps(post_data), headers=headers)
            if form.name.data == r.json()['student_name']:
                student = Student(stu_id=form.stu_id.data,name=form.name.data,qq=form.qq.data,stu_class=form.stu_class.data)
                flash(u'报名成功！！！')
                db.session.add(student)
            else:
                flash(u'所填姓名和学号不符！！！')
                redirect(url_for('main.index'))
        else:
            flash(u'你已经报过名了，请勿多次点击！！！')
        redirect(url_for('main.index'))
    return render_template('website.html',form=form)



