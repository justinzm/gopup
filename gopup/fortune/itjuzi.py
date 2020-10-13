#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 16:58
# @Author  : justin.郑 3907721@qq.com
# @File    : itjuzi.py
# @Desc    : IT桔子

import pandas as pd
import requests
from gopup.fortune.cons import it_url, it_headers


def death_company():
    """
    倒闭公司
    https://www.itjuzi.com/deathCompany
    :return: pandas.DataFrame
    """
    temp_df = pd.read_csv(it_url, index_col=0)
    for i in range(1, 3):
        json_url = (
            f"https://www.itjuzi.com/api/closure?com_prov=&fund_status=&sort=&page={i}"
        )
        data_json = requests.get(url=json_url, headers=it_headers).json()
        data_df = data_json["data"]["info"]
        data_df = pd.DataFrame(data_df)
        data_df = data_df[
            [
                "com_name",
                "born",
                "com_change_close_date",
                "live_time",
                "total_money",
                "cat_name",
                "com_prov",
            ]
        ]
        temp_df = temp_df.append(data_df, ignore_index=True)
        temp_df.drop_duplicates(inplace=True)
    return temp_df


def nicorn_company():
    """
    独角兽公司
    :return: pandas.DataFrame
    """
    temp_df = pd.read_csv(
        "https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/data/data_juzi/nicorn_company.csv",
        index_col=0,
    )
    for i in range(1, 2):
        json_url = f"https://www.itjuzi.com/api/nicorn?page={i}&com_prov=&cat_id=&order_id=1&com_name="
        data_json = requests.get(url=json_url, headers=it_headers).json()
        data_df = data_json["data"]["data"]
        data_df = pd.DataFrame(data_df)
        temp_df = temp_df.append(data_df, ignore_index=True)
        temp_df.drop_duplicates(inplace=True)
    return temp_df


def maxima_company():
    """
    千里马公司
    :return: pandas.DataFrame
    """
    temp_df = pd.read_csv(
        "https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/data/data_juzi/maxima.csv",
        index_col=0,
    )
    temp_df.head().append(temp_df.tail())
    for i in range(1, 2):
        json_url = f"https://www.itjuzi.com/api/maxima/?page={i}&com_prov=&cat_id=&order_id=1&com_name="
        data_json = requests.get(url=json_url, headers=it_headers).json()
        data_df = data_json["data"]["data"]
        data_df = pd.DataFrame(data_df)
        temp_df = temp_df.append(data_df, ignore_index=True)
        temp_df.drop_duplicates(inplace=True)
    return temp_df


if __name__ == "__main__":
    death_company_df = death_company()
    print(death_company_df)
    nicorn_company_df = nicorn_company()
    print(nicorn_company_df)
    maxima_company_df = maxima_company()
    print(maxima_company_df)