#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/11/17 11:24
# @Author  : KelvinYe
import time
from flask import request, jsonify
from flask_login import login_required

from app.common.common import *
from app.common.jmeter import Jmeter, Env
from app.common.log import getlogger
from app.main import main
from config import config

logger = getlogger(__name__)


@main.route('/api/jmeter/gettree', methods=['GET'])
# @login_required
def gettree():
    workspace = config.get('jmeter').get('workspace')
    dirname = request.args.get('dirname')
    treepath = get_abspath_by_dirname(workspace, dirname)
    response = get_script_tree(treepath)
    logger.debug(rf'response={response}')

    return jsonify(json.dumps(response))

# @main.route('/api/jmeter/run', methods=['POST'])
# @login_required
# def runjmter():
#     if request.method == 'POST':
#         env = Env.get_testenv(request.form.get('env'))
#         script_list = request.form.get('scriptList')
#         jmeterbin = config.get('jmeter').get('jmeterbin')
#         currenttime = time.strftime('%Y%m%d%H%M%S', time.localtime())
#         reportname = rf'../htmlreport/{currenttime}.html'
#         logger.debug(f'env={env}')
#         logger.debug(f'scriptList={script_list}')
#         logger.debug(f'reportname={reportname}')
#
#         os.chdir(jmeterbin)  # 设置脚本执行路径为jmeter/bin
#         jmeter = Jmeter(env, reportname, jmeterbin)
#         for script in script_list:
#             jmeter.execute(script)
#
#         return 'runjmter'
