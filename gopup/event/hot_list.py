#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 0020
# @Author  : justin.郑 3907721@qq.com
# @File    : hot_list.py
# @Desc    : 各类榜单

import json
import pandas as pd
import requests


def douban_movie_list():
    """
    豆瓣新片榜
    Returns
    -------
    DataFrame
        "titleCn, title，rate, link, img, description, ranking"
    """
    url = "https://www.bjsoubang.com/api/getChannelData"
    params = {
        "channel_id": 16
    }
    r = requests.get(url=url, params=params)
    res_list = json.loads(r.text)['info']['data']
    df = pd.DataFrame(res_list)
    df['ranking'] = df.index + 1
    return df


def douban_week_praise_list():
    """
    豆瓣一周口碑榜
    Returns
    -------
    DataFrame
        "title，trend, link, ranking"
    """
    url = "https://www.bjsoubang.com/api/getChannelData"
    params = {
        "channel_id": 19
    }
    r = requests.get(url=url, params=params)
    res_list = json.loads(r.text)['info']['data']
    df = pd.DataFrame(res_list)
    return df


def zhihu_hot_search_list():
    """
    知乎热搜榜
    Returns
    -------
    DataFrame
        "display_query，query, link, ranking"
    """
    url = "https://www.bjsoubang.com/api/getChannelData"
    params = {
        "channel_id": 10
    }
    r = requests.get(url=url, params=params)
    res_list = json.loads(r.text)['info']['data']
    df = pd.DataFrame(res_list)
    df['ranking'] = df.index + 1
    return df


def zhihu_hot_list():
    """
    知乎热榜
    Returns
    -------
    DataFrame
        "title, img，description, link, ranking, hot"
    """
    url = "https://www.bjsoubang.com/api/getChannelData"
    params = {
        "channel_id": 2
    }
    r = requests.get(url=url, params=params)
    res_list = json.loads(r.text)['info']['data']
    df = pd.DataFrame(res_list)
    df['ranking'] = df.index + 1
    return df


def wx_hot_word_list():
    """
    微信热词榜
    Returns
    -------
    DataFrame
        "title, link, hot_rank, ranking"
    """
    url = "https://www.bjsoubang.com/api/getChannelData"
    params = {
        "channel_id": 6
    }
    r = requests.get(url=url, params=params)
    res_list = json.loads(r.text)['info']['data']
    df = pd.DataFrame(res_list)
    df['ranking'] = df.index + 1
    return df


def wx_hot_list():
    """
    微信热门榜
    Returns
    -------
    DataFrame
        "title, img，description, link, ranking"
    """
    url = "https://www.bjsoubang.com/api/getChannelData"
    params = {
        "channel_id": 1
    }
    r = requests.get(url=url, params=params)
    res_list = json.loads(r.text)['info']['data']
    df = pd.DataFrame(res_list)
    df['ranking'] = df.index + 1
    return df


def weibo_hot_search_list():
    """
    微博热搜榜
    Returns
    -------
    DataFrame
        "title, tag, link, hot, ranking"
    """
    url = "https://www.bjsoubang.com/api/getChannelData"
    params = {
        "channel_id": 4
    }
    r = requests.get(url=url, params=params)
    res_list = json.loads(r.text)['info']['data']
    df = pd.DataFrame(res_list)
    df['ranking'] = df.index + 1
    return df


def weibo_new_era_list():
    """
    微博新时代榜
    Returns
    -------
    DataFrame
        "title, link, ranking"
    """
    url = "https://www.bjsoubang.com/api/getChannelData"
    params = {
        "channel_id": 5
    }
    r = requests.get(url=url, params=params)
    res_list = json.loads(r.text)['info']['data']
    df = pd.DataFrame(res_list)
    df['ranking'] = df.index + 1
    return df


def baidu_hot_list():
    """
    百度实时热点榜
    Returns
    -------
    DataFrame
        "title, id, status, link_video, link_search, link_news, link_img, hot, ranking"
    """
    url = "https://www.bjsoubang.com/api/getChannelData"
    params = {
        "channel_id": 3
    }
    r = requests.get(url=url, params=params)
    res_list = json.loads(r.text)['info']['data']
    df = pd.DataFrame(res_list)
    df['ranking'] = df.index + 1
    return df


def baidu_today_hot_list():
    """
    百度今日热点榜
    Returns
    -------
    DataFrame
        "title, id, status, link_video, link_search, link_news, link_img, hot, ranking"
    """
    url = "https://www.bjsoubang.com/api/getChannelData"
    params = {
        "channel_id": 12
    }
    r = requests.get(url=url, params=params)
    res_list = json.loads(r.text)['info']['data']
    df = pd.DataFrame(res_list)
    df['ranking'] = df.index + 1
    return df


def baidu_hot_word_list():
    """
    百度百科热词榜
    Returns
    -------
    DataFrame
        "title, link, status, description, ranking"
    """
    url = "https://www.bjsoubang.com/api/getChannelData"
    params = {
        "channel_id": 9
    }
    r = requests.get(url=url, params=params)
    res_list = json.loads(r.text)['info']['data']
    df = pd.DataFrame(res_list)
    df['ranking'] = df.index + 1
    return df


if __name__ == "__main__":
    weibo_new_era_list()

