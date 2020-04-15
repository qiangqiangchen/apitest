# -*- coding: UTF-8 -*-
import json

import requests

from Action.login import login
from config import config

if __name__=='__main__':
    url=config.base_url+'/fileComponentController/upload'
    files={'upfile':open(r'C:\Users\Administrator\Desktop\作业人员.xls','rb')}
    data={'annoType':'1','annoTitle':'2222222','creatUser':r'任卫华','createDatetime':'2020-04-08','editorValue':'<p>2222222222222222</p>'}
    cookies=login(data={'username': 'qiangqiangchen', 'password': 'zz123asd'})
    result=requests.post(url=url,data=data,files=files,cookies=cookies)
    filename_json=result.json()
    filename=filename_json['data'][0]['fileName']
    old_name=filename_json['data'][0]['fileOldName']
    print(result.text)
    gonggao={'annoType':'1',
             'annoTitle':'2222222',
             'creatUser':r'任卫华',
             'createDatetime':'2020-04-08',
             filename+'_fileName':filename,
             filename+'_realName':old_name,
             'editorValue':'<p>2222222222222222</p>',
             'annoStatus':'1',
             'annoContents':'<p>2222222222222222</p>'}
    creat=requests.post(url=config.base_url+'/publish/announcement',data=gonggao,cookies=cookies)
    print(creat.text)