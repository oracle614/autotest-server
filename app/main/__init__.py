#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 16:42
# @Author  : KelvinYe

from flask import Blueprint

main = Blueprint('main', __name__)

from . import forms, views, api
