#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/17 11:24
# @Author  : KelvinYe
import json

from flask import request, jsonify
from flask_login import login_required

from app.common.common import get_dirname_list, dirname_to_abspath, get_scriptname_list
from app.common.log import getlogger
from app.main import main
from config import config

logger = getlogger(__name__)


@main.route('/api/jmeter/getscript', methods=['GET'])
# @login_required
def getdirandscript():
    workspace = config.get('jmeter').get('workspace')
    dir_name = request.args.get('dirname')
    dir_abspath = dirname_to_abspath(workspace, dir_name)
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
