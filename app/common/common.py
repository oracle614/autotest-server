#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/1 17:38
# @Author  : KelvinYe
import json
import os

from config import config


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


def scriptname_to_abspath(rootdir, scriptname):
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


def dirname_to_abspath(rootdir, dir_name):
    """
    搜索 rootdir目录及子目录下 dir_name目录的绝对路径
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
    for dirname in listdir(rootdir):
        dir_abspath = os.path.join(rootdir, dirname)
        filetype = get_filetype(dir_abspath)
        child = None
        if os.path.isdir(dir_abspath):
            child = (get_script_tree(os.path.join(rootdir, dirname)))
        response.append(file_dto(dirname, filetype, child))
    return response


def file_dto(name=None, filetype=None, child=None):
    return {'name':     name,
            'filetype': filetype,
            'child':    child}


def listdir(dirpath):
    """
    返回指定目录下的所有文件和目录名
    """
    return os.listdir(dirpath)


def get_filetype(filepath):
    filetype = None
    if os.path.isdir(filepath):
        filetype = 'dir'
    elif isjmx(filepath):
        filetype = 'script'
    return filetype


# if __name__ == '__main__':
#     workspace = config.get('jmeter').get('workspace')
#     # print(dirname_to_abspath(workspace, 'BindCardFacade'))
#     print(get_script_tree(workspace))
