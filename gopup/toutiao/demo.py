# -*- coding: utf-8 -*-

import json
import requests


class Toutiao(object):

    def __init__(self):
        self.url = 'https://www.toutiao.com/api/pc/feed/'
        self.jm_js = "http://www.gopup.cn/static/lib/jm.js"
        self.session = requests.session()

    def get_params(self):
        """获取加密参数"""
        params = requests.get(url=self.jm_js).text
        return json.loads(params)

    def run_spider(self):
        params = self.get_params()
        print(params)

        params = {
            'category': 'news_hot',
            'utm_source': 'toutiao',
            'widen': 1,
            "max_behot_time": 0,
            "max_behot_time_tmp": 0,
            'tadrequire': 'true',
            'as': params['as'],
            'cp': params['cp'],
            '_signature': params['sign'],
        }
        # cookie未解决
        headers = {
            'cookie': "csrftoken=93caf9dae34d5289b9fc8652229882f7; s_v_web_id=verify_kblwbxnd_wgxnwO98_VxW3_4VMg_BxCp_tmiQsacXIER3; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=ztoein1fd1592551983501; SLARDAR_WEB_ID=004b127d-9078-498c-bbb8-b9ced3f8bd2d; tt_webid=6839963699140675080; tt_webid=6839963699140675080; tt_scid=eglD-q.pkX3MQ8Zn-vrnORGa6hxB0TQO-bshWs7v0RE6sbGCPfU5njBU-Si-FJUt88d7",
            'referer': 'https://www.toutiao.com/ch/news_hot/',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.3',
            'x-requested-with': 'XMLHttpRequest',
        }
        resp = self.session.get(self.url, params=params, headers=headers)

        print(resp.status_code)
        # print(resp.text)
        print(resp.json())


if __name__ == '__main__':
    test = Toutiao()
    test.run_spider()
