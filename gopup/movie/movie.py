#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/15 0015
# @Author  : justin.郑 3907721@qq.com
# @File    : movie.py
# @Desc    : 影视数据
# EBOT艺恩票房智库 https://www.endata.com.cn

import json
import os

import pandas as pd
import requests
import execjs
from gopup.movie.cons import headers
from gopup.utils.date_utils import today, day_last_date


def realtime_boxoffice():
    """
    获取实时电影票房数据
    数据来源：EBOT艺恩票房智库 https://www.endata.com.cn/BoxOffice
    :return:
        DataFrame
              BoxOffice     实时票房（万）
              Irank         排名
              MovieName     影片名
              boxPer        票房占比 （%）
              movieDay      上映天数
              sumBoxOffice  累计票房（万）
              default_url   影片海报
    """
    try:
        url = "https://www.endata.com.cn/API/GetData.ashx"
        data = {
            "tdate": today(),
            "MethodName": "BoxOffice_GetHourBoxOffice"
        }
        r = requests.post(url=url, data=data, headers=headers)
        js = get_js('webDES.js')

        docjs = execjs.compile(js)
        res = docjs.call("webInstace.shell", r.text)
        res_dict = json.loads(res)

        if res_dict['Status'] == 1:
            tmp = res_dict['Data']['Table1']
            res_pd = pd.DataFrame(tmp)
            res_pd = res_pd.drop(columns=['moblie_url', 'larger_url', 'mId', 'MovieImg'])
        return res_pd
    except Exception as e:
        return str(e)


def day_boxoffice(date=None):
    """
    获取单日电影票房数据
    数据来源：EBOT艺恩票房智库 https://www.endata.com.cn/BoxOffice
    :param date: 日期
    :return:
        DataFrame
              Irank         排名
              MovieName     影片名
              BoxOffice     单日票房(万)
              BoxOffice_Up  环比变化
              SumBoxOffice  累计票房（万）
              default_url   影片海报
              AvgPrice      平均票价
              AvpPeoPle     场均人次
              RapIndex      口碑指数
              MovieDay      上映天数

    """
    try:
        if date == None:
            edate = today()
        else:
            edate = date
        sdate = day_last_date(edate, days=1)
        url = "https://www.endata.com.cn/API/GetData.ashx"
        data = {
            "sdate": sdate,
            "edate": edate,
            "MethodName": "BoxOffice_GetDayBoxOffice"
        }
        r = requests.post(url=url, data=data, headers=headers)
        js = get_js('webDES.js')

        docjs = execjs.compile(js)
        res = docjs.call("webInstace.shell", r.text)
        res_dict = json.loads(res)

        if res_dict['Status'] == 1:
            tmp = res_dict['Data']['Table']
            res_pd = pd.DataFrame(tmp)
            res_pd = res_pd.drop(columns=['MovieImg', 'moblie_url', 'larger_url', 'MovieID', 'Director', 'BoxOffice1', 'IRank_pro', 'RapIndex'])
        return res_pd
    except Exception as e:
        return str(e)


def day_cinema(date=None):
    """
    获取单日影院票房
    :param date:
    :return:
        DataFrame
              RowNum         排名
              CinemaName     影院名称
              TodayBox       单日票房(元)
              TodayShowCount 单日场次
              AvgPeople      场均人次
              price          场均票价(元)
              Attendance     上座率
    """
    try:
        url = "https://www.endata.com.cn/API/GetData.ashx"
        data = {
            "date": date,
            "rowNum1": 1,
            "rowNum2": 100,
            "MethodName": "BoxOffice_GetCinemaDayBoxOffice"
        }
        r = requests.post(url=url, data=data, headers=headers)
        js = get_js('webDES.js')

        docjs = execjs.compile(js)
        res = docjs.call("webInstace.shell", r.text)
        res_dict = json.loads(res)

        if res_dict['Status'] == 1:
            tmp = res_dict['Data']['Table']
            res_pd = pd.DataFrame(tmp)
            res_pd = res_pd.drop(
                columns=['CinemaID', 'TodayAudienceCount', 'TodayOfferSeat'])
        return res_pd
    except Exception as e:
        return str(e)


def realtime_tv():
    """
    获取实时电视剧播映指数
    数据来源：EBOT艺恩票房智库 https://www.endata.com.cn/BoxOffice/Video/index.html
    :return:
        DataFrame
              TvName        名称
              Irank         排名
              Genres        类型
              PlayIndex     播映指数
              MediaHot      媒体热度
              UserHot       用户热度
              AnswerHot     好评度
              PlayHot       观看度
              date          日期
    """
    try:
        url = "https://www.endata.com.cn/API/GetData.ashx"
        data = {
            "tvType": 2,
            "MethodName": "BoxOffice_GetTvData_PlayIndexRank"
        }
        r = requests.post(url=url, data=data, headers=headers)
        js = get_js('webDES.js')

        docjs = execjs.compile(js)
        res = docjs.call("webInstace.shell", r.text)
        res_dict = json.loads(res)

        if res_dict['Status'] == 1:
            tmp = res_dict['Data']['Table']
            res_pd = pd.DataFrame(tmp)
            res_pd['date'] = res_dict['Data']['Table1'][0]['MaxDate']
        return res_pd
    except Exception as e:
        return str(e)


def realtime_show():
    """
    获取实时综艺播映指数
    数据来源：EBOT艺恩票房智库 https://www.endata.com.cn/BoxOffice/Video/index.html
    :return:
        DataFrame
              TvName        名称
              Irank         排名
              Genres        类型
              PlayIndex     播映指数
              MediaHot      媒体热度
              UserHot       用户热度
              AnswerHot     好评度
              PlayHot       观看度
              date          日期
    """
    try:
        url = "https://www.endata.com.cn/API/GetData.ashx"
        data = {
            "tvType": 8,
            "MethodName": "BoxOffice_GetTvData_PlayIndexRank"
        }
        r = requests.post(url=url, data=data, headers=headers)
        js = get_js('webDES.js')

        docjs = execjs.compile(js)
        res = docjs.call("webInstace.shell", r.text)
        res_dict = json.loads(res)

        if res_dict['Status'] == 1:
            tmp = res_dict['Data']['Table']
            res_pd = pd.DataFrame(tmp)
            res_pd['date'] = res_dict['Data']['Table1'][0]['MaxDate']
        return res_pd
    except Exception as e:
        return str(e)


def realtime_artist():
    """
    获取艺人商业价值
    数据来源：EBOT艺恩票房智库 https://www.endata.com.cn/BoxOffice/Marketing/Artist/business.html
    :return:
        DataFrame
              StarBaseName  艺人
              Irank         排名
              BusinessValueIndex_L1  商业价值
              MajorHotIndex_L2       专业热度
              FocusHotIndex_L2       关注热度
              PredictHotIndex_L2     预测热度
              ReputationIndex_L3     美誉度
    """
    try:
        url = "https://www.endata.com.cn/API/GetData.ashx"
        data = {
            "Order": "BusinessValueIndex_L1",
            "OrderType": "DESC",
            "PageIndex": 1,
            "PageSize": 100,
            "MethodName": "Data_GetList_Star"
        }
        r = requests.post(url=url, data=data, headers=headers)
        js = get_js('webDES.js')

        docjs = execjs.compile(js)
        res = docjs.call("webInstace.shell", r.text)
        res_dict = json.loads(res)

        if res_dict['Status'] == 1:
            tmp = res_dict['Data']['Table']
            res_pd = pd.DataFrame(tmp)
            res_pd = res_pd.drop(
                columns=['StarBaseID'])
        return res_pd
    except Exception as e:
        return str(e)


def realtime_artist_flow():
    """
    获取艺人流量价值
    数据来源：EBOT艺恩票房智库 https://www.endata.com.cn/BoxOffice/Marketing/Artist/business.html
    :return:
        DataFrame
              StarBaseName  艺人
              Irank         排名
              FlowValueIndex_L1      流量价值
              MajorHotIndex_L2       专业热度
              FocusHotIndex_L2       关注热度
              PredictHotIndex_L2     预测热度
              TakeGoodsIndex_L2      带货力
    """
    try:
        url = "https://www.endata.com.cn/API/GetData.ashx"
        data = {
            "Order": "FlowValueIndex_L1",
            "OrderType": "DESC",
            "PageIndex": 1,
            "PageSize": 100,
            "MethodName": "Data_GetList_Star"
        }
        r = requests.post(url=url, data=data, headers=headers)
        js = get_js('webDES.js')

        docjs = execjs.compile(js)
        res = docjs.call("webInstace.shell", r.text)
        res_dict = json.loads(res)

        if res_dict['Status'] == 1:
            tmp = res_dict['Data']['Table']
            res_pd = pd.DataFrame(tmp)
            res_pd = res_pd.drop(
                columns=['StarBaseID', 'ReputationIndex_L3', 'BusinessValueIndex_L1'])
        return res_pd
    except Exception as e:
        return str(e)


def get_js(js_url):
    js_url = _get_js_path(js_url, __file__)
    f = open(js_url, 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


def _get_js_path(name, module_file):
    """
    获取 JS 文件的路径(从模块所在目录查找)
    :param name: 文件名
    :param module_file: filename
    :return: str json_file_path
    """
    module_folder = os.path.abspath(os.path.dirname(os.path.dirname(module_file)))
    module_json_path = os.path.join(module_folder, "movie", name)
    return module_json_path


if __name__ == "__main__":
    # "Python运行execjs中出现编码问题: https://www.jianshu.com/p/df0000013254"
    tmp = realtime_boxoffice()
    print(tmp)

