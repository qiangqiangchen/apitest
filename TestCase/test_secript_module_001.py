# -*- coding:utf-8 -*-
import unittest, sys, json

from Action.login import login, logout
from Common.APIUtils import APIUtils

url = 'http://devdb.com:8988'

cookies = None

# 当前模块执行前只执行一次
def setUpModule():
    global cookies
    cookies = login(data={'username': 'qiangqiangchen', 'password': 'zz123asd'})
    print('======setUpModule======')

# 当前模块执行前只执行一次
def tearDownModule():
    global cookies
    logout(cookies)
    cookies=None
    print('======tearDownModule======')


class test_script_class_s(unittest.TestCase, APIUtils):
    # 类方法，后面是cls,整个类只执行一次
    @classmethod #声明为类方法（必须）
    def setUpClass(cls):
        print('======setUpClass======')

    # 当前类只执行一次
    @classmethod
    def tearDownClass(cls):
        print('======tearDownClass======')

    def test_script_001(self):
        result = self.get(url=url + '/find/homepage/announcement', cookies=cookies)
        print(result.text)

    def test_script_002(self):
        result = self.get(url=url + '/find/wop/dept/list/search', cookies=cookies)
        print(result.text)



class test_script_module(unittest.TestCase, APIUtils):
    #该类中每个测试用例执行一次
    def setUp(self):
        print('======setUp======')

    def test_script_003(self):
        data = {"checkStatus": "", "cnName": "", "appointDept": "", "caseNo": "", "caseDeadlineStart": "",
                "caseDeadlineEnd": "", "isDeadline": 0, "sortParam": [], "pageNum": 1, "pageSize": "10"}
        result = self.post(url=url + '/find/my/case/info/for/allocated', json=data, cookies=cookies)
        print(result.text)

    # 该类中每个测试用例执行一次
    def tearDown(self):
        print('======tearDown======')


if __name__ == '__main__':
    unittest.main()
