# -*- coding: utf-8 -*-
from flask import current_app, request, redirect, url_for
from flask_admin import BaseView, expose
from flask_admin import form
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user
from jinja2 import Markup
from wtforms.validators import DataRequired

from . import main
from .. import admin, db
from ..models import Student, Manager, PictureWall, file_path


class StudentView(ModelView):
    column_list = ('stu_id', 'name', 'stu_class', 'qq')
    column_labels = dict(stu_id=u"学号", name=u'姓名', stu_class=u'班级', qq=u"联系方式")
    can_export = True

    def __init__(self, session, **kwargs):
        super(StudentView, self).__init__(Student, session, **kwargs)

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('main.login'))


class ManagerView(ModelView):
    column_list = ('account', 'password')
    column_labels = dict(account=u"账号", password=u"密码")

    def __init__(self, session, **kwargs):
        super(ManagerView, self).__init__(Manager, session, **kwargs)

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('main.login'))


admin.add_view(StudentView(db.session, name=u'学生报名表'))
admin.add_view(ManagerView(db.session, name=u"管理员表"))


@main.before_app_request
def check_need_login():
    if str(request.url_rule)[1:6] == 'admin' and not current_user.is_authenticated:
        return  current_app.login_manager.unauthorized()


class ImageView(ModelView):
    column_list = ('pic_url', 'name', 'info', 'add_time')
    column_labels = dict(pic_url=u"图片", name=u'名字', info=u'说明', add_time=u"添加时间",)
    column_default_sort = ('add_time',)
    form_excluded_columns = ('remote_url',)
    form_edit_rules = ('name', 'info', 'add_time')  # 修改表单显示的字段
    column_editable_list = ('name', 'info', 'add_time')  # 可以ajax实时编辑的字段

    def __init__(self, session, **kwargs):
        super(ImageView, self).__init__(PictureWall, session, **kwargs)

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('main.login'))

    def _list_thumbnail(view, context, model, name):
        if model.remote_url:
            return Markup('<img src="%s">' % model.remote_url)

        return Markup('<img src="%s">' % url_for('static',
                                                 filename=form.thumbgen_filename(model.pic_url)))

    column_formatters = {
        'pic_url': _list_thumbnail
    }

    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    form_extra_fields = {
        'pic_url': form.ImageUploadField(u'图片',
                                         base_path=file_path,
                                         thumbnail_size=(100, 100, True),
                                         validators=[DataRequired()])
    }


admin.add_view(ImageView(db.session,name=u'图片墙'))


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect(url_for('main.index'))


admin.add_view(LogoutView(name=u'注销'))