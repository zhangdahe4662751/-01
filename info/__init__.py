# 导入flask模块
import logging
from logging.handlers import RotatingFileHandler

from  flask  import  Flask
# 导入flask_sqlaichemy模块
from  flask_sqlalchemy import   SQLAlchemy
# 导入Session并且实例化
from   flask_session import  Session
# 导入flaskwtf扩展
from  flask_wtf import CSRFProtect

from config import myconfig


# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG) # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)




db = SQLAlchemy()
def  create_app(config_name):
    # 实例化对象
    app = Flask(__name__)
    # 配置生产环境
    app.config.from_object(myconfig[config_name])
    # db与app进行关联
    db.init_app(app)
    # 实例化session对象
    Session(app)
    # 实例化csrf对象，配置cerf保护
    CSRFProtect(app)
    # 注册蓝图
    from  info.modules.news  import news_blu
    app.register_blueprint(news_blu)
    return app





