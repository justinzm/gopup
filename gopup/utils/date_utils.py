#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : date_utils.py
# @Desc    : 日期管理工具

import datetime
import time
import pandas as pd


def year_qua(date):
    mon = date[5:7]
    mon = int(mon)
    return [date[0:4], _quar(mon)]


def _quar(mon):
    if mon in [1, 2, 3]:
        return '1'
    elif mon in [4, 5, 6]:
        return '2'
    elif mon in [7, 8, 9]:
        return '3'
    elif mon in [10, 11, 12]:
        return '4'
    else:
        return None


def today():
    """
    获取当天日期 年-月-日
    """
    day = datetime.datetime.today().date()
    return str(day)


def get_year():
    """
    获取当年
    """
    year = datetime.datetime.today().year
    return year


def get_month():
    """
    获取当月
    """
    month = datetime.datetime.today().month
    return month


def get_hour():
    """
    获取当前小时
    """
    return datetime.datetime.today().hour


def today_last_year():
    """
    获取去年的今天日期
    """
    lasty = datetime.datetime.today().date() + datetime.timedelta(-365)
    return str(lasty)


def day_last_week(days=-7):
    """
    获得前几天的日期
    :param days: 前几天
    """
    lasty = datetime.datetime.today().date() + datetime.timedelta(days)
    return str(lasty)


def day_last_date(date, days=-1):
    """
    获得某天的之前一天日期
    :param date: 日期
    """
    dd = datetime.datetime.strptime(date, "%Y-%m-%d")
    lasty = dd + datetime.timedelta(days)
    return str(lasty)[0:10]


def get_now():
    """
    获得当前时间
    """
    return time.strftime('%Y-%m-%d %H:%M:%S')


def int2time(timestamp):
    datearr = datetime.datetime.utcfromtimestamp(timestamp)
    timestr = datearr.strftime("%Y-%m-%d %H:%M:%S")
    return timestr


def diff_day(start=None, end=None):
    """
    两个日期间 相差天数
    :param start: 开始日期
    :param end:   截止日期
    :return: 相差天数
    """
    d1 = datetime.datetime.strptime(end, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(start, '%Y-%m-%d')
    delta = d1 - d2
    return delta.days


def get_quarts(start, end):
    idx = pd.period_range('Q'.join(year_qua(start)), 'Q'.join(year_qua(end)),
                          freq='Q-JAN')
    return [str(d).split('Q') for d in idx][::-1]


def trade_cal():
    '''
    交易日历
    isOpen=1是交易日，isOpen=0为休市
    '''
    ALL_CAL_FILE = 'http://file.tushare.org/tsdata/calAll.csv'
    df = pd.read_csv(ALL_CAL_FILE)
    return df


def is_holiday(date):
    '''
    判断是否为交易日，返回True or False
    '''
    df = trade_cal()
    holiday = df[df.isOpen == 0]['calendarDate'].values
    if isinstance(date, str):
        today = datetime.datetime.strptime(date, '%Y-%m-%d')

    if today.isoweekday() in [6, 7] or str(date) in holiday:
        return True
    else:
        return False


def last_tddate():
    today = datetime.datetime.today().date()
    today = int(today.strftime("%w"))
    if today == 0:
        return day_last_week(-2)
    else:
        return day_last_week(-1)


def tt_dates(start='', end=''):
    startyear = int(start[0:4])
    endyear = int(end[0:4])
    dates = [d for d in range(startyear, endyear + 1, 2)]
    return dates


def _random(n=13):
    from random import randint
    start = 10 ** (n - 1)
    end = (10 ** n) - 1
    return str(randint(start, end))


def get_q_date(year=None, quarter=None):
    dt = {'1': '-03-31', '2': '-06-30', '3': '-09-30', '4': '-12-31'}
    return '%s%s' % (str(year), dt[str(quarter)])
 

if __name__ == "__main__":
    tmp = day_last_date('2017-03-27')
    # tmp = tt_dates('2017-03-27', '2021-03-30')
    print(tmp)

