# -*- coding: utf-8 -*-

# 一、导入模块
from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy


# 二、创建 Flask 实例
app = Flask(__name__)
# from_pyfile 方法默认会加载配置
app.config.from_pyfile('conf/config.py', silent=False)
# 数据库连接初始化，传入程序实例APP；
db = SQLAlchemy(app)


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

# 创建数据库模型
class User(db.Model): # 表名将会是 user（自动生成，小写处理），注意模型类要声明继承即 db.Model；
	id = db.Column(db.Integer, primary_key=True)  # 主键
	name = db.Column(db.String(20))  # 名字
	
class Movie(db.Model):      # 表名将会是 movie
	id = db.Column(db.Integer, primary_key=True) # 主键
	title = db.Column(db.String(60))  # 电影标题
	year = db.Column(db.String(4))  # 电影年份

# 三、定义路由及视图函数
@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    #return 'Welcome to My Watchlist!!!'
    user = User.query.first()  # 读取用户记录;
    movies = Movie.query.all() # 读取所有电影记录：
    return render_template('index.html', name=name, movies=movies)

# 四、运行项目
if __name__ == "__main__":
	app.run()
































