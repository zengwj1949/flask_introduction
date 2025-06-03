# -*- coding: utf-8 -*-

# 一、导入模块
from flask import Flask, render_template
import os


# 二、创建 Flask 实例
app = Flask(__name__)
app.config.from_pyfile('conf/config.py', silent=False)

# 定义虚拟数据
name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

# 三、定义路由及视图函数
@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    #return 'Welcome to My Watchlist!!!'
    return render_template('index.html', name=name, movies=movies)

# 四、运行项目
if __name__ == "__main__":
	app.run()
































