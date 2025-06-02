# 一、导入模块
from flask import Flask

# 二、创建 Flask 实例
app = Flask(__name__)

# 三、定义路由及视图函数
@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'

# 四、运行项目
