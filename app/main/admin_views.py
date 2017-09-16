# -*- coding: utf-8 -*-
from flask import current_app, request
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from . import main
from .. import admin, db
from ..models import Student, Manager


class StudentView(ModelView):
    column_list = ('stu_id', 'name', 'stu_class', 'qq')
    column_labels = dict(stu_id=u"学号", name=u'姓名', stu_class=u'班级', qq=u"联系方式")

    def __init__(self, session, **kwargs):
        super(StudentView, self).__init__(Student, session, **kwargs)


class ManagerView(ModelView):
    column_list = ('account', 'password')
    column_labels = dict(account=u"账号", password=u"密码")

    def __init__(self, session, **kwargs):
        super(ManagerView, self).__init__(Manager, session, **kwargs)


admin.add_view(StudentView(db.session, name=u'学生报名表'))
admin.add_view(ManagerView(db.session, name=u"管理员表"))

@main.before_app_request
def check_need_login():
    if request.endpoint[:5] == 'admin' and not current_user.is_authenticated:
        print request.endpoint
        return current_app.login_manager.unauthorized()