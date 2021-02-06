#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 0005
# @Author  : justin.郑 3907721@qq.com
# @File    : train.py
# @Desc    : 12306车站、车次数据

import json
import pandas as pd
import requests


def station_name():
    """
    获取12306车站信息
    Returns
    -------
    DataFrame
        "拼音码、站名、电报码、拼音、首字母、ID""
    """
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


def train_list():
    """
    获取12306车次信息
    Returns
    -------
    DataFrame
        "拼音码、站名、电报码、拼音、首字母、ID""
    """
    url = "https://kyfw.12306.cn/otn/resources/js/query/train_list.js"
    r = requests.get(url=url)
    data_text = r.text
    tmp_str = data_text[data_text.find("={")+1:]
    tmp_dict = json.loads(tmp_str)['2019-07-16']
    tmp_list = tmp_str.split('@')
    res_list = []
    for li in tmp_list:
        res_list.append(li.split('|'))
    columns = ["拼音码", "站名", "电报码", "拼音", "首字母", "ID"]
    data_df = pd.DataFrame(res_list, columns=columns)
    data_df.set_index("ID", inplace=True)
    return data_df


if __name__ == '__main__':
    tmp = train_list()
    print(tmp)
