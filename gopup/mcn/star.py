#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 12:59
# @Author  : justin.郑 3907721@qq.com
# @File    : star.py
# @Desc    : 星图
# https://star.toutiao.com/
import math
import time
import requests
import pandas as pd
from gopup.mcn import cons
from gopup.utils.utils import get_fields


def star_hot_list(section, hot_list, category, cookie):
    """
    星图热榜 抖音达人热榜
    :param section:
    :param hot_list:
    :param category:
    :param cookie:
    :return:
    """
    # cookie = cons.STAR_COOKIE
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "referer": "https://star.toutiao.com/ad",
        "cookie": cookie
    }

    params = "%s-%s-%s" % (section, hot_list, category)
    try:
        url = cons.STAR_HOT_URL[params]
    except:
        return {"code": 401, "msg": "没有找到对应类型"}

    r = requests.get(url, headers=headers)

    publish_date = r.json()['data']['file_name'][-20:-1]
    data_all = r.json()['data']['stars']
    res_list = []
    new_rank = 1
    for data in data_all:
        res_dict = {
            "id": data['id'],
            "new_rank": new_rank,
            "nick_name": data['nick_name'],
            "avatar_uri": data['avatar_uri'],
            "province": data.setdefault('province'),
            "city": data['city'],
            "avg_play": data['avg_play'],
            "score": get_fields(data['fields'], "score"),
            "follower": get_fields(data['fields'], "follower"),
            "positive_vv": get_fields(data['fields'], "positive_vv"),
            "personal_interate_rate": get_fields(data['fields'], "personal_interate_rate"),
            "expected_cpm": get_fields(data['fields'], "expected_cpm"),
            "file_name": params,
            "publish_date": publish_date,
            "crawler_date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
        res_list.append(res_dict)
        new_rank += 1
    df = pd.DataFrame(res_list)
    return df


def star_market_list(section="抖音达人", market_list="抖音传播任务", category="全部", limit=30, page=1, cookie=None):
    """
    达人广场 抖音达人
    :param section:
    :param market_list:
    :param category:
    :return:
    """
    cookie = cons.STAR_COOKIE
    res_url = get_star_market_url(category, cookie)

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "referer": "https://star.toutiao.com/ad",
        "cookie": cookie
    }
    url = res_url % (limit, page)
    r = requests.get(url, headers=headers)
    try:
        res = r.json()['data']['authors']
    except:
        return {"msg": "cookie已经过期", "code": 401}
    return res


def get_star_market_url(category, cookie):
    limit = 10
    if category == "全部":
        url = "https://star.toutiao.com/v/api/demand/author_list/?limit=%s&need_detail=true&page=1&platform_source=1&task_category=1&order_by=score&use_recommend=1" % limit
        res_url = "https://star.toutiao.com/v/api/demand/author_list/?limit=%s&need_detail=true&page=%s&platform_source=1&task_category=1&order_by=score&use_recommend=1"
    else:
        category_list = cons.STAR_MARKET_DOUYIN_CATEGORY
        for cate in category_list:
            first_dict = cate['first']
            first_val = list(first_dict.values())[0]
            if category == first_val:
                tag = list(first_dict.keys())[0]
                url = "https://star.toutiao.com/v/api/demand/author_list/?limit=%s&need_detail=true&page=1&platform_source=1&task_category=1&tag=%s&order_by=score" % (
                limit, tag)
                res_url = "https://star.toutiao.com/v/api/demand/author_list/?limit=%s&need_detail=true&page=%s&platform_source=1&task_category=1&tag="+str(tag)+"&order_by=score"
            else:
                second_list = cate['second']
                for second_dict in second_list:
                    second_val = list(second_dict.values())[0]
                    if category == second_val:
                        tag = list(first_dict.keys())[0]
                        tag_level_two = list(second_dict.keys())[0]
                        url = "https://star.toutiao.com/v/api/demand/author_list/?limit=%s&need_detail=true&page=1&platform_source=1&task_category=1&tag=%s&tag_level_two=%s&order_by=score" % (limit, tag, tag_level_two)
                        res_url = "https://star.toutiao.com/v/api/demand/author_list/?limit=%s&need_detail=true&page=%s&platform_source=1&task_category=1&tag="+str(tag)+"&tag_level_two="+str(tag_level_two)+"&order_by=score"

    # headers = {
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    #     "referer": "https://star.toutiao.com/ad",
    #     "cookie": cookie
    # }
    #
    # r = requests.get(url, headers=headers)
    # total_count = r.json()['data']['pagination']['total_count']

    # return res_url, total_count
    return res_url


if __name__ == "__main__":
    # tmp = star_hot_list("抖音达人热榜", "星图指数榜", "财经投资")
    tmp = star_market_list(category="搞笑", limit=30, page=1)
    print(tmp)