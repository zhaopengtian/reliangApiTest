import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(r"E:/pyobject/seleniumTest/testCases")
from TestCases.test_tasks import Totasks

import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import yagmail
from Utils.log import *


# '''发送带邮件的函数动作'''
# def send_mall(file_new):
#     f = open(file_new,'rb')
#     mail_boby = f.read()
#     f.close()
#     #基本信息
#     smtpsrver = 'smtp.qq.com'
#     pwd = "exbjjmbjshezbdga"    #QQ邮箱授权码
#     #定义邮件主题
#     msg = MIMEMultipart()
#     msg['subject'] = Header(u'PO自动化测试报告','utf-8')
#     msg['form'] = "729560832@qq.com"                        #必须加，不加报错。发送者邮箱账号
#     msg['to'] = "zhaopengtian2015@163.com"                  #必须加，不加报错。接收者邮箱账号
#     #html邮件正文
#     body = MIMEText(mail_boby,"html","utf-8")
#     msg.attach(body)
#     att = MIMEText(mail_boby,"base64","utf-8")
#     att["Content-Type"] = "application/octet-stream"
#     att["Content-Disposition"] = 'attachment;filename="test_report.html"'
#     msg.attach(att)
#     #链接邮箱服务器发送邮件
#     smtp = smtplib.SMTP()
#     smtp.connect(smtpsrver)
#     smtp.login(msg['from'],pwd)
#     smtp.sendmail(msg['from'],msg['to'],msg.as_string())
#     log.info("邮件发送成功")

def new_file(test_dir):
    result_dir = test_dir
    lists = os.listdir(result_dir)     #print(lists)   #列出测试报告目录下的所有文件
    lists.sort()                                       #从小到大排序 文件
    file = [x for x in lists if x.endswith('.html')]   #for循环遍历以.html格式的测试报告
    file_path = os.path.join(result_dir,file[-1])      #找到测试报告目录下最新的测试报告
    return file_path
'''获取testcase下的所有模块'''
# def getAllClass():
#     Testsuite = unittest.defaultTestLoader.discover(
#         start_dir= os.path.join(os.path.dirname(__file__)),
#         pattern='test*.py')
#     return Testsuite


'''生成测试报告写入指定的Reports目录'''
# def runMain():
#     f = open(os.path.join(os.path.dirname(__file__),'report',time.strftime("%Y_%m_%d_%H_%M_%S")+'report.html'),'wb')
#
#     runner = HTMLTestRunner(
#             stream=f,  # 文件
#             title="python自动化测试百度进入测试",  # 标题
#             description="简单的账户登录自动化测试1"  # 描述
#         )
#     runner.run(getAllClass())  # 启动测试套件


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.realpath(__file__))                                       #获取文件所在路径
    pro_dir = os.path.dirname(os.path.realpath(__file__)).split('seleniumTest')[0]               #项目所在路径
    test_dir = os.path.join(base_dir)                                                #测试用例所在目录
    test_report = os.path.join(pro_dir,'Reports')         #测试报告所在目录
    # print(base_dir)
    # print(pro_dir)
    # print(test_dir)
    # print(test_report)
    # print(sys.path)
    '''跑testCases包下的所有测试用例'''
    # testlist = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    '''跑指定文件下的测试用例'''
    testlist = unittest.TestSuite()
    testlist.addTest(Totasks("test_2_bd"))
    # testlist.addTest(TestModel("test_4_ss"))
    '''跑一个类文件下的所有测试用例'''
    # testlist = unittest.TestSuite(unittest.makeSuite(TestModel))
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename = test_report + "\\" + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(
                stream=fp,  # 文件
                verbosity=2,
                title="pythonPO自动化测试百度进入测试",  # 标题
                description=u"系统环境：Win10 浏览器：Chrome 用例执行情况："  # 描述
            )
    runner.run(testlist)  # 启动测试套件

    fp.close()
    new_report = new_file(test_report)                                #获取最新报告文件

    yagindex = yagmail.SMTP(user='729560832@qq.com', password='exbjjmbjshezbdga', host='smtp.qq.com')
    yag_contents = ['这是一个yagmail模板发送邮件正文的实例，哈哈哈哈']
    # yagindex.send('zhaopengtian@lefu.cc', 'yagmail带附件主题实例', yag_contents, new_report)
    yagindex.send('zhaopengtian2015@163.com', 'yagmail带附件主题实例', yag_contents, new_report)
    log.info('发送邮件成功')
