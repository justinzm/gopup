#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 0021
# @Author  : justin.郑 3907721@qq.com
# @File    : index_baidu.py
# @Desc    : 获取百度指数
 

import matplotlib.pyplot as plt
import pandas as pd
import requests

plt.rcParams["font.sans-serif"] = ["SimHei"]


def decrypt(t: str, e: str) -> str:
    """
    解密函数
    :param t:
    :type t:
    :param e:
    :type e:
    :return:
    :rtype:
    """
    n, i, a, result = list(t), list(e), {}, []
    ln = int(len(n) / 2)
    start, end = n[ln:], n[:ln]
    a = dict(zip(end, start))
    return "".join([a[j] for j in e])


def get_ptbk(uniqid: str, cookie: str) -> str:
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Cookie": cookie,
        "DNT": "1",
        "Host": "zhishu.baidu.com",
        "Pragma": "no-cache",
        "Proxy-Connection": "keep-alive",
        "Referer": "zhishu.baidu.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    session = requests.Session()
    session.headers.update(headers)
    with session.get(
        url=f"http://index.baidu.com/Interface/ptbk?uniqid={uniqid}"
    ) as response:
        ptbk = response.json()["data"]
        return ptbk


def baidu_search_index(word, start_date, end_date, cookie):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Cookie": cookie,
        "DNT": "1",
        "Host": "zhishu.baidu.com",
        "Pragma": "no-cache",
        "Proxy-Connection": "keep-alive",
        "Referer": "zhishu.baidu.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    session = requests.Session()
    session.headers.update(headers)
    with session.get(
        url=f"http://index.baidu.com/api/SearchApi/index?word={word}&area=0&startDate={start_date}&endDate={end_date}"
    ) as response:
        data = response.json()["data"]
        all_data = data["userIndexes"][0]["all"]["data"]
        uniqid = data["uniqid"]
        ptbk = get_ptbk(uniqid, cookie)
        result = decrypt(ptbk, all_data).split(",")
        result = [int(item) if item != "" else 0 for item in result]
        if len(result) == len(pd.date_range(start=start_date, end=end_date, freq="7D")):
            temp_df_7 = pd.DataFrame(
                [pd.date_range(start=start_date, end=end_date, freq="7D"), result],
                index=["date", word],
            ).T
            temp_df_7.index = pd.to_datetime(temp_df_7["date"])
            del temp_df_7["date"]
            return temp_df_7
        else:
            temp_df_1 = pd.DataFrame(
                [pd.date_range(start=start_date, end=end_date, freq="1D"), result],
                index=["date", word],
            ).T
            temp_df_1.index = pd.to_datetime(temp_df_1["date"])
            del temp_df_1["date"]
            return temp_df_1


def baidu_info_index(word, start_date, end_date, cookie):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Cookie": cookie,
        "DNT": "1",
        "Host": "zhishu.baidu.com",
        "Pragma": "no-cache",
        "Proxy-Connection": "keep-alive",
        "Referer": "zhishu.baidu.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    session = requests.Session()
    session.headers.update(headers)
    with session.get(
        url=f"http://index.baidu.com/api/FeedSearchApi/getFeedIndex?word={word}&area=0&startDate={start_date}&endDate={end_date}"
    ) as response:
        data = response.json()["data"]
        all_data = data["index"][0]["data"]
        uniqid = data["uniqid"]
        ptbk = get_ptbk(uniqid, cookie)
        result = decrypt(ptbk, all_data).split(",")
        result = [int(item) if item != "" else 0 for item in result]
        if len(result) == len(pd.date_range(start=start_date, end=end_date, freq="7D")):
            temp_df_7 = pd.DataFrame(
                [pd.date_range(start=start_date, end=end_date, freq="7D"), result],
                index=["date", word],
            ).T
            temp_df_7.index = pd.to_datetime(temp_df_7["date"])
            del temp_df_7["date"]
            return temp_df_7
        else:
            temp_df_1 = pd.DataFrame(
                [pd.date_range(start=start_date, end=end_date, freq="1D"), result],
                index=["date", word],
            ).T
            temp_df_1.index = pd.to_datetime(temp_df_1["date"])
            del temp_df_1["date"]
            return temp_df_1


def baidu_media_index(word, start_date, end_date, cookie):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Cookie": cookie,
        "DNT": "1",
        "Host": "zhishu.baidu.com",
        "Pragma": "no-cache",
        "Proxy-Connection": "keep-alive",
        "Referer": "zhishu.baidu.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    session = requests.Session()
    session.headers.update(headers)
    with session.get(
        url=f"http://index.baidu.com/api/NewsApi/getNewsIndex?word={word}&area=0&startDate={start_date}&endDate={end_date}"
    ) as response:
        data = response.json()["data"]
        all_data = data["index"][0]["data"]
        uniqid = data["uniqid"]
        ptbk = get_ptbk(uniqid, cookie)
        result = decrypt(ptbk, all_data).split(",")
        result = ["0" if item == "" else item for item in result]
        result = [int(item) for item in result]
        if len(result) == len(pd.date_range(start=start_date, end=end_date, freq="7D")):
            temp_df_7 = pd.DataFrame(
                [pd.date_range(start=start_date, end=end_date, freq="7D"), result],
                index=["date", word],
            ).T
            temp_df_7.index = pd.to_datetime(temp_df_7["date"])
            del temp_df_7["date"]
            return temp_df_7
        else:
            temp_df_1 = pd.DataFrame(
                [pd.date_range(start=start_date, end=end_date, freq="1D"), result],
                index=["date", word],
            ).T
            temp_df_1.index = pd.to_datetime(temp_df_1["date"])
            del temp_df_1["date"]
            return temp_df_1


if __name__ == "__main__":
    cookie = "F7EB2ABF6DC23E3AE0D29AD77AC3A828; PSTM=1550065926; BAIDUID=7595D1FDD779944C2A288CBAD9865244:FG=1; H_WISE_SIDS=135670_136721_137754_138181_138497_114745_128149_139148_120168_138471_138878_137978_137690_131246_132551_118883_118873_118847_118829_118790_138165_138883_136431_138845_138697_136862_138146_138114_139172_139592_136196_137105_139273_139398_139691_133847_137735_138343_137467_138564_134256_131423_139397_139090_139246_137782_138657_136537_110085_137441_127969_139161_138837_139287_139407_127417_137186_136635_138426_139733_138941_139677_139221_138779; MCITY=-218%3A; bdshare_firstime=1580385892027; BDUSS=2JKVDg5clpLUGI2QzRnQmxtdGtad3VUSHVJN0VGQjNwSn5Ub2NSS1BRNnlsMTllRVFBQUFBJCQAAAAAAAAAAAEAAABU8PMTst24-dauw~cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALIKOF6yCjheU; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=6; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1584712811; bdindexid=dmkg48p5ip10oj5u1cif5k06e7; H_PS_PSSID=30973_1432_31121_21101_20692_30908_30824_31086_26350_22157; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1584760723"
    data = baidu_search_index(
        word="口罩", start_date="2020-01-01", end_date="2020-02-14", cookie=cookie
    )
    print(data)
    data.dropna(inplace=True)
    data.plot()
    plt.show()
    data = baidu_info_index(
        word="疫情", start_date="2020-01-01", end_date="2020-02-14", cookie=cookie
    )
    print(data)
    data.dropna(inplace=True)
    data.plot()
    plt.show()
    data = baidu_media_index(
        word="武汉", start_date="2020-01-01", end_date="2020-02-14", cookie=cookie
    )
    print(data)
    data.dropna(inplace=True)
    data.plot()
    plt.show()


