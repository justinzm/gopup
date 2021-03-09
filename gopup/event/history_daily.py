#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 0020
# @Author  : justin.郑 3907721@qq.com
# @File    : history_daily.py
# @Desc    : 历史上的今日

import json
import pandas as pd
import requests


def history_daily():
    """
    历史上的今日
    Returns
    -------
    DataFrame
        "year，title, type, link, desc""
    """
    try:
        url = "https://www.bjsoubang.com/api/getHistoryDaily"
        r = requests.get(url=url)
        res_list = json.loads(r.text)['info']
        df = pd.DataFrame(res_list)
        df = df.drop(['cover', 'festival', 'recommend'], axis=1)
        return df
    except:
        return None
 

if __name__ == "__main__":
    tmp = history_daily()
    print(tmp)

