#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_fixture_run.py
# @Time      :2020/12/25 14:45
# @Author    :HaoHao
import pytest
import allure
import os
import logging
from data.Read_data import Read

def test_1(Search_movie):
    try:
        assert 'SUCCESSED!' in Search_movie
        logging.error('有效值的成功测试')
    except:
        assert 'SUCCESSED!' not in Search_movie
        logging.error('无效值的成功测试')

if __name__ == '__main__':
    pytest.main(['-s','test_fixture_run.py','--alluredir','../temp'])
    os.system('allure generate ../temp -o ../report --clean')







