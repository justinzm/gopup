#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 0005
# @Author  : justin.郑 3907721@qq.com
# @File    : train.py
# @Desc    : 12306车站、车次数据

import pandas as pd
import requests
from pyquery import PyQuery as pq


def station_name():
    """
    获取12306车站信息
    Returns
    -------
    DataFrame
        "拼音码、站名、电报码、拼音、首字母、ID""
    """
    try:
        url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js"
        r = requests.get(url=url)
        data_text = r.text
        tmp_str = data_text[data_text.find("='")+3: -2]
        tmp_list = tmp_str.split('@')
        res_list = []
        for li in tmp_list:
            res_list.append(li.split('|'))
        columns = ["拼音码", "站名", "电报码", "拼音", "首字母", "ID"]
        data_df = pd.DataFrame(res_list, columns=columns)
        data_df.set_index("ID", inplace=True)
        return data_df
    except:
        return None


# def train_list():
#     """
#     获取12306车次信息
#     Returns
#     -------
#     DataFrame
#         "拼音码、站名、电报码、拼音、首字母、ID""
#     """
#     url = "https://kyfw.12306.cn/otn/resources/js/query/train_list.js"
#     r = requests.get(url=url)
#     data_text = r.text
#     tmp_str = data_text[data_text.find("={")+1:]
#     # tmp_dict = json.loads(tmp_str)['2019-07-16']
#     tmp_list = tmp_str.split('@')
#     res_list = []
#     for li in tmp_list:
#         res_list.append(li.split('|'))
#     columns = ["拼音码", "站名", "电报码", "拼音", "首字母", "ID"]
#     data_df = pd.DataFrame(res_list, columns=columns)
#     data_df.set_index("ID", inplace=True)
#     return data_df


def train_time_table(train_number):
    """
    车次时刻表
    :return:
        DataFrame
        "车次、车型、始发站、终点站、始发时、终到时、全程时间"
    """
    try:
        url = "https://www.keyunzhan.com/dongche/%s/" % train_number
        r = requests.get(url=url)
        doc = pq(r.text)
        tds = doc(".listTable td[bgcolor='#FFFFFF']")
        tmp = []
        for v in tds.items():
            tmp.append(v.text())
        res = {
            "车次": tmp[0],
            "车型": tmp[1],
            "始发站": tmp[2],
            "终点站": tmp[3],
            "始发时": tmp[4],
            "终到时": tmp[5],
            "全程时间": tmp[6]
        }
        data_df = pd.DataFrame(res, index=[0])
        return data_df
    except:
        return None


if __name__ == '__main__':
    tmp = train_time_table(train_number="t15")
    print(tmp)
