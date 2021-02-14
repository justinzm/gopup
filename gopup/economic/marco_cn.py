#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 0024
# @Author  : justin.郑 3907721@qq.com
# @File    : marco_cn.py
# @Desc    : 中国宏观数据

import pandas as pd
import numpy as np
import re
import json
import requests
from gopup.economic import cons


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


def get_gdp_quarter():
    """
    获取季度国内生产总值数据
    --------
    DataFrame
        month :统计月份
        cpi : "季度", "国内生产总值 绝对值(亿元)", "国内生产总值 同比增长", "第一产业 绝对值(亿元)", "第一产业 同比增长", "第二产业 绝对值(亿元)", "第二产业 同比增长", "第三产业 绝对值(亿元)", "第三产业 同比增长"
    """
    url = "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx"
    params = {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "20"
    }
    r = requests.get(url=url, params=params)
    data_text = r.text
    tmp_list = data_text[data_text.find("[")+2: -3]
    tmp_list = tmp_list.split('","')
    res_list = []
    for li in tmp_list:
        res_list.append(li.split(','))
    columns = ["季度", "国内生产总值 绝对值(亿元)", "国内生产总值 同比增长", "第一产业 绝对值(亿元)", "第一产业 同比增长", "第二产业 绝对值(亿元)", "第二产业 同比增长", "第三产业 绝对值(亿元)", "第三产业 同比增长"]
    data_df = pd.DataFrame(res_list, columns=columns)
    return data_df


def get_cpi():
    """
        获取居民消费价格指数数据（CPI）
    --------
    DataFrame
        month :统计月份
        cpi : "月份", "全国当月", "全国同比增长", "全国环比增长", "全国累计", "城市当月", "城市同比增长", "城市环比增长", "城市累计", "农村当月", "农村同比增长", "农村环比增长", "农村累计"
    """
    url = "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx"
    params = {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "19"
    }
    r = requests.get(url=url, params=params)
    data_text = r.text
    tmp_list = data_text[data_text.find("[")+2: -3]
    tmp_list = tmp_list.split('","')
    res_list = []
    for li in tmp_list:
        res_list.append(li.split(','))
    columns = ["月份", "全国当月", "全国同比增长", "全国环比增长", "全国累计", "城市当月", "城市同比增长", "城市环比增长", "城市累计", "农村当月", "农村同比增长", "农村环比增长", "农村累计"]
    data_df = pd.DataFrame(res_list, columns=columns)
    return data_df


def get_ppi():
    """
        获取工业品出厂价格指数数据
    --------
    DataFrame
        "月份", "当月", "当月同比增长", "累计"
    """
    url = "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx"
    params = {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "22"
    }
    r = requests.get(url=url, params=params)
    data_text = r.text
    tmp_list = data_text[data_text.find("[") + 2: -3]
    tmp_list = tmp_list.split('","')
    res_list = []
    for li in tmp_list:
        res_list.append(li.split(','))
    columns = ["月份", "当月", "当月同比增长", "累计"]
    data_df = pd.DataFrame(res_list, columns=columns)
    return data_df


def get_pmi():
    """
        获取采购经理人指数(PMI)
    --------
    DataFrame
        "月份", "制造业指数", "制造业同比增长", "非制造业指数", "非制造业同比增长"
    """
    url = "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx"
    params = {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "21"
    }
    r = requests.get(url=url, params=params)
    data_text = r.text
    tmp_list = data_text[data_text.find("[") + 2: -3]
    tmp_list = tmp_list.split('","')
    res_list = []
    for li in tmp_list:
        res_list.append(li.split(','))
    columns = ["月份", "制造业指数", "制造业同比增长", "非制造业指数", "非制造业同比增长"]
    data_df = pd.DataFrame(res_list, columns=columns)
    return data_df


def get_rrr():
    """
        获取存款准备金率数据
    --------
    DataFrame
        "公布时间", "生效时间", "大型金融机构 调整前", "大型金融机构 调整后", "大型金融机构 调整幅度", "中小型金融机构 调整前", "中小型金融机构 调整后", "中小型金融机构 调整幅度", "备注", "消息公布次日指数涨跌 上证", "消息公布次日指数涨跌 深证"
    """
    url = "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx"
    params = {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "23"
    }
    r = requests.get(url=url, params=params)
    data_text = r.text
    tmp_list = data_text[data_text.find("[") + 2: -3]
    tmp_list = tmp_list.split('","')
    res_list = []
    for li in tmp_list:
        res_list.append(li.split(','))
    columns = ["公布时间", "生效时间", "大型金融机构 调整前", "大型金融机构 调整后", "大型金融机构 调整幅度", "中小型金融机构 调整前", "中小型金融机构 调整后", "中小型金融机构 调整幅度", "备注", "消息公布次日指数涨跌 上证", "消息公布次日指数涨跌 深证"]
    data_df = pd.DataFrame(res_list, columns=columns)
    return data_df


def get_money_supply():
    """
        获取货币供应量数据
    --------
    DataFrame
        "月份", "货币和准货币(M2) 数量(亿元)", "货币和准货币(M2) 同比增长", "货币和准货币(M2) 环比增长", "货币(M1) 数量(亿元)", "货币(M1) 同比增长	", "货币(M1) 环比增长", "流通中的现金(M0) 数量(亿元)", "流通中的现金(M0) 同比增长", "流通中的现金(M0) 环比增长"
    """
    url = "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx"
    params = {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "11"
    }
    r = requests.get(url=url, params=params)
    data_text = r.text
    tmp_list = data_text[data_text.find("[") + 2: -3]
    tmp_list = tmp_list.split('","')
    res_list = []
    for li in tmp_list:
        res_list.append(li.split(','))
    columns = ["月份", "货币和准货币(M2) 数量(亿元)", "货币和准货币(M2) 同比增长", "货币和准货币(M2) 环比增长", "货币(M1) 数量(亿元)", "货币(M1) 同比增长	", "货币(M1) 环比增长", "流通中的现金(M0) 数量(亿元)", "流通中的现金(M0) 同比增长", "流通中的现金(M0) 环比增长"]
    data_df = pd.DataFrame(res_list, columns=columns)
    return data_df


def get_gold_and_foreign_reserves():
    """
    获取外汇储备
    Returns
    -------
    DataFrame
        "月份", "国家外汇储备(亿美元) 数值", "国家外汇储备(亿美元) 同比", "国家外汇储备(亿美元) 环比", "黄金储备(万盎司) 数值", "黄金储备(万盎司) 同比", "黄金储备(万盎司) 环比"
    """
    url = "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx"
    params = {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "16"
    }
    r = requests.get(url=url, params=params)
    data_text = r.text
    tmp_list = data_text[data_text.find("[") + 2: -3]
    tmp_list = tmp_list.split('","')
    res_list = []
    for li in tmp_list:
        res_list.append(li.split(','))
    columns = ["月份", "国家外汇储备(亿美元) 数值", "国家外汇储备(亿美元) 同比", "国家外汇储备(亿美元) 环比", "黄金储备(万盎司) 数值", "黄金储备(万盎司) 同比", "黄金储备(万盎司) 环比"]
    data_df = pd.DataFrame(res_list, columns=columns)
    return data_df


# 0.3.2
def get_industrial_growth():
    """
    获取工业增加值增长
    Returns
    -------
    DataFrame
        "月份", "同比增长%", "累计增长%"
    """
    url = "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx"
    params = {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "0"
    }
    r = requests.get(url=url, params=params)
    data_text = r.text
    tmp_list = data_text[data_text.find("[") + 2: -3]
    tmp_list = tmp_list.split('","')
    res_list = []
    for li in tmp_list:
        res_list.append(li.split(','))
    columns = ["月份", "同比增长%", "累计增长%"]
    data_df = pd.DataFrame(res_list, columns=columns)
    return data_df


def get_fiscal_revenue():
    """
    获取财政收入
    Returns
    -------
    DataFrame
        "月份、当月(亿元)、同比增长、环比增长、累计(亿元)、同比增长"
    """
    url = "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx"
    params = {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "14"
    }
    r = requests.get(url=url, params=params)
    data_text = r.text
    tmp_list = data_text[data_text.find("[") + 2: -3]
    tmp_list = tmp_list.split('","')
    res_list = []
    for li in tmp_list:
        res_list.append(li.split(','))
    columns = ["月份", "当月(亿元)", "同比增长", "环比增长", "累计(亿元)", "同比增长"]
    data_df = pd.DataFrame(res_list, columns=columns)
    return data_df


def get_consumer_total():
    """
    获取社会消费品零售总额
    Returns
    -------
    DataFrame
        "月份、当月(亿元)、同比增长、环比增长、累计(亿元)、同比增长"
    """
    url = "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx"
    params = {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "5"
    }
    r = requests.get(url=url, params=params)
    data_text = r.text
    tmp_list = data_text[data_text.find("[") + 2: -3]
    tmp_list = tmp_list.split('","')
    res_list = []
    for li in tmp_list:
        res_list.append(li.split(','))
    columns = ["月份", "当月(亿元)", "同比增长", "环比增长", "累计(亿元)", "同比增长"]
    data_df = pd.DataFrame(res_list, columns=columns)
    return data_df


def get_credit_data():
    """
    获取信贷数据
    Returns
    -------
    DataFrame
        "月份、当月(亿元)、同比增长、环比增长、累计(亿元)、同比增长"
    """
    url = "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx"
    params = {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "7"
    }
    r = requests.get(url=url, params=params)
    data_text = r.text
    tmp_list = data_text[data_text.find("[") + 2: -3]
    tmp_list = tmp_list.split('","')
    res_list = []
    for li in tmp_list:
        res_list.append(li.split(','))
    columns = ["月份", "当月(亿元)", "同比增长", "环比增长", "累计(亿元)", "同比增长"]
    data_df = pd.DataFrame(res_list, columns=columns)
    return data_df


def get_fdi_data():
    """
    获取外商直接投资数据(FDI)
    Returns
    -------
    DataFrame
        "月份、当月(亿元)、同比增长、环比增长、累计(亿元)、同比增长"
    """
    url = "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx"
    params = {
        "type": "GJZB",
        "sty": "ZGZB",
        "p": "1",
        "ps": "200",
        "mkt": "15"
    }
    r = requests.get(url=url, params=params)
    data_text = r.text
    tmp_list = data_text[data_text.find("[") + 2: -3]
    tmp_list = tmp_list.split('","')
    res_list = []
    for li in tmp_list:
        res_list.append(li.split(','))
    columns = ["月份", "当月(十万元)", "同比增长", "环比增长", "累计(十万元)", "同比增长"]
    data_df = pd.DataFrame(res_list, columns=columns)
    # data_df['当月(亿元)'] = data_df['当月(亿元)'].map(lambda x: int(x)/100000)
    # data_df['累计(亿元)'] = data_df['累计(亿元)'].map(lambda x: int(x)/100000)
    return data_df


if __name__ == '__main__':
    tmp = get_fdi_data()
    print(tmp)

