# -*- coding:utf-8 -*-
import unittest,sys

from Action.login import login, logout
from Common.APIUtils import APIUtils
from Common.tools import *
from config.Tag import Tag

class test_script(NewTestCase, APIUtils):
    url = 'http://devdb.com:8988'
    cookies = None

    def setUp(self):
        self.cookies = login(data={'username': 'qiangqiangchen', 'password': 'zz123asd'})
        if not self.cookies:
            sys.exit(-1)
    # @skip_if(1==1,'不想测试')
    @skip('没有原因的跳过')
    def test_script_001(self):
        '''
        第一个测试用例
        :return:
        '''
        result = self.get(url=self.url+'/find/homepage/announcement',cookies=self.cookies)
        responsetime=result.elapsed.total_seconds()
        self.assertGreater(0.2,responsetime)
    @unittest.skipIf(3>2,'测试框架跳过功能')
    def test_script_002(self):
        result=self.get(url=self.url+'/find/wop/dept/list/search',cookies=self.cookies)
        responsetime = result.elapsed.total_seconds()
        self.assertGreater(0.2, responsetime)
    @tag(Tag.SMOKE)
    def test_script_003(self):
        data={"checkStatus":"","cnName":"","appointDept":"","caseNo":"","caseDeadlineStart":"","caseDeadlineEnd":"","isDeadline":0,"sortParam":[],"pageNum":1,"pageSize":"10"}
        result=self.post(url=self.url+'/find/my/case/info/for/allocated',json=data,cookies=self.cookies)
        responsetime = result.elapsed.total_seconds()
        self.assertGreater(0.2, responsetime)

    def tearDown(self):
        logout(self.cookies)

if __name__ == '__main__':
    unittest.main()
