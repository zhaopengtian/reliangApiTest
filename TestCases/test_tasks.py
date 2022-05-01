import unittest
from Utils.page import *
from Basepage.unittestChushihua import TestApi
from Utils.tokeinfo import tokeninfo
class Totasks(TestApi,Helper):
    def test_2_bd(self):
        '''BD验证'''
        # token = tokeninfo()
        # url = 'http://webapi.loex.abc/exchange-web-api/v1/bd/verify'
        # headers = {"Content-Type": "application/json;charset=UTF-8", "exchange-token": token}
        # data = {'type':'Skype', 'content':'Skype'}
        # r = self.post(url,data,headers)
        self.assertEqual('10003','10002')

    def test_3_bd1(self):
        '''BD验证'''
        token = tokeninfo()
        url = 'http://webapi.loex.abc/exchange-web-api/v1/bd/verify'
        headers = {"Content-Type": "application/json;charset=UTF-8", "exchange-token": token}
        data = {'type':'Skype', 'content':'Skype'}
        r = self.post(url,data,headers)
        self.assertEqual(r.json()['code'],'10002')


if __name__ == '__main__':
    unittest.main
