#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 15:22
# @Author  : KelvinYe

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import User

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


def get_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


"""
.\venv\Scripts\python manage.py shell
"""
manager.add_command("shell", Shell(make_context=get_shell_context))

"""
第一次使用：
1. 初始化： .\venv\Scripts\python manage.py db init
2. 创建第一个版本： .\venv\Scripts\python manage.py db migrate -m "initial migration"
3. 运行升级： .\venv\Scripts\python manage.py db upgrade

后缀更新：
1. 更新表格的字段 (models.py)
2. .\venv\Scripts\python manage.py db migrate -m "update"(相当于commit 更新到/migrate目录)
3. .\venv\Scripts\python manage.py db upgrade
"""
manager.add_command('db', MigrateCommand)

"""
.\venv\Scripts\python manage.py runserver
"""
if __name__ == '__main__':
    # manager.run()
    app.run()
