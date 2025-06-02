# -*- coding: utf-8 -*-

# 一、导入模块
from flask import Flask
import os


# 二、创建 Flask 实例
app = Flask(__name__)
app.config.from_pyfile('conf/config.py', silent=False)

# 三、定义路由及视图函数
@app.route('/')
@app.route('/home')
@app.route('/index')
def hello():
    return 'Welcome to My Watchlist!!!'

# 四、运行项目
if __name__ == "__main__":
	app.run()

