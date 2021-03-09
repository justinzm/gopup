#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 0019
# @Author  : justin.郑 3907721@qq.com
# @File    : index_sogou.py
# @Desc    : 搜狗指数

import json
import pandas as pd
import requests
from gopup.index.cons import index_toutiao_headers


def sogou_index(keyword, start_date, end_date, data_type="SEARCH_ALL"):
    """
    搜狗指数趋势数据
    :param keyword:     关键词
    :param start_date:  开始日期
    :param end_date:    截止日期
    :param data_type:   指数趋势
    :return:
        datetime    日期
        index       指数
    """

    # SEARCH_ALL 整体趋势  SEARCH_PC PC趋势  SEARCH_WAP 移动趋势
    try:
        url = "http://zhishu.sogou.com/getDateData?kwdNamesStr=%s&startDate=%s&endDate=%s&dataType=%s&queryType=INPUT" % (keyword, start_date, end_date, data_type)

        res = requests.get(url, headers=index_toutiao_headers)
        pv_list = json.loads(res.text)['data']['pvList'][0]
        df = pd.DataFrame(pv_list)
        df['index'] = df['pv']
        df = df.drop(['kwdId', 'isPeak', 'id', 'pv'], axis=1)
        return df
    except:
        return None


if __name__ == "__main__":
    sogou_index(keyword="耐克", start_date="20210101", end_date="20210218")

