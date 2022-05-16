#-- coding: utf-8 --

#@Time : 2022/5/9 9:35

#@Author : zhaopt

#@Email : 729560832@qq.com

#@File : test_login.py

#@Software: PyCharm


import unittest
from Utils.page import *
from Basepage.unittestChushihua import TestApi
from Utils.operationyaml import *
from Utils.operationini import *
from Utils.log import *
class Login(TestApi,Helper):
    # 获取服务器地址
    url = read_yaml('server_address.yaml', 'url')
    '''客户端用户登录,登录成功'''
    def test_login(self):
        url = 'http://' + self.url + '/public/login'
        log.info("客户端用户登录,登录成功:"+url)
        #获取ini中用例
        data = getini_by_section('客户端用户登录,登录成功')
        headers = {}
        r = self.post(url,data,headers)
        log.info('传入参数:')
        self.assertEqual(r.json()['msg'], '登录成功')
        self.assertEqual(r.json()['data']['userName'], getini_by_option('客户端用户登录,登录成功','username'))
        self.assertEqual(r.json()['data']['userName'], '索诺亚')
        self.assertEqual(r.json()['data']['deptName'], '横岗街道保安学校')
        self.assertEqual(r.json()['data']['idCard'], '210282199004103417')
        self.assertEqual(r.json()['data']['healthCard'], '9999')
        self.assertEqual(r.json()['data']['userTel'], '14000000000')
        log.info(r.json()['msg'])
        token = r.json()['data']['token']
        print(r.text)

        #将token写入yaml文件
        if token:
            token_data = {'token':token}
            write_yaml('token.yaml',token_data)
            log.info("token写入yaml成功")
        else:
            log.info('没有token')


