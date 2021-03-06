#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 16:49
# @Author  : KelvinYe


from flask import render_template, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.utils import redirect

from app.common.common import get_dirname_list
from app.main import main
from app.models import User
from config import config


# @main.route('/login', methods=['POST'])
# def login():
#     if form.validate_on_submit():
#         user = User.query.filter_by(loginName=form.loginName.data).first()
#         datax = request.form.to_dict()
#         usernamx = datax.get('username')
#         passwordx = datax.get('password')
#         if user is not None and user.verify_password(form.password.data):
#             login_user(user, form.remember_me.data)
#             return redirect(request.args.get('next') or url_for('main.index'))
#         flash('Invalid username or password.')
#     return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@main.route('/run')
@login_required
def run():
    workspace = config.get('jmeter').get('workspace')
    dirs = get_dirname_list(workspace)
    return render_template('run.html', dirs=dirs)
