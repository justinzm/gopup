#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/28 0028
# @Author  : justin.郑 3907721@qq.com
# @File    : university.py
# @Desc    : 高校数据

import json
import pandas as pd
import requests


def university():
    """
    获取全国普通高等学校名单
    :return:
        DataFrame
              序号
              学校名称
              学校标识码
              主管部门
              所在省市
              所在地
              办学层次
              备注
    """
    try:
        url = "http://img.kekepu.com/gaoxiao.json"
        r = requests.get(url=url)
        datas = json.loads(r.text)
        res_list = []
        for data in datas:
            for d in datas[data]:
                tmp = {}
                tmp['序号'] = d['序号']
                tmp['学校名称'] = d['学校名称']
                tmp['学校标识码'] = d['学校标识码']
                tmp['主管部门'] = d['主管部门']
                tmp['所在省市'] = data
                tmp['所在地'] = d['所在地']
                tmp['办学层次'] = d['办学层次']
                tmp['备注'] = d['备注']
                res_list.append(tmp)

        res_pd = pd.DataFrame(res_list)
        return res_pd
    except Exception as e:
        return None


def adult_university():
    """
    获取全国成人高等学校名单
    :return:
        DataFrame
              序号
              学校名称
              学校标识码
              主管部门
              备注
    """
    try:
        url = "adult.xls"
        res_pd = pd.read_excel(url)
        return res_pd
    except Exception as e:
        return None


if __name__ == "__main__":
    tmp = adult_university()
    print(tmp)



 

