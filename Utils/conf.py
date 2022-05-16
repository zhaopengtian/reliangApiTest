#-- coding: utf-8 --

#@Time : 2022/5/16 11:11

#@Author : zhaopt

#@Email : 729560832@qq.com

#@File : conf.py

#@Software: PyCharm

import configparser
class Conf(configparser.ConfigParser):
    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

cf = Conf()
cf.read("../data/case_parameters.ini",encoding='UTF-8')
exclude_list = cf.options('获取保健文章列表,正确')
print(exclude_list)