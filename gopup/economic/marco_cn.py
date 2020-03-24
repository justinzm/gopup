#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 0024
# @Author  : justin.郑 3907721@qq.com
# @File    : marco_cn.py
# @Desc    : 中国宏观数据

import pandas as pd


def marco_cmlrd():
    """
    中国宏观杠杆率数据
    :return:
    """
    url = "http://114.115.232.154:8080/handler/download.ashx"
    excel_data = pd.read_excel(url, sheet_name="Data", header=0, skiprows=1)
    excel_data["Period"] = pd.to_datetime(excel_data["Period"]).dt.strftime("%Y-%m")
    excel_data.columns = [
        "年份",
        "居民部门",
        "非金融企业部门",
        "政府部门",
        "中央政府",
        "地方政府",
        "实体经济部门",
        "金融部门资产方",
        "金融部门负债方",
    ]
    return excel_data


if __name__ == '__main__':
    tmp = marco_cmlrd()
    print(tmp)

