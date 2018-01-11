#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/1 17:38
# @Author  : KelvinYe
import os

from config import config


def get_script_list(rootdir):
    """
    返回目录及子目录下所有的jmx脚本的绝对路径
    """
    jmxs = []
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if isjmx(file):
                jmxs.append(os.path.join(root, file))
    return jmxs


def get_script_abspath(rootdir, scriptname):
    """
    返回目录及子目录下指定脚本的绝对路径
    """
    abspath = ''
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if scriptname == file:
                abspath = os.path.join(root, file)
                break
    return abspath


def get_dir_abspath(rootdir, dir_name):
    """
    返回目录及子目录下指定目录的绝对路径
    """
    abspath = ''
    for root, dirs, files in os.walk(rootdir):
        for d in dirs:
            if dir_name == d:
                abspath = os.path.join(root, d)
                break
    return abspath


def isjmx(filename):
    """
    根据文件名（入参含后缀）判断文件后缀是否为 .jmx
    """
    return os.path.splitext(filename)[-1] == ".jmx" if True else False


def get_dirname_list(path):
    """
    返回path目录下所有目录的list
    """
    dirs = []
    for dirname in os.listdir(path):
        if os.path.isdir(os.path.join(path, dirname)):
            dirs.append(dirname)
    return dirs


def get_scriptname_list(path):
    """
    返回path目录下所有script的list
    """
    scripts = []
    for filename in os.listdir(path):
        fileabspath = os.path.join(path, filename)
        if os.path.isfile(fileabspath) and isjmx(fileabspath):
            scripts.append(filename)
    return scripts


if __name__ == '__main__':
    workspace = config.get('jmeter').get('workspace')
    print(get_dir_abspath(workspace, 'BindCardFacade'))
