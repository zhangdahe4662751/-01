# 创建蓝图对象
from flask import render_template,current_app

from . import news_blu
# 导入session
from  flask  import  session

#  绑定路由
@news_blu.route("/")
def  manage_index():
    # 配置状态保持
    session["name"] = "python003"
    return  render_template("news/index.html")

@news_blu.route("/favicon.ico")
def favicon():
    return current_app.send_static_file('news/favicon.ico')