#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 0016
# @Author  : justin.郑 3907721@qq.com
# @File    : index_google.py
# @Desc    : 谷歌相关数据接口

import ast
import pandas as pd
import requests
from gopup.index.cons import headers
from gopup.utils.date_utils import int2time


def google_fact_check(keyword, offset=0, limit=100, hl=None):
    """
    谷歌事实查证
    :param keyword: 查证关键词
    :param offset:  起始数
    :param limit:   每次获取数量 300篇最大
    :param hl:      语言 默认为全部；中文：zh，英文：en ……
    :return:
        DataFrame
            title       信息标题
            url         信息链接
            type        查证类型
            remark      查证摘要
            check       查核机构
            source_data 信息来源
            news_img    信息图像
            value       事实查证值
            date        日期时间
    """
    try:
        url = "https://toolbox.google.com/factcheck/api/search"
        data = {
            "hl": hl,
            "query": keyword,
            "num_results": limit,
            "offset": offset
        }
        r = requests.get(url, params=data, headers=headers)
        if r.status_code == 200:
            con = r.text[6:]
            con = con.replace("\n", "").replace("null", "'-'")
            con_list = ast.literal_eval(con)[0][1]
            res_list = []
            for i in range(0, len(con_list)):
                con = con_list[i]
                tmp = {
                    "title": con[0][0],
                    "type": con[0][3][0][3],
                    "url": con[0][3][0][1],
                    "remark": con[0][3][0][8],
                    "check": con[0][3][0][0][0],
                    "source_data": listToStr(con[0][3][0][0]),
                    "date": "-" if con[0][3][0][2] == "-" else int2time(int(con[0][3][0][2])),
                    "news_img": con[1],
                    "value": con[2],
                }
                res_list.append(tmp)
        res_pd = pd.DataFrame(res_list)
        return res_pd
    except:
        return None


def listToStr(lists):
    res = []
    for li in lists:
        if not isinstance(li, list):
            res.append(li)
    if len(res) > 0:
        return ','.join(res)
    return None


if __name__ == "__main__":
    google_fact_check(keyword="china", hl="zh")

