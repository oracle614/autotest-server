#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/17 11:24
# @Author  : KelvinYe
import json

from flask import request, jsonify
from flask_login import login_required

from app.common.common import get_dirname_list, get_dir_abspath, get_scriptname_list
from app.common.log import getlogger
from app.main import main
from config import config

logger = getlogger(__name__)


class Response:
    __slots__ = ('__result', '__success', '__errorcode', '__errormsg')

    def __init__(self, result, success=False, errorcode=0, errormsg='failure'):
        """
        接口响应基类
        :param result: 响应结果
        :param success: True or False
        :param errorcode: 响应码， 0：失败， 1：成功
        :param errormsg: success or failure
        """
        self.__result = result
        self.__success = success
        self.__errorcode = errorcode
        self.__errormsg = errormsg


@main.route('/api/getdirandscript', methods=['GET'])
# @login_required
def getdirandscript():
    workspace = config.get('jmeter').get('workspace')
    dir_name = request.args.get('dirname')
    dir_abspath = get_dir_abspath(workspace, dir_name)
    logger.debug(f'dir_name={dir_name}')
    logger.debug(f'dir_abspath={dir_abspath}')

    dirlist = get_dirname_list(dir_abspath)
    scriptlist = get_scriptname_list(dir_abspath)
    logger.debug(f'dirlist={dirlist}')
    logger.debug(f'scriptlist={scriptlist}')

    return jsonify({'dirlist': dirlist, 'scriptlist': scriptlist})


@main.route('/api/runjmter', methods=['POST'])
# @login_required
def runjmter():
    script_type = request.form.get('scriptType')
    script_value = request.form.get('scriptValue')
    logger.debug(f'script_type={script_type}')
    logger.debug(f'script_value={script_value}')

    return 'runjmter'
