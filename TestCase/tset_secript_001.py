# -*- coding:utf-8 -*-
import unittest,sys,json

from Action.login import login, logout
from Common.APIUtils import APIUtils


class test_script(unittest.TestCase, APIUtils):
    url = 'http://devdb.com:8988'
    cookies = None

    def setUp(self):
        self.cookies = login(data={'username': 'qiangqiangchen', 'password': 'zz123asd'})
        if not self.cookies:
            sys.exit(-1)
    def test_script_001(self):
        result = self.get(url=self.url+'/find/homepage/announcement',cookies=self.cookies)
        print(result.text)
    def test_script_002(self):
        result=self.get(url=self.url+'/find/wop/dept/list/search',cookies=self.cookies)
        print(result.text)
    def test_script_003(self):
        data={"checkStatus":"","cnName":"","appointDept":"","caseNo":"","caseDeadlineStart":"","caseDeadlineEnd":"","isDeadline":0,"sortParam":[],"pageNum":1,"pageSize":"10"}
        result=self.post(url=self.url+'/find/my/case/info/for/allocated',json=data,cookies=self.cookies)
        print(result.text)
    def tearDown(self):
        logout(self.cookies)

if __name__ == '__main__':
    unittest.main()
