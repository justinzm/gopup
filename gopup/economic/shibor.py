#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : shibor.py
# @Desc    : 利率数据
# 上海银行间同业拆放利率（Shibor）数据接口

import json
import pandas as pd
import numpy as np
import requests
from gopup.economic import cons
from gopup.utils import date_utils as du


def shibor_data():
    """
    获取上海银行间同业拆放利率（Shibor）

    Return
    ------
    date:日期
    ON:隔夜拆放利率
    1W:1周拆放利率
    2W:2周拆放利率
    1M:1个月拆放利率
    3M:3个月拆放利率
    6M:6个月拆放利率
    9M:9个月拆放利率
    1Y:1年拆放利率
    https://www.shibor.org/dqs/rest/cm-u-bk-shibor/ShiborHisExcel?lang=cn
    """
    try:
        url = 'https://www.shibor.org/dqs/rest/cm-u-bk-shibor/ShiborHisExcel?lang=cn'
        herder = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive"
        }

        r = requests.get(url, headers=herder)
        df = pd.read_excel(r.content)
        return df
    except Exception as e:
        return None


def shibor_quote_data(year=None):
    """
    获取Shibor银行报价数据
    Parameters
    ------
      year:年份(int)

    Return
    ------
    date:日期
    bank:报价银行名称
    ON:隔夜拆放利率
    ON_B:隔夜拆放买入价
    ON_A:隔夜拆放卖出价
    1W_B:1周买入
    1W_A:1周卖出
    2W_B:买入
    2W_A:卖出
    1M_B:买入
    1M_A:卖出
    3M_B:买入
    3M_A:卖出
    6M_B:买入
    6M_A:卖出
    9M_B:买入
    9M_A:卖出
    1Y_B:买入
    1Y_A:卖出
    """
    year = du.get_year() if year is None else year
    lab = cons.SHIBOR_TYPE['Quote']
    try:
        url = cons.SHIBOR_DATA_URL % (cons.P_TYPE['http'], cons.DOMAINS['shibor'],
                                      cons.PAGES['dw'], 'Quote',
                                      year, lab,
                                      year)
        herder = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive"
        }

        r = requests.get(url, headers=herder)
        df = pd.read_excel(r.content)
        df.columns = cons.SHIBOR_Q_COLS
        df['date'] = df['date'].map(lambda x: x.date())
        return df
    except:
        return None


def shibor_ma_data():
    """
    获取Shibor均值数据
    Return
    ------
    date:日期
       其它分别为各周期5、10、20均价
    """
    try:
        url = 'https://www.shibor.org/dqs/rest/cm-u-bk-shibor/ShiborMnHisExcel?lang=cn'
        herder = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive"
        }

        r = requests.get(url, headers=herder)
        df = pd.read_excel(r.content)
        return df
    except:
        return None


def lpr_data(startDate, endDate):
    """
    获取贷款市场报价利率（LPR）
    Parameters
    ------
      startDate:起止日期(str)
      endDate:截止日期(str)

    Return
    ------
    showDateCN:日期
    1Y:1年贷款基础利率
    5Y:5年贷款基础利率
    """

    try:
        url = cons.LPR_DATA_URL

        herder = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive"
        }

        data = {
            "lang": "CN",
            "strStartDate": startDate,
            "strEndDate": endDate
        }

        r = requests.post(url, data=data, headers=herder)
        data_dict = json.loads(r.text)['records']
        df = pd.DataFrame(data_dict)
        return df
    except:
        return None


if __name__ == "__main__":
    tmp = shibor_data()
    print(tmp)
 

