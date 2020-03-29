#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 17:31
# @Author  : justin.郑 3907721@qq.com
# @File    : classifying.py
# @Desc    : 股票分类数据接口

import pandas as pd


def get_industry_classified(standard='sina'):
    df = pd.read_csv(ct.TSDATA_CLASS % (ct.P_TYPE['http'], ct.DOMAINS['oss'], 'industry_sw'),
                     dtype={'code': object})


if __name__ == "__main__":
    get_industry_classified()