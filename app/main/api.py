#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/17 11:24
# @Author  : KelvinYe
import json

from flask import request, jsonify
from flask_login import login_required

from app.common.common import *
from app.common.log import getlogger
from app.main import main
from config import config

logger = getlogger(__name__)


@main.route('/api/jmeter/getscript', methods=['GET'])
# @login_required
def getscript():
    workspace = config.get('jmeter').get('workspace')
    response = get_script_tree(workspace)
    logger.debug(rf'workspace={workspace}')
    logger.debug(rf'response={response}')

    return jsonify(json.dumps(response))


@main.route('/api/runjmter', methods=['POST'])
# @login_required
def runjmter():
    script_type = request.form.get('scriptType')
    script_value = request.form.get('scriptValue')
    logger.debug(f'script_type={script_type}')
    logger.debug(f'script_value={script_value}')

    return 'runjmter'
