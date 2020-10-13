#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 17:36
# @Author  : justin.郑 3907721@qq.com
# @File    : franchise.py
# @Desc    : 商业特许经营信息

import pandas as pd
import requests


def franchise_china():
    """
    中国-商业特许经营信息管理
    http://txjy.syggs.mofcom.gov.cn/
    :return: 中国-商业特许经营的所有企业
    :rtype: pandas.DataFrame
    """
    url = "http://txjy.syggs.mofcom.gov.cn/index.do"
    # file_url 历史数据文件, 主要是为了防止重复访问的速度和资源浪费问题
    file_url = "https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/franchise/franchise_china.csv"
    outer_df = pd.read_csv(file_url, encoding="gbk", index_col=0)
    try:
        for page in range(1, 5):
            payload = {
                "method": "entps",
                "province": "",
                "city": "",
                "cpf.cpage": str(page),
                "cpf.pagesize": "100",
            }
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
            }
            r = requests.get(url, params=payload, headers=headers)
            temp_df = pd.read_html(r.text)[1]
            inner_df = temp_df.iloc[:, 0].str.split("  ", expand=True)
            inner_df.columns = ["特许人名称", "备案时间", "地址"]
            outer_df = outer_df.append(inner_df, ignore_index=True)
    except:
        pass
    outer_df.drop_duplicates(inplace=True)
    return outer_df


if __name__ == "__main__":
    franchise_china_df = franchise_china()
    print(franchise_china_df)