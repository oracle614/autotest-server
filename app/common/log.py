#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 11:49
# @Author  : KelvinYe

import logging

from config import config


# %(name)s：             Logger的名字
# %(levelno)s：          数字形式的日志级别
# %(levelname)s：        文本形式的日志级别
# %(pathname)s：         调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s：         调用日志输出函数的模块的文件名
# %(module)s：           调用日志输出函数的模块名
# %(funcName)s：         调用日志输出函数的函数名
# %(lineno)d：           调用日志输出函数的语句所在的代码行
# %(created)f：          当前时间，用UNIX标准的表示时间的浮 点数表示
# %(relativeCreated)d：  输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s：          字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”
# %(thread)d：           线程ID（可能没有）
# %(threadName)s：       线程名（可能没有）
# %(process)d：          进程ID（可能没有）
# %(message)s：          用户输出的消息
def getlogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(config.get('log').get('level'))

    # fh = logging.FileHandler(config.get('log').get('name'))  # 用于写入日志文件
    ch = logging.StreamHandler()  # 用于输出到控制台

    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s.%(funcName)s - %(levelname)s - %(message)s')
    # fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 给logger添加handler
    # logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
