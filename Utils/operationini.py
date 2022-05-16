#-- coding: utf-8 --

#@Time : 2022/5/9 16:06

#@Author : zhaopt

#@Email : 729560832@qq.com

#@File : operationini.py

#@Software: PyCharm
from Utils.conf import Conf
import configparser
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
class Conf(configparser.ConfigParser):
    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr
    """
    根据section获取所有值
    """

    def getini_by_section(section):
        #必须实例化一下类
        cf = Conf()
        #获取ini文件路径
        # conf = configparser.ConfigParser()
        file_path = sys.path[1]+'\data\\'+"case_parameters.ini"
        cf.read(file_path,encoding='UTF-8')
        #根据section获取所有的值
        items = cf.items(section)
        #将list转为dict
        return dict(items)

    """
    根据option获取所有值
    """
    def getini_by_option(section,option):
        cf = Conf()
        # 获取ini文件路径
        # conf = configparser.ConfigParser()
        file_path = sys.path[1]+'\data\\'+"case_parameters.ini"
        cf.read(file_path,encoding='UTF-8')
        # 根据section获取所有的值
        value = cf.get(section,option)
        return value


    # sections = conf.sections()
    # print('获取配置文件所有的section', sections)
    #
    # options = conf.options('客户端用户登录,登录成功')
    # print('获取指定section下所有option', options)




