from  redis import StrictRedis
class  Config(object):
    # 设置密钥
    SECRET_KEY = "jbqysui2YyP+VP+kyEFi/FcIgQ1BPKnts+qSZfZyleV+OE1pG5lgzEHxub+n6NNZikNuoq3t4J7c9+OhRApKew=="
    #配置debug模式
    DEBUG = True
    # 配置数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/python000'
    # 配置动态追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 配置session存储的数据库
    REDIS_HOSE = "127.0.0.1"
    REDIS_PORT = 6379

    SESSION_TYPE = "redis"
    # 实例化session对象
    SESSION_REDIS = StrictRedis(host=REDIS_HOSE,port=REDIS_PORT)
    # 配置过期时间
    PERMANENT_SESSION_LIFETIME = 86400
    # 对SESSION对象进行签名
    SESSION_USE_SIGNER = True

class  Development(Config):
    DEBUG = True


class Product(Config):
    DEBUG = False


myconfig = {
    "Development":Development,
    "product":Product
}




