#-- coding: utf-8 --

#@Time : 2022/5/9 9:54

#@Author : zhaopt

#@Email : 729560832@qq.com

#@File : test_shouye.py

#@Software: PyCharm
import time
import unittest
import json
from Utils.dicttogetparameter import *
from Utils.log import *
from Utils.page import *
from Utils.operationyaml import *
from Utils.operationini import Conf
from Basepage.unittestChushihua import TestApi
class Shouye(TestApi,Helper):
    # 获取token
    token = read_yaml('token.yaml', 'token')
    #获取服务器地址
    url = read_yaml('server_address.yaml', 'url')
    cf = Conf

    '''获取保健文章分类,正确'''
    def test_shouye_articleclassification(self):
        # 获取ini中用例
        data = self.cf.getini_by_section('获取保健文章分类,正确')
        get_parameter = dict_to_get_parameter(data)
        url = 'http://'+self.url+'/healthArticle/getArticleType?'+get_parameter
        log.info('获取保健文章分类,正确:'+url)
        headers = {"token": self.token}
        r = self.get(url,headers)
        log.info('传入参数:')
        # print(json.dumps(r,ensure_ascii=False,indent=1))
        # print(r.text)
        self.assertEqual(1000,r.json()['code'])
        self.assertEqual('71',r.json()['data'][5]['typeId'],'typeId值不正确')
        self.assertEqual('妇幼保健', r.json()['data'][5]['typeName'], 'typeName值不正确')
        log.info('接口正确参数获取保健文章分类成功')
        time.sleep(2)


    '''获取保健文章列表,正确'''
    def test_shouye_articlelist(self):
        # 获取ini中用例
        data= self.cf.getini_by_section('获取保健文章列表,正确')
        #进行格式转换
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/healthArticle/getHealthArticleList?'+get_parameter
        log.info('获取保健文章列表,正确:'+url)
        headers = {"token": self.token}
        r = self.get(url,headers)
        log.info('传入参数:')
        # print(json.dumps(r,ensure_ascii=False,indent=1))
        # print(r.json()['data']['records'][0])
        print(r.text)
        self.assertEqual(1000, r.json()['code'])
        self.assertEqual('妇幼文章', r.json()['data']['records'][0]['title'], 'title值不正确')
        self.assertEqual('71', r.json()['data']['records'][0]['typeId'], 'typeId值不正确')
        self.assertEqual('啦啦啦啦啦啦啦啦绿绿绿', r.json()['data']['records'][0]['overview'], 'overview值不正确')
        read_name = r.json()['data']['records'][0]['readNum']
        self.assertFalse(read_name==None and read_name=="",'read_name的值为空')
        log.info('接口正确参数获取保健文章列表成功')
        time.sleep(2)

    '''获取保健知识文章详情,正确'''
    def test_shouye_articledetails(self):
        data = self.cf.getini_by_section('获取保健知识文章详情,正确')
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/healthArticle/getArticleDetail?'+get_parameter
        log.info('获取保健知识文章详情:'+url)
        headers = {"token": self.token}
        # 获取ini中用例
        # print(data)
        # data = {'id':227}
        r = self.get(url,headers)
        log.info('传入参数:')
        print(r.text)
        # print(json.dumps(r,ensure_ascii=False,indent=1))
        # print(r.json()['data']['records'][0])
        # self.assertEqual(1000, r.json()['code'])
        # self.assertEqual('妇幼文章', r.json()['data']['records'][0]['title'], 'title值不正确')
        # self.assertEqual('71', r.json()['data']['records'][0]['typeId'], 'typeId值不正确')
        # self.assertEqual('啦啦啦啦啦啦啦啦绿绿绿', r.json()['data']['records'][0]['overview'], 'overview值不正确')
        # read_name = r.json()['data']['records'][0]['readNum']
        # self.assertFalse(read_name==None and read_name=="",'read_name的值为空')
        log.info('接口正确参数获取保健知识文章详情成功')
        time.sleep(2)

