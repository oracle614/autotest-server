#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 15:24
# @Author  : KelvinYe

from configparser import ConfigParser

import os

# config = ConfigParser()
# config.read(os.path.abspath(os.path.dirname(__file__)) + r'\local.config')
#
#
# def getconfig(section, option):
#     return config.get(section, option)
#
#
# def getconfigint(section, option):
#     return config.getint(section, option)
PROJECT_ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

config = {
    'db':         {
        'path': PROJECT_ROOT_DIR,
        'name': 'database'

    },
    'jmeter':     {
        'jmeterhome': r'F:\Jmeter\apache-jmeter-3.1-interface',
        'jmeterbin':  r'F:\Jmeter\apache-jmeter-3.1-interface\bin',
        'workspace':  r'F:\Jmeter\works\inf'
    },
    'SECRET_KEY': b'\xaa\xe9\x06\xd3Oe\xfa-M\x93\xc5$\xe2\xf4\xd6\x99D\xafui\xc3H\x1eL',
    'log':        {
        'name':  os.path.join(PROJECT_ROOT_DIR, 'app.log'),
        'level': 'DEBUG'  # LogLevel: CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
    }
}
