# coding=utf-8
from flask import render_template,flash,url_for,redirect
from app.main.forms import StudentForm
from app.models import Student, db
from app.main import main


@main.route('/', methods=['GET','POST'])
def index():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student.query.filter_by(stuid=form.stuid.data).first()
        if student is None:
            student = Student(stuid=form.stuid.data, name=form.name.data,qq=form.qq.data,banji=form.banji.data)
            db.session.add(student)
            flash(u'报名成功！！！')
        else:
            flash(u'你已经报过名了！！！')
        redirect(url_for('main.index'))
    return render_template('index.html', form=form)



