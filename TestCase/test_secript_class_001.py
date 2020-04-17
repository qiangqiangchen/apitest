# -*- coding:utf-8 -*-
import unittest,sys,json

from Action.login import login, logout
from Common.APIUtils import APIUtils


class test_script_class(unittest.TestCase, APIUtils):
    url = 'http://devdb.com:8988'
    cookies = None
    @classmethod
    def setUpClass(cls):
        cls.cookies = login(data={'username': 'qiangqiangchen', 'password': 'zz123asd'})
        if not cls.cookies:
            sys.exit(-1)
    @classmethod
    def tearDownClass(cls):
        logout(cls.cookies)

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


if __name__ == '__main__':
    unittest.main()
