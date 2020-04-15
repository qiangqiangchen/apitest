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
    def get(self, url, data=None, headers=None, cookies=None, allow_redirects=True):
        result = requests.get(url=url, data=data, headers=headers, cookies=cookies, allow_redirects=allow_redirects)
        result.encoding = "utf-8"
        return result

    def post(self, url, data=None,json=None, headers=None, cookies=None, allow_redirects=True):
        result = requests.post(url=url, data=data,json=json, headers=headers, cookies=cookies, allow_redirects=allow_redirects)
        result.encoding = "utf-8"
        return result


if __name__ == '__main__':
    api = APIUtils()
    api.get(url=config.base_url + '/find/homepage/announcement', data=None, allow_redirects=False)
