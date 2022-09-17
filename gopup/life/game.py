#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/15 17:26
# @Author  : justin.郑 3907721@qq.com
# @File    : game.py
# @Desc    : 游戏排行榜

import requests
import time
import pandas as pd
from pyquery import PyQuery as pq


def club_rank(type):
    """
    中国电竞价值排行榜 俱乐部排行榜
    Parameters
    ------
      type: 类型    gameid
            英雄联盟 2
            绝地求生 3
            王者荣耀 4
            DOTA2  1
            穿越火线 5
            和平精英 6
    Return
    ------
    日期、类型、排名、俱乐部logo、俱乐部名称、人气指数、舆论指数、综合指数、排名变动

    http://rank.uuu9.com/club/ranking?gameId=6&type=0
    """
    if type == "DOTA2":
        gameid = 1
    elif type == "英雄联盟":
        gameid = 2
    elif type == "绝地求生":
        gameid = 3
    elif type == "王者荣耀":
        gameid = 4
    elif type == "穿越火线":
        gameid = 5
    elif type == "和平精英":
        gameid = 6
    else:
        return "游戏名称输入错误"
    try:
        url = "http://rank.uuu9.com/club/ranking?gameId=%s&type=0" % gameid
        herder = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive"
        }
        r = requests.get(url=url, headers=herder)
        doc = pq(r.text)
        trs = doc(".ec_table table tbody tr")
        res_list= []
        for tr in trs.items():
            bd_res = tr(".ec_change i").attr("class")
            bd_val = tr(".ec_change").text()
            if bd_res == "rise":
                bd = "上升 %s位" % bd_val
            elif bd_res == "decline":
                bd = "下降 %s位" % bd_val
            else:
                bd = "-"
            res_dict = {
                "日期": time.strftime("%Y-%m-%d"),
                "类型": type,
                "排名": tr.find(".ec_num").text(),
                "俱乐部logo": "http://rank.uuu9.com/%s" % tr("img").attr("src"),
                "俱乐部名称": tr("dd").text(),
                "人气指数": tr("td:nth-child(3)").text(),
                "舆论指数": tr("td:nth-child(4)").text(),
                "综合指数": tr("td:nth-child(5)").text(),
                "排名变动": bd
            }
            res_list.append(res_dict)
        res_pd = pd.DataFrame(res_list)
        return res_pd
    except:
        return None


def player_rank(type):
    """
    中国电竞价值排行榜 选手排行榜
    Parameters
    ------
      type: 类型    gameid
            英雄联盟 2
            绝地求生 3
            王者荣耀 4
            DOTA2  1
            穿越火线 5
            和平精英 6
    Return
    ------
    日期、类型、排名、选手头像、选手名、所属战队、人气指数、舆论指数、战绩指数、综合指数、身价、排名变动

    http://rank.uuu9.com/player/ranking?gameId=6&type=0
    """
    if type == "DOTA2":
        gameid = 1
    elif type == "英雄联盟":
        gameid = 2
    elif type == "绝地求生":
        gameid = 3
    elif type == "王者荣耀":
        gameid = 4
    elif type == "穿越火线":
        gameid = 5
    elif type == "和平精英":
        gameid = 6
    else:
        return "游戏名称输入错误"
    try:
        url = "http://rank.uuu9.com/player/ranking?gameId=%s&type=0" % gameid
        herder = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive"
        }
        r = requests.get(url=url, headers=herder)
        doc = pq(r.text)
        trs = doc(".ec_table table tbody tr")
        res_list= []
        for tr in trs.items():
            bd_res = tr(".ec_change i").attr("class")
            bd_val = tr(".ec_change").text()
            if bd_res == "rise":
                bd = "上升 %s位" % bd_val
            elif bd_res == "decline":
                bd = "下降 %s位" % bd_val
            else:
                bd = "-"
            if type == "英雄联盟":
                res_dict = {
                    "日期": time.strftime("%Y-%m-%d"),
                    "类型": type,
                    "排名": tr.find(".ec_num").text(),
                    "选手头像": "http://rank.uuu9.com/%s" % tr("img").attr("src"),
                    "选手名": tr("dd").text(),
                    "所属战队": tr("td:nth-child(3)").text(),
                    "人气指数": tr("td:nth-child(4)").text(),
                    "舆论指数": tr("td:nth-child(5)").text(),
                    "战绩指数": tr("td:nth-child(6)").text(),
                    "综合指数": tr("td:nth-child(7)").text(),
                    "身价": tr("td:nth-child(8)").text(),
                    "排名变动": bd
                }
            else:
                res_dict = {
                    "日期": time.strftime("%Y-%m-%d"),
                    "类型": type,
                    "排名": tr.find(".ec_num").text(),
                    "选手头像": "http://rank.uuu9.com/%s" % tr("img").attr("src"),
                    "选手名": tr("dd").text(),
                    "所属战队": tr("td:nth-child(3)").text(),
                    "人气指数": tr("td:nth-child(4)").text(),
                    "舆论指数": tr("td:nth-child(5)").text(),
                    "综合指数": tr("td:nth-child(6)").text(),
                    "身价": tr("td:nth-child(7)").text(),
                    "排名变动": bd
                }

            res_list.append(res_dict)
        res_pd = pd.DataFrame(res_list)
        return res_pd
    except:
        return None


if __name__ == "__main__":
    tmp = player_rank(type="英雄联盟")
    print(tmp)
