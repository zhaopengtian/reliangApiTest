#-- coding: utf-8 --

#@Time : 2022/5/16 10:02

#@Author : zhaopt

#@Email : 729560832@qq.com

#@File : dicttogetparameter.py

#@Software: PyCharm


'''把dict转换成get参数形式'''
def dict_to_get_parameter(paramt):
    return (str(paramt)[2:-2].replace("': '","=").replace("', '","&"))
