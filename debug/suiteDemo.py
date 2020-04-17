# -*- coding:utf-8 -*-
import os
import unittest

from Common.HTMLTestReportCN import HTMLTestRunner
from TestCase.test_secript_001 import test_script



#新建TestSuite，并添加和批量添加测试用例
suite=unittest.TestSuite()
suite.addTest(test_script('test_script_001'))
suite.addTests([test_script('test_script_002'),test_script('test_script_003')])


#使用makesuite来制作测试用例集
suite1=unittest.makeSuite(test_script,'test_script_002')  #使用测试类的单条用例制作测试集
suite2=unittest.makeSuite(test_script) # 使用整个测试类制作测试集合(包含该测试类所有用例)

#使用TestLoad(用例加载器)生成测试集
suite3=unittest.TestLoader().loadTestsFromTestCase(test_script)#加载该测试类所有用例并生成测试集


#使用discover遍历所有的用例
suite4=unittest.defaultTestLoader.discover(r'E:\pycharmproject\APITest\TestCase',pattern='test_*')



suite_1=unittest.TestSuite()
suite_1.addTest(test_script('test_script_001'))

suite_2=unittest.makeSuite(test_script,'test_script_002')

suite_count=unittest.TestSuite([suite_1,suite_2])  #将两个测试集组成一个

#生成文字测试结果
with open('result.text','w') as f:
    unittest.TextTestRunner(stream=f,verbosity=2).run(suite_count)

with open('report.html','wb') as f:
    HTMLTestRunner(stream=f,title="API test",description='测试描述',verbosity=2,tester='cqq').run(suite2)