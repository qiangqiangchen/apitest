# -*- coding: UTF-8 -*-
import unittest

from config.Tag import Tag
from config.config import setting

CASE_TAG_FLAG = "__case_tag__"
CASE_INFO_FLAG = "__case_info__"

def skip_if(condition,reason):
    def wrap(func):
        return unittest.skipIf(condition,'"{}" is skipped ,renson:{}'.format("{}.{}".format(func.__module__, func.__name__),reason))(func)
    return wrap

def skip(reason):
    def wrap(func):
        return unittest.skip('"{}" is skipped ,renson:{}'.format("{}.{}".format(func.__module__, func.__name__),reason))(func)
    return wrap

def tag(*tag_type):
    def wrap(func):
        if not hasattr(func, CASE_TAG_FLAG):
            tags = {Tag.ALL}
            tags.update(tag_type)
            setattr(func, CASE_TAG_FLAG, tags)
        else:
            getattr(func, CASE_TAG_FLAG).update(tag_type)
        return func

    return wrap


class Tools():
    @staticmethod
    def filter_test_case(funcs_dict):
        funcs = dict()
        cases = dict()
        for i in funcs_dict:
            if i.startswith('test_'):
                cases[i] = funcs_dict[i]
            else:
                funcs[i] = funcs_dict[i]
        return funcs, cases


class Meta(type):
    def __new__(cls, clsname, bases, attrs):
        funcs, cases = Tools.filter_test_case(attrs)
        for test_case_name, test_case in cases.items():
            if not hasattr(test_case, CASE_TAG_FLAG):
                setattr(test_case, CASE_TAG_FLAG, {Tag.ALL})
            # 增加用例标识
            case_info = "{}.{}".format(test_case.__module__, test_case.__name__)
            setattr(test_case, CASE_INFO_FLAG, case_info)

            # 过滤不执行的

            if not getattr(test_case, CASE_TAG_FLAG) & set(setting.run_case):
                continue
            else:
                funcs.update({test_case_name: test_case})
        return super(Meta, cls).__new__(cls, clsname, bases, funcs)


class NewTestCase(unittest.TestCase, metaclass=Meta):
    pass


unittest.TestCase = NewTestCase

if __name__ == '__main__':
    d = {'__module__': 'testcase.test_case_001', '__qualname__': 'TestBattle', 'test_start_battle': '123',
         'test_skill_buff': '123',
         'test_normal_attack': '<function TestBattle.test_normal_attack at 0x0000000005526840>',
         'test_get_battle_reward': '<function TestBattle.test_get_battle_reward at 0x00000000055268C8>'}
    def getatt():
        name='cqq'
        print(name)
    print(getattr(getatt,'__classs__'))
