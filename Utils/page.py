import os,requests

class Helper(object):
    def get(self,url,data,headers=''):
        '''重构Get请求'''
        if url:
            r = requests.get(url=url,data=data,headers=headers)
            return r
        else:
            try:
                print('接口地址有误！')
            except Exception as M:
                print('错误原因：%s'%M)

    def post(self,url,data,headers=''):
        '''重构Post请求'''
        if url:
            r = requests.post(url=url,data=data,headers=headers)
            return r
        else:
            try:
                print('接口地址有误！')
            except Exception as M:
                print('错误原因：%s' % M)

    def delete(self,url,headers=''):
        '''重构Delete请求'''
        if url:
            r = requests.get(url=url, headers=headers)
            return r
        else:
            try:
                print('接口地址有误！')
            except Exception as M:
                print('错误原因：%s' % M)