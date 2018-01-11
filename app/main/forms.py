#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 16:49
# @Author  : KelvinYe

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, DataRequired


class LoginForm(FlaskForm):
    loginName = StringField('LoginName', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField()
