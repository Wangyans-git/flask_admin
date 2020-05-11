

class Config(object):
    """  项目配置   """
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin123@localhost/flask_mall'
    SECRET_KEY = 'ASDASD'


"""
1.按模块拆分
2.视图文件中，实例化一个蓝图对象
accounts = Blueprint('accounts',__name__,template_folder='templates',static_folder='static')
3.模块抽取单独文件，注意ORM相关配置，抽取配置到文件
4.将蓝图对象注册到flask的实例app
5.修改以前URL，要添加前缀
"""