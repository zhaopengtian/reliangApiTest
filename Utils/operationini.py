#-- coding: utf-8 --

#@Time : 2022/5/9 16:06

#@Author : zhaopt

#@Email : 729560832@qq.com

#@File : operationini.py

#@Software: PyCharm

import configparser
"""
根据section获取所有值
"""
def getini_by_section(section):
    #获取ini文件路径
    conf = configparser.ConfigParser()
    file_path = "../data/case_parameters.ini"
    conf.read(file_path,encoding='UTF-8')
    #根据section获取所有的值
    items = conf.items(section)
    #将list转为dict
    return dict(items)

"""
根据option获取所有值
"""
def getini_by_option(section,option):
    # 获取ini文件路径
    conf = configparser.ConfigParser()
    file_path = "../data/case_parameters.ini"
    conf.read(file_path,encoding='UTF-8')
    # 根据section获取所有的值
    value = conf.get(section,option)
    return value


    # sections = conf.sections()
    # print('获取配置文件所有的section', sections)
    #
    # options = conf.options('客户端用户登录,登录成功')
    # print('获取指定section下所有option', options)




