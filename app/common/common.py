#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/1 17:38
# @Author  : KelvinYe
import json
import os

from config import config
from app.common.log import getlogger

logger = getlogger(__name__)


def get_script_abspath_list(rootdir):
    """
    返回 rootdir目录及子目录下所有的jmx脚本的绝对路径
    """
    jmxs = []
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if isjmx(file):
                jmxs.append(os.path.join(root, file))
    return jmxs


def get_abspath_by_scriptname(rootdir, scriptname):
    """
    搜索 rootdir目录及子目录下 scriptname脚本的绝对路径
    """
    abspath = ''
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if scriptname == file:
                abspath = os.path.join(root, file)
                break
    return abspath


def get_abspath_by_dirname(rootdir, dirname):
    """
    搜索 rootdir目录及子目录下 dirname目录的绝对路径
    """
    abspath = ''
    for root, dirs, files in os.walk(rootdir):
        for name in dirs:
            if dirname == name:
                abspath = os.path.join(root, name)
                break
    return abspath


def get_script_abspath_by_keyword(rootdir, keyword):
    """
    搜索 rootdir目录及子目录下 含有 keyword 脚本名的绝对路径
    """
    abspath = ''
    for root, dirs, files in os.walk(rootdir):
        for name in files:
            if keyword in name:
                abspath = os.path.join(root, name)
                break
    return abspath


def isjmx(filename):
    """
    判断文件名（入参含后缀）后缀是否为 .jmx
    """
    return os.path.splitext(filename)[-1] == ".jmx" if True else False


def get_dirname_list(rootdir):
    """
    返回 rootdir目录下所有目录名list
    """
    dirs = []
    for dirname in os.listdir(rootdir):
        if os.path.isdir(os.path.join(rootdir, dirname)):
            dirs.append(dirname)
    return dirs


def get_scriptname_list(rootdir):
    """
    返回 rootdir目录下所有script的list
    """
    scripts = []
    for filename in os.listdir(rootdir):
        fileabspath = os.path.join(rootdir, filename)
        if os.path.isfile(fileabspath) and isjmx(fileabspath):
            scripts.append(filename)
    return scripts


def get_script_tree(rootdir):
    """
    递归获取文件树数据，以json报文返回
    """
    response = []
    for name in listdir(rootdir):
        if name == 'csv':
            # 过滤csv文件
            continue
        dir_abspath = os.path.join(rootdir, name)
        if isjmx(name):
            name = name[:-4]
        child = None
        if os.path.isdir(dir_abspath):
            # 如果是文件夹则递归获取文件夹内容
            child_res = get_script_tree(dir_abspath)
            if child_res:
                # 如文件夹下有内容则返回list，无则为None
                child = child_res
        response.append(file_dto(name, child))
    return response


def file_dto(name=None, child=None):
    return {'name': name, 'child': child}


def listdir(dirpath):
    """
    返回指定目录下的所有文件和目录名
    """
    return os.listdir(dirpath)

# if __name__ == '__main__':
#     workspace = config.get('jmeter').get('workspace')
#     print(dirname_to_abspath(workspace, 'BindCardFacade'))
#     print(get_script_tree(workspace))
#     print(get_script_abspath_by_keyword(workspace, 'closeAgree'))
