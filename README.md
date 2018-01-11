# AutomatedTestPlatform
#### 项目介绍
自动化测试平台主要为Jmeter自动化测试提供web调度前端。

#### 安装依赖
1. 创建虚拟环境venv：```python -m venv venv```；
2. 安装依赖：```pip install -r requirements.txt```。

#### 创建SQLite数据库
##### 初始化
1. 初始化： `.\venv\Scripts\python manage.py db init`
2. 创建第一个版本： `.\venv\Scripts\python manage.py db migrate -m "initial migration"`
3. 运行升级： `.\venv\Scripts\python manage.py db upgrade``
##### 后缀更新：
1. 更新表格的字段 (models.py)
2. `.\venv\Scripts\python manage.py db migrate -m "update"`(相当于commit 更新到/migrate目录)
3. `.\venv\Scripts\python manage.py db upgrade`

#### 在shell中维护用户
```
.\venv\Scripts\python manage.py shell
>>> u = User(loginName='admin', password='admin', name='Administrator')
>>> db.session.add(u)
>>> db.session.commit()
```
