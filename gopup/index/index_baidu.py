#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 0021
# @Author  : justin.郑 3907721@qq.com
# @File    : index_baidu.py
# @Desc    : 获取百度指数

from gopup.index.baidu_decrypt import decrypt_func, get_encrypt_json, format_data, get_key, format_data_feed, format_data_new
import pandas as pd
import requests
import datetime
import json
import math


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
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Cookie": cookie,
        "Host": "index.baidu.com",
        "Referer": "http://index.baidu.com/v2/main/index.html",
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
            "Host": "index.baidu.com",
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
            "Host": "index.baidu.com",
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
            "Host": "index.baidu.com",
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
            "Host": "index.baidu.com",
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
                "period": data['period'],
                "sim": word['sim']
            }
            res_list.append(tmp)
        df = pd.DataFrame(res_list)
        return df
    except:
        return None


def baidu_search_index(word, start_date, end_date, cookie, type="all"):
    # 百度搜索数据
    try:
        keywords_list = [[word]]
        encrypt_json = get_encrypt_json(
            start_date=start_date,
            end_date=end_date,
            keywords=keywords_list,
            type='search',
            area=0,
            cookies=cookie
        )

        encrypt_datas = encrypt_json['data']['userIndexes']
        uniqid = encrypt_json['data']['uniqid']

        result = []
        key = get_key(uniqid, cookie)
        for encrypt_data in encrypt_datas:
            encrypt_data[type]['data'] = decrypt_func(key, encrypt_data[type]['data'])

            for formated_data in format_data(encrypt_data, kind=type):
                result.append(formated_data)
                # yield formated_data

        data_df = pd.DataFrame(result)
        data_df.index = pd.to_datetime(data_df["date"])
        del data_df["date"]
        return data_df
    except Exception as e:
        return None


def baidu_info_index(word, start_date, end_date, cookie):
    # 百度资讯指数
    try:
        keywords_list = [[word]]
        encrypt_json = get_encrypt_json(
            start_date=start_date,
            end_date=end_date,
            keywords=keywords_list,
            type='feed',
            area=0,
            cookies=cookie
        )

        encrypt_datas = encrypt_json['data']['index']
        uniqid = encrypt_json['data']['uniqid']

        result = []
        key = get_key(uniqid, cookie)
        for encrypt_data in encrypt_datas:
            encrypt_data['data'] = decrypt_func(key, encrypt_data['data'])

            for formated_data in format_data_feed(encrypt_data):
                result.append(formated_data)
                # yield formated_data

        data_df = pd.DataFrame(result)
        data_df.index = pd.to_datetime(data_df["date"])
        del data_df["date"]
        return data_df
    except Exception as e:
        return None


def baidu_media_index(word, start_date, end_date, cookie):
    # 百度媒体指数
    try:
        keywords_list = [[word]]
        encrypt_json = get_encrypt_json(
            start_date=start_date,
            end_date=end_date,
            keywords=keywords_list,
            type='news',
            area=0,
            cookies=cookie
        )

        encrypt_datas = encrypt_json['data']['index']
        uniqid = encrypt_json['data']['uniqid']

        result = []
        key = get_key(uniqid, cookie)
        for encrypt_data in encrypt_datas:
            encrypt_data['data'] = decrypt_func(key, encrypt_data['data'])

            for formated_data in format_data_new(encrypt_data):
                result.append(formated_data)
                # yield formated_data

        data_df = pd.DataFrame(result)
        data_df.index = pd.to_datetime(data_df["date"])
        del data_df["date"]
        return data_df
    except Exception as e:
        return None


if __name__ == "__main__":
    cookie = '''BIDUPSID=512FE19892358D21D38C8FC50F5F37F7; PSTM=1660901365; BAIDUID=53AD0CE37FCDB36D9D1B39A93FE374F4:SL=0:NR=10:FG=1; MCITY=-218:; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1669711408; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04197989677NThjerC/uBmfwE7gLBzI02yJ8yNHTsFzC9Mvw15Giipt5mNfYGiOJJaietrqN/yfiAZ2wyc7wrxZIM4AmuC8T0Uype0oc+iT0eomfpv0bxF01EuH3GfRaLWOggGR0cJlqQQkCeNva3/6/Oeo8zaFYyF9aOYLP6MJTgThglmKM5W4+pZJdfSoe/1AC5rcykOV7L3ITsi5rOHnbcY8qWnLQrxLE501xT/LNe8/AgZ9rwxIqndsPDy48Cers3z9jAhNNSAhioe0SxpZYP6UA2+zbU+HLjUjs/r3JZ9oTHD4y74rmI2+I/6wivNS5UW0bwlsGeCjCrgtJEZV64q3l0KMuQ==21051097423431534993178797661057; __cas__rn__=419798967; BDUSS=H5mRnBLV1VKRDJjN2V4U0ItYk1NTTh3cGFrci1aWFk1dThVc0h1TWdLdVhlSzVqSVFBQUFBJCQAAAAAAAAAAAEAAABU8PMTst24-dauw~cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJfrhmOX64ZjT; __cas__st__212=46422731375e77016d42f24b466a2923fe6c883e0d40204c45fafe3607ba75de77b8a818b4cf1d4bd1f13da3; __cas__id__212=42043514; CPID_212=42043514; CPTK_212=465825438; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc={"uid_":{"value":"334753876","scope":1}}; bdindexid=c181tsmjr0t61fj5lnkvm89g92; delPer=0; PSINO=7; BA_HECTOR=8g8l0001012k8k018k2kafde1hods3f1g; BAIDUID_BFESS=53AD0CE37FCDB36D9D1B39A93FE374F4:SL=0:NR=10:FG=1; ZFY=W6cfbp666Zmh5e59gDgWLr71gsDxBHze7zwUqW12dc0:C; ZD_ENTRY=baidu; __bid_n=184c7598aa6179061b4207; H_PS_PSSID=37856_36552_37513_37491_37831_37841_37766_37802_37761_37850_26350_22157; RT="z=1&dm=baidu.com&si=53c9ba06-3f80-461c-95a4-254c3ebba8fc&ss=lb3lgacz&sl=2&tt=1wn&bcn=https://fclog.baidu.com/log/weirwood?type=perf"; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1669809498; ab_sr=1.0.1_YTVjZTBhZDNlNzg2NjUxZDg0NWFkMGE1YTY0NzVlYzA1ZTg4OTZhZGU1ZGIyNjhlNzVjNTA1YTY4OTE4ZmE5NDExODI3NWZhZGI1YWVlODZkMDEwMzhmNmZjNWMwZmE0ZjIzMDljNTgzMTQ1ZDhjZWMzYzM1YjBlZWU1ZmY2MDY1MmU4YTUwNzNmNWJiODZhMDhkZDM0ZWNlYzRkNjNjZg==; BDUSS_BFESS=H5mRnBLV1VKRDJjN2V4U0ItYk1NTTh3cGFrci1aWFk1dThVc0h1TWdLdVhlSzVqSVFBQUFBJCQAAAAAAAAAAAEAAABU8PMTst24-dauw~cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJfrhmOX64ZjT'''
    data = baidu_search_index(word="极限挑战", start_date='2022-09-01', end_date='2022-09-19', cookie=cookie)
    # data = baidu_atlas_index(word="极限挑战", cookie=cookie)
    print(data)



