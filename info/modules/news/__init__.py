# 导入蓝图对象
from  flask import Blueprint

# 创建蓝图对象
news_blu = Blueprint("news_blu",__name__)

# 使用蓝图的模块导入创建蓝图的模块
from . import views