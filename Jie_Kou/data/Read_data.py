#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Read_data.py
# @Time      :2020/12/25 10:45
# @Author    :HaoHao
import yaml

def Read(file):
    with open(rf"{file}","r") as f:
        r=yaml.safe_load(f)
    Data=list(zip(r["key_1"],r["name"]))
    print(Data)
    return Data
# Read('Ying_data.yaml')
