import unittest
from Utils.page import *
from Utils.tokeinfo import tokeninfo
class Totasks(unittest.TestCase,Helper):

    def test_bd(self):

        token = tokeninfo()
        url = 'http://192.168.8.197:9007/calorie-management-diet/login/sendMsg?phone=14000000101&templateId=441820&areaCode=0086'
        headers = {"Content-Type": "application/json;charset=UTF-8", "platform": "Android","version":"1.0.0"}
        data = {'phone':'14000000103', 'templateId':'441820','areaCode':'0086'}
        r = self.get(url,headers)
        print(r.text)
        print(r.json()['msg'])
        # self.assertEqual(r.json()['code'], '10003')


if __name__ == '__main__':
    unittest.main
