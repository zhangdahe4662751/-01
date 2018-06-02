# 导入flak模块
from   flask   import  Flask,session
# 命令行脚本扩展
from  flask_script import  Manager
# 导入数据库迁移对象
from  flask_migrate  import Migrate,MigrateCommand


from  info import create_app,db

from  info import models

app = create_app("Development")
# 实例化manager对象
manager = Manager(app)
# 实例化迁移脚本
Migrate(app,db)
# 给manage添加迁移扩展
manager.add_command("db",MigrateCommand)



# 程序入口
if __name__ == '__main__':
    print(app.url_map)
    manager.run()
    # app.run()
