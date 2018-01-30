#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/1/30 17:44
# @Author  : KelvinYe
from app import socketio, emit


@socketio.on('connect', namespace='/jmeterunrealtimelog')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})


@socketio.on('my event', namespace='/jmeterunrealtimelog')
def test_message(message):
    emit('my response', {'data': message['data'], 'count': 2})
