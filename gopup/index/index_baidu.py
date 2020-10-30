#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 0021
# @Author  : justin.郑 3907721@qq.com
# @File    : index_baidu.py
# @Desc    : 获取百度指数
import json

import pandas as pd
import requests


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


def baidu_interest_index(word, cookie):
    """
    百度指数 人群画像兴趣分布
    :param word: 关键词
    :param cookie:
    :return:
        desc    兴趣分类
        tgi     TGI指数
        word_rate   关键词分布比率
        all_rate    全网分布比率
        period      周期范围
    """
    try:
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
        url = "http://index.baidu.com/api/SocialApi/interest?wordlist[]=%s" % word
        r = requests.get(url=url, headers=headers)
        data = json.loads(r.text)['data']
        period = "%s|%s" % (data['startDate'], data['endDate'])

        age_list = data['result'][0]['interest']
        age_df = pd.DataFrame(age_list)

        all_list = data['result'][1]['interest']
        all_df = pd.DataFrame(all_list)
        all_df.drop(["tgi", "typeId"], axis=1, inplace=True)

        res_df = pd.merge(age_df, all_df, on='desc')
        res_df['period'] = period
        res_df.drop(["typeId"], axis=1, inplace=True)
        res_df.rename(columns={'rate_x': 'word_rate', 'rate_y': 'all_rate'}, inplace=True)
        return res_df
    except:
        return None


def baidu_gender_index(word, cookie):
    """
    百度指数 人群画像性别分布
    :param word: 关键词
    :param cookie:
    :return:
        desc    性别
        tgi     TGI指数
        word_rate   关键词分布比率
        all_rate    全网分布比率
        period      周期范围
    """
    try:
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
        url = "http://index.baidu.com/api/SocialApi/baseAttributes?wordlist[]=%s" % word
        r = requests.get(url=url, headers=headers)
        data = json.loads(r.text)['data']
        period = "%s|%s" % (data['startDate'], data['endDate'])

        age_list = data['result'][0]['gender']
        age_df = pd.DataFrame(age_list)

        all_list = data['result'][1]['gender']
        all_df = pd.DataFrame(all_list)
        all_df.drop(["tgi", "typeId"], axis=1, inplace=True)

        res_df = pd.merge(age_df, all_df, on='desc')
        res_df['period'] = period
        res_df.drop(["typeId"], axis=1, inplace=True)
        res_df.rename(columns={'rate_x': 'word_rate', 'rate_y': 'all_rate'}, inplace=True)
        return res_df
    except:
        return None


def baidu_age_index(word, cookie):
    """
    百度指数 人群画像年龄分布
    :param word: 关键词
    :param cookie:
    :return:
        desc    年龄范围
        tgi     TGI指数
        word_rate   关键词分布比率
        all_rate    全网分布比率
        period      周期范围
    """
    try:
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
        url = "http://index.baidu.com/api/SocialApi/baseAttributes?wordlist[]=%s" % word
        r = requests.get(url=url, headers=headers)
        data = json.loads(r.text)['data']
        period = "%s|%s" % (data['startDate'], data['endDate'])

        age_list = data['result'][0]['age']
        age_df = pd.DataFrame(age_list)

        all_list = data['result'][1]['age']
        all_df = pd.DataFrame(all_list)
        all_df.drop(["tgi", "typeId"], axis=1, inplace=True)

        res_df = pd.merge(age_df, all_df, on='desc')
        res_df['period'] = period
        res_df.drop(["typeId"], axis=1, inplace=True)
        res_df.rename(columns={'rate_x': 'word_rate', 'rate_y': 'all_rate'}, inplace=True)
        return res_df
    except:
        return None


def baidu_atlas_index(word, cookie, date=None):
    """
    百度指数 需求图谱
    :param word: 关键词
    :param cookie:
    :param date: 周期
    :return:
        period  周期范围
        word    相关词
        pv      搜索热度
        ratio   搜索变化率
    """

    try:
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
        if date == None:
            date = ""
        url = "http://index.baidu.com/api/WordGraph/multi?wordlist[]=%s&datelist=%s" % (word, date)
        r = requests.get(url=url, headers=headers)
        data = json.loads(r.text)['data']
        wordlist = data['wordlist'][0]['wordGraph']
        res_list = []
        for word in wordlist:
            tmp = {
                "word": word['word'],
                "pv": word['pv'],
                "ratio": word['ratio'],
                "period": data['period']
                # "sim": word['sim']
            }
            res_list.append(tmp)
        df = pd.DataFrame(res_list)
        return df
    except:
        return None


def baidu_search_index(word, start_date, end_date, cookie):
    # 趋势研究
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
    cookie = 'BIDUPSID=F7EB2ABF6DC23E3AE0D29AD77AC3A828; PSTM=1550065926; H_WISE_SIDS=135670_136721_137754_138181_138497_114745_128149_139148_120168_138471_138878_137978_137690_131246_132551_118883_118873_118847_118829_118790_138165_138883_136431_138845_138697_136862_138146_138114_139172_139592_136196_137105_139273_139398_139691_133847_137735_138343_137467_138564_134256_131423_139397_139090_139246_137782_138657_136537_110085_137441_127969_139161_138837_139287_139407_127417_137186_136635_138426_139733_138941_139677_139221_138779; bdshare_firstime=1580385892027; BAIDUID=BECC251AF81F5D6642279AA52D2B4069:FG=1; MCITY=-218%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=NKRHNYcTVELWM4TFd4SGFUYng3ZkRsb3Q2RHRuRVBZRXc4TkVkWk96bUctY0ZmSVFBQUFBJCQAAAAAAAAAAAEAAABU8PMTst24-dauw~cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIZsml-GbJpfOH; delPer=0; PSINO=7; BA_HECTOR=2h0haga1258525e07i1fpnavq0k; H_PS_PSSID=32818_1441_32843_31254_32972_7517_32115_31709_32915; ZD_ENTRY=baidu; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1602223107,1604039250; bdindexid=qf316t4v2ap0sliptu9n1nm821; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1604039863; __yjsv5_shitong=1.0_7_835dba6616d254eab5e9498efc28ecbfaa90_300_1604039721016_111.175.93.198_5928ee1f; RT="z=1&dm=baidu.com&si=v9wmb9z1ug&ss=kgvvjxki&sl=g&tt=kol&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=kzph"'
    data = baidu_interest_index(word="王者荣耀", cookie=cookie)
    print(data)



