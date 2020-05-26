#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 16:30
# @Author  : justin.郑 3907721@qq.com
# @File    : rest_agent.py
# @Desc    :

import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np


class RestAgent():
    def __init__(self):
        # request header
        self.user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) " \
                     "AppleWebKit/537.36 (KHTML, like Gecko) " \
                     "Chrome/57.0.2987.133 Safari/537.36 "

        # simulate http request
        self.session = requests.Session()
        self.session.headers['User-Agent'] = self.user_agent
        self.session.headers['X-Forwarded-For'] = ':'.join('{0:x}'.format(np.random.randint(0, 2**16 - 1)) for i in range(4)) + ':1'
        self.proxies = None

    def add_headers(self, dict):
        self.session.headers.update(dict)

    def get_cookies(self):
        return self.session.cookies

    def set_proxies(self, proxies):
        self.proxies = proxies

    def do_request(self, url, param = None, method="GET", type="text", encoding = None, json = None, **kwargs):
        if self.proxies is None:
            if method == "GET":
                res = self.session.get(url, params=param, **kwargs)
            else:
                if json is not None:
                    res = self.session.post(url, json=json, **kwargs)
                else:
                    res = self.session.post(url, data=param, **kwargs)
        else:
            if method == "GET":
                res = self.session.get(url, params=param, proxies=self.proxies, **kwargs)
            else:
                if json is not None:
                    res = self.session.post(url, json=json, proxies=self.proxies, **kwargs)
                else:
                    res = self.session.post(url, data=param, proxies=self.proxies, **kwargs)

        if res.status_code != 200:
            return None
        else:

            if encoding is not None:
                res.encoding = encoding

            if type == 'text':
                return res.text
            else:
                return res.content

    def get_aspx_param(self, url):
        html = self.do_request(url)
        bsObj = BeautifulSoup(html, 'html5lib')
        __VIEWSTATE          = bsObj.find('input', {'id': '__VIEWSTATE'}).attrs['value']
        __EVENTVALIDATION    = bsObj.find('input', {'id': '__EVENTVALIDATION'}).attrs['value']
        __VIEWSTATEGENERATOR = bsObj.find('input', {'id' : '__VIEWSTATEGENERATOR'}).attrs['value']

        data = {
            "__VIEWSTATE"            : __VIEWSTATE,
            "__EVENTVALIDATION"     : __EVENTVALIDATION,
            "__VIEWSTATEGENERATOR"  : __VIEWSTATEGENERATOR,
        }
        return data

    def get_proxy_list(self):
        url = "http://www.mimiip.com/gngao/"
        pageno = 0

        proxy_list = []
        while pageno < 10:
            pageno = pageno + 1
            rsp = self.do_request(url + str(pageno), None, None)

            if rsp is None:
                return None

            soup = BeautifulSoup(rsp)
            tables = soup.find_all('table')

            data = []
            for table in tables:
                if table.has_key('class') and "list" in table['class']:
                    rows = table.findAll('tr')
                    for row in rows:
                        cols = row.findAll('td')
                        if (len(cols) > 5) :
                            ip   = cols[0].text
                            port = cols[1].text
                            type = cols[4].text
                            data.append((ip, port, type))

            if len(data) == 0:
                break
            else:
                proxy_list.extend(data)

        df = pd.DataFrame(proxy_list)
        df.columns = ['IP', 'Port', 'Type']

        return df


if __name__ == '__main__':
    aqi = RestAgent()
    result = aqi.get_proxy_list()
    print(result)