#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :conftest.py.py
# @Time      :2020/12/25 14:05
# @Author    :HaoHao
import pytest
import requests
from data.Read_data import Read
# 使用fixture夹具来将请求的函数变为公共代码，需要调用的时候直接写函数名字就行
@pytest.fixture(scope='function',
                params=Read(r'../data/Ying_data.yaml'),
                # 使用这种方式必须得在fixture中用parames传参
                name='Search',
                autouse=True)
def Search_movie(request):
    url="http://web.juhe.cn:8080/environment/water/river"
    head={'Accept':'application/json, text/javascript, */*; q=0.01',
          'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    # 参数写法：get,可以直接跟url后面，用？隔开，也可以将参数赋给params函数
            # post时，将参数赋给data函数
    #         注意：post请求时，如果参数中有中文，就要用.encode()函数重新编码，否则报错，
    #         且要根据上传的参数类型添加Content-Type头部向服务器声明自己上传的数据类型
    # 如果想传json格式就导入json模块，将参数写为一个字典query={""}然后用quer=json.dumps(query)将数据类型改为json格式

    # query=f'key={request.param[0]}&river={request.param[1]}'.encode()
    query=f'key={request.param[0]}&river={request.param[1]}'
    res=requests.get(url,headers=head,params=query)
    # res=requests.post(url,headers=head,data=query)
    print(res.text)
    return  res.text

















































