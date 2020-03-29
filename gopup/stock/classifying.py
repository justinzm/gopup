#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 17:31
# @Author  : justin.郑 3907721@qq.com
# @File    : classifying.py
# @Desc    : 股票分类数据接口

import pandas as pd


def get_industry_classified(standard='sina'):
    """
        获取行业分类数据
    Parameters
    ----------
    standard
    sina:新浪行业 sw：申万 行业

    Returns
    -------
    DataFrame
        code :股票代码
        name :股票名称
        c_name :行业名称
    """
    if standard == 'sw':
        df = pd.read_csv('https://github.com/justinzm/gopup/blob/master/data/industry_sw.csv',
                        dtype={'code': object})
    else:
        df = pd.read_csv('https://github.com/justinzm/gopup/blob/master/data/industry.csv',
                         dtype={'code': object})
    return df


if __name__ == "__main__":
    tmp = get_industry_classified('sw')
    print(tmp)