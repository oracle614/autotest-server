#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/17 11:24
# @Author  : KelvinYe

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
    logger.debug(rf'response={response}')

    return jsonify(json.dumps(response))


@main.route('/api/jmeter/run', methods=['POST'])
# @login_required
def runjmter():
    if request.method == 'POST':
        scripts = request.form.get('scriptType')
        logger.debug(f'scripts={scripts}')

    # return 'runjmter'
