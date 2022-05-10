#-- coding: utf-8 --

#@Time : 2022/5/9 14:16

#@Author : zhaopt

#@Email : 729560832@qq.com

#@File : operationyaml.py

#@Software: PyCharm

import json

from ruamel import yaml
# import yaml

# 写入到yaml文件
"""
dataurl为yaml文件名
content为要写入的内容,dict类型
"""
def write_yaml(dataurl,content):
    with open('../data/'+dataurl, 'w', encoding='utf-8') as f:
        # 将字典写入到yaml文件中
        yaml.dump(content, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)

#读取yaml文件
"""
filename为yaml文件名
keys为键值
"""
def read_yaml(filename,keys):
    with open('../data/'+filename, 'r', encoding="utf-8") as f:
        # yaml文件中读取内容
        msg = yaml.load(f.read(), Loader=yaml.Loader)
        return msg.get(keys)
