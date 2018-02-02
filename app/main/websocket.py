#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 11:07
# @Author  : KelvinYe
import time

import os
from flask_socketio import emit
from app import socket
from app.common.jmeter import Env, Jmeter
from app.common.log import getlogger
from config import config

logger = getlogger(__name__)


@socket.on('connect', namespace='/jmeter')
def connect():
    logger.debug('connect')


@socket.on('disconnect', namespace='/jmeter')
def disconnect():
    logger.debug('disconnect')


@socket.on('sendtest', namespace='/jmeter')
def send(request):
    logger.debug(str(request))
    for i in range(10):
        logger.debug(i)
        emit('send-clinet', 'line')
    emit('disconnect')


@socket.on('run', namespace='/jmeter')
def runjmeter(request):
    env = Env.get_testenv(request['env'])
    script_list = request['scriptList']
    jmeterbin = config.get('jmeter').get('jmeterbin')
    currenttime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    reportname = rf'../htmlreport/{currenttime}.html'
    logger.debug(f'env={env}')
    logger.debug(f'scriptList={script_list}')
    logger.debug(f'reportname={reportname}')

    # os.chdir(jmeterbin)  # 设置脚本执行路径为jmeter/bin

    # jmeter = Jmeter(env, reportname, jmeterbin)
    # for script in script_list:
    #     jmeter.execute(script)
