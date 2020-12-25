#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_YingXun.py
# @Time      :2020/12/25 10:54
# @Author    :HaoHao
# import os
#
# import pytest
# import allure
# from common import Yingshi_jiekou
# from data import Read_data
# import logging
# Yingshi_jiekou.Y_xun().log()
# class Test_Yingxun():
#     @pytest.mark.parametrize('key_1,name',Read_data.Read('../data/Ying_data.yaml'))
#     def test_1(self,key_1,name):
#         res=Yingshi_jiekou.Y_xun().Search_movie(key_1,name)
#         logging.debug('获取两个参数')
#         try:
#             assert '成功的返回' in res
#             logging.error('获取两个参数')
#         except:
#             assert '成功的返回' not in res
#             logging.error('获取两个参数')
#
# if __name__ == '__main__':
#     pytest.main(['-s','test_YingXun.py','--alluredir','../temp'])
#     os.system('allure generate ../temp -o ../report --clean')
