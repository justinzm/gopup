#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 11:27
# @Author  : justin.郑 3907721@qq.com
# @File    : utils.py
# @Desc    :


def get_fields(fields, label):
    """ 搜索DICT中的label 获取值"""
    for res_dict in fields:
        if res_dict['label'] == label:
            return res_dict['value']
    return ""