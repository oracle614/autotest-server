#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/6/1 10:09
# @Author  : yekaiwen
import os
from enum import Enum
from subprocess import Popen, PIPE, STDOUT
from flask_socketio import emit

from app.common.log import getlogger
from app import socket

logger = getlogger(__name__)


class Jmeter:
    def __init__(self, env, reportname, jmeterpath):
        self.command = rf'{jmeterpath}\jmeter -JpropFileName="{env}" -JreportName="{reportname}" -JisAppend="true" -n -t '

    def execute(self, jmxabspath):
        command = self.command + jmxabspath
        logger.debug(f'Commond: 【{command}】')
        popen = Popen(command, stdout=PIPE, stderr=STDOUT, shell=True, universal_newlines=True)
        while popen.poll() is None:  # 检查子进程是否结束
            line = popen.stdout.readline()
            line = line.strip()
            if line:
                logger.debug(line)
                emit('realtimelog', line)
        if popen.returncode == 0:
            logger.debug('Command execution success')
        else:
            logger.debug('Command execution failed')
        emit('disconnect')


class Env(Enum):
    testNewSH = r'../env_properties/envTestNewSH.properties'
    testNewGZ = r'../env_properties/envTestNewGZ.properties'

    @staticmethod
    def get_testenv(env_name):
        """
        根据测试环境简称获取配置文件相对路径
        """
        env_value = ''
        for env in Env:
            if env_name == env.name:
                env_value = env.value
        return env_value
