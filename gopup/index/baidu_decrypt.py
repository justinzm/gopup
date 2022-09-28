#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/9/28 11:10
# @Author : justin.郑 3907721@qq.com
# @File : baidu_decrypt.py
# @desc : 百度解密

from typing import List, Dict, Tuple
from urllib.parse import urlencode, quote
from gopup.index.errors import ErrorCode, GopupError
from Crypto.Cipher import AES
from base64 import b64encode
import datetime
import requests
import json


headers = {
    'Host': 'index.baidu.com',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
}

ALL_KIND = ['all', 'pc', 'wise']


def decrypt_func(key: str, data: str) -> List[str]:
    """
        数据解密方法
    """
    a = key
    i = data
    n = {}
    s = []
    for o in range(len(a)//2):
        n[a[o]] = a[len(a)//2 + o]
    for r in range(len(data)):
        s.append(n[i[r]])
    return ''.join(s).split(',')


def http_get(url: str, cookies: str, cipher_text: str = "") -> str:
    """
        发送get请求, 程序中所有的get都是调这个方法
        如果想使用多cookies抓取, 和请求重试功能
        在这自己添加
    """
    _headers = headers.copy()
    _headers['Cookie'] = cookies
    if cipher_text:
        _headers["Cipher-Text"] = cipher_text
    try:
        response = requests.get(url, headers=_headers, timeout=30)
    except requests.Timeout:
        raise GopupError(ErrorCode.NETWORK_ERROR)
    if response.status_code != 200:
        raise GopupError(ErrorCode.NETWORK_ERROR)
    return response.text


def get_cipher_text(keyword: str) -> str:
    byte_list = [
        b"\x00", b"\x01", b"\x02", b"\x03", b"\x04", b"\x05", b"\x06", b"\x07",
        b"\x08", b"\x09", b"\x0a", b"\x0b", b"\x0c", b"\x0d", b"\x0e", b"\x0f",
        b"\x10"
    ]
    # 这个数是从acs-2057.js里写死的，但这个脚本请求时代时间戳，不确定是不是一个动态变化的脚本
    start_time = 1652338834776
    end_time = int(datetime.datetime.now().timestamp()*1000)

    wait_encrypted_data = {
        "ua": headers["User-Agent"],
        "url": quote(f"https://index.baidu.com/v2/main/index.html#/trend/{keyword}?words={keyword}"),
        "platform": "MacIntel",
        "clientTs": end_time,
        "version": "2.1.0"
    }
    password = b"yyqmyasygcwaiyaa"
    iv = b"1234567887654321"
    aes = AES.new(password, AES.MODE_CBC, iv)
    wait_encrypted_str = json.dumps(wait_encrypted_data).encode()
    filled_count = 16 - len(wait_encrypted_str) % 16
    wait_encrypted_str += byte_list[filled_count] * filled_count
    encrypted_str = aes.encrypt(wait_encrypted_str)
    cipher_text = f"{start_time}_{end_time}_{b64encode(encrypted_str).decode()}"
    return cipher_text


def get_encrypt_json(
    *,
    start_date: str,
    end_date: str,
    keywords: List[List[str]],
    type: str,
    area: int,
    cookies: str
) -> Dict:
    pre_url_map = {
        'search': 'http://index.baidu.com/api/SearchApi/index?',
        'live': 'http://index.baidu.com/api/LiveApi/getLive?',
        'news': 'http://index.baidu.com/api/NewsApi/getNewsIndex?',
        'feed': 'http://index.baidu.com/api/FeedSearchApi/getFeedIndex?'
    }

    pre_url = pre_url_map[type]
    word_list = [
        [{'name': keyword, 'wordType': 1} for keyword in keyword_list]
        for keyword_list in keywords
    ]
    if type == 'live':
        request_args = {
            'word': json.dumps(word_list),
            'region': area
        }
    else:
        request_args = {
            'word': json.dumps(word_list),
            'startDate': start_date,
            'endDate': end_date,
            'area': area
        }
    url = pre_url + urlencode(request_args)
    cipher_text = get_cipher_text(keywords[0][0])
    html = http_get(url, cookies, cipher_text=cipher_text)
    datas = json.loads(html)
    if datas['status'] == 10000:
        raise GopupError(ErrorCode.NO_LOGIN)
    if datas["status"] == 10001:
        raise GopupError(ErrorCode.REQUEST_LIMITED)
    if datas['status'] != 0:
        raise GopupError(ErrorCode.UNKNOWN, str(datas))
    return datas


def get_key(uniqid: str, cookies: str) -> str:
    url = 'http://index.baidu.com/Interface/api/ptbk?uniqid=%s' % uniqid
    html = http_get(url, cookies)
    datas = json.loads(html)
    key = datas['data']
    return key


def format_data(data: Dict, kind: str):
    """
        格式化堆在一起的数据
    """
    keyword = str(data['word'])
    start_date = datetime.datetime.strptime(data['all']['startDate'], '%Y-%m-%d')
    end_date = datetime.datetime.strptime(data['all']['endDate'], '%Y-%m-%d')
    date_list = []
    while start_date <= end_date:
        date_list.append(start_date)
        start_date += datetime.timedelta(days=1)

    # for kind in ALL_KIND:
    index_datas = data[kind]['data']
    for i, cur_date in enumerate(date_list):
        try:
            index_data = index_datas[i]
        except IndexError:
            index_data = ''
        formated_data = {
            'keyword': [keyword_info['name'] for keyword_info in json.loads(keyword.replace('\'', '"'))][0],
            'type': kind,
            'date': cur_date.strftime('%Y-%m-%d'),
            'index': index_data if index_data else '0'
        }
        yield formated_data


def format_data_feed(data: Dict):
    keyword = str(data['key'])
    start_date = datetime.datetime.strptime(data['startDate'], '%Y-%m-%d')
    end_date = datetime.datetime.strptime(data['endDate'], '%Y-%m-%d')
    date_list = []
    while start_date <= end_date:
        date_list.append(start_date)
        start_date += datetime.timedelta(days=1)

    index_datas = data['data']
    for i, cur_date in enumerate(date_list):
        try:
            index_data = index_datas[i]
        except IndexError:
            index_data = ''
        formated_data = {
            'keyword': [keyword_info['name'] for keyword_info in json.loads(keyword.replace('\'', '"'))][0],
            'date': cur_date.strftime('%Y-%m-%d'),
            'index': index_data if index_data else '0'
        }
        yield formated_data


def format_data_new(data: Dict):
    keyword = str(data['key'])
    start_date = datetime.datetime.strptime(data['startDate'], '%Y-%m-%d')
    end_date = datetime.datetime.strptime(data['endDate'], '%Y-%m-%d')
    date_list = []
    while start_date <= end_date:
        date_list.append(start_date)
        start_date += datetime.timedelta(days=1)

    index_datas = data['data']
    for i, cur_date in enumerate(date_list):
        try:
            index_data = index_datas[i]
        except IndexError:
            index_data = ''
        formated_data = {
            'keyword': [keyword_info['name'] for keyword_info in json.loads(keyword.replace('\'', '"'))][0],
            'date': cur_date.strftime('%Y-%m-%d'),
            'index': index_data if index_data else '0'
        }
        yield formated_data

