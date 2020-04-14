#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 12:59
# @Author  : justin.郑 3907721@qq.com
# @File    : star.py
# @Desc    : 星图
# https://star.toutiao.com/

import requests
import urllib
from gopup.mcn import cons

def star_hot_list(cookie=None):
    cookie = cons.STAR_COOKIE
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "referer": "https://star.toutiao.com/ad",
        "cookie": cookie
    }
    tag = urllib.parse.quote_plus('颜值达人')
    url = "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6720184315054915588&tag=%s&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=1a839930d2dc2aa1f7f6faf703a63bf1" % tag
    r = requests.get(url, headers=headers)
    data_json = r.json()
    pass


if __name__ == "__main__":
    star_hot_list()