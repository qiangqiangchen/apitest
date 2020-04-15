# -*- coding: UTF-8 -*-
import requests

from Common.APIUtils import APIUtils
from config import config

api = APIUtils()

def login(data):

    result = api.post(url=config.base_url + '/doLogin', data=data, allow_redirects=False)
    home=api.get(url=config.base_url + '/home',cookies=result.cookies)
    if u'在线作业平台首页' in home.text:
        print(r'登录成功')
        return result.cookies
    else:
        print('login is fail')
        return None

def logout(cookies):
    api.get(url=config.base_url+'/logout',cookies=cookies,allow_redirects=False)
    home = api.get(url=config.base_url + '/home', cookies=cookies)
    if u'在线作业平台登录' in home.text:
        print('登出成功')
    else:
        print('登出失败')


if __name__=='__main__':
    c=login(data={'username': 'qiangqiangchen', 'password': 'zz123asd'})
    logout(c)