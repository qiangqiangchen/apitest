# -*- coding: UTF-8 -*-
import requests

from config import config


class APIUtils:
    # def send(self, method, url=None, data=None, cookies=None,**kw):
    #     result = None
    #     if method.lower() == 'post':
    #         result = requests.post(url=url, data=data, cookies=cookies,**kw)
    #         result.encoding = "utf-8"
    #     elif method.lower() == 'get':
    #         result = requests.get(url=url, data=data, cookies=cookies,**kw)
    #         result.encoding = "utf-8"
    #     else:
    #         print('method值错误！！！')
    def get(self, url, data=None, headers=None, cookies=None, allow_redirects=True, timeout=300):
        try:
            result = requests.get(url=url, data=data, headers=headers, cookies=cookies, allow_redirects=allow_redirects,
                                  timeout=timeout)
            result.encoding = "utf-8"
            return result
        except requests.exceptions.Timeout:
            print(url+'timeout')


    def post(self, url, data=None, json=None, headers=None, cookies=None, allow_redirects=True, timeout=300):
        try:
            result = requests.post(url=url, data=data, json=json, headers=headers, cookies=cookies,
                                   allow_redirects=allow_redirects, timeout=timeout)
            result.encoding = "utf-8"
            return result
        except requests.exceptions.Timeout:
            print(url+'timeout')

if __name__ == '__main__':
    api = APIUtils()
    api.get(url=config.base_url + '/find/homepage/announcement', data=None, allow_redirects=False)
