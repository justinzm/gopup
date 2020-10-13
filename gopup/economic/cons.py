#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : cons.py
# @Desc    : 配置文件

P_TYPE = {'http': 'http://', 'ftp': 'ftp://'}

MACRO_TYPE = ['nation','price','fininfo']

MACRO_URL = '%smoney.finance.%s/mac/api/jsonp.php/SINAREMOTECALLCALLBACK%s/MacPage_Service.get_pagedata?cate=%s&event=%s&from=0&num=%s&condition=&_=%s'

DOMAINS = {'sina': 'sina.com.cn', 'sinahq': 'sinajs.cn',
           'ifeng': 'ifeng.com', 'sf': 'finance.sina.com.cn',
           'vsf': 'vip.stock.finance.sina.com.cn',
           'idx': 'www.csindex.com.cn', '163': 'money.163.com',
           'em': 'eastmoney.com', 'sseq': 'query.sse.com.cn',
           'sse': 'www.sse.com.cn', 'szse': 'www.szse.cn',
           'oss': 'file.tushare.org', 'idxip':'115.29.204.48',
           'shibor': 'www.shibor.org', 'mbox':'www.cbooo.cn',
           'tt': 'gtimg.cn', 'gw': 'gw.com.cn',
           'v500': 'value500.com', 'sstar': 'stock.stockstar.com',
           'dfcf': 'nufm.dfcfw.com'}

PAGES = {'fd': 'index.phtml', 'dl': 'downxls.php', 'jv': 'json_v2.php',
         'cpt': 'newFLJK.php', 'ids': 'newSinaHy.php', 'lnews': 'rollnews_ch_out_interface.php',
         'ntinfo': 'vCB_BulletinGather.php', 'hs300b': '000300cons.xls',
         'hs300w': '000300closeweight.xls','sz50b': '000016cons.xls',
         'dp': 'all_fpya.php', '163dp':'fpyg.html',
         'emxsg': 'JS.aspx', '163fh':'jjcgph.php',
         'newstock': 'vRPD_NewStockIssue.php', 'zz500b': '000905cons.xls',
         'zz500wt': '000905closeweight.xls',
         't_ticks': 'vMS_tradedetail.php', 'dw': 'downLoad.html',
         'qmd': 'queryMargin.do', 'szsefc': 'ShowReport.szse',
         'ssecq': 'commonQuery.do', 'sinadd': 'cn_bill_download.php', 'ids_sw':'SwHy.php',
         'idx': 'index.php', 'index': 'index.html'}

SHIBOR_TYPE ={'Shibor': 'Shibor数据', 'Quote': '报价数据', 'Tendency': 'Shibor均值数据',
              'LPR': 'LPR数据', 'LPR_Tendency': 'LPR均值数据'}

GDP_YEAR_COLS = ['year','gdp','pc_gdp','gnp','pi','si','industry','cons_industry','ti','trans_industry','lbdy']
GDP_QUARTER_COLS = ['quarter','gdp','gdp_yoy','pi','pi_yoy','si','si_yoy','ti','ti_yoy']
GDP_FOR_COLS = ['year','end_for','for_rate','asset_for','asset_rate','goods_for','goods_rate']
GDP_PULL_COLS = ['year','gdp_yoy','pi','si','industry','ti']
GDP_CONTRIB_COLS = ['year','gdp_yoy','pi','si','industry','ti']
CPI_COLS = ['month','cpi']
PPI_COLS = ['month','ppiip','ppi','qm','rmi','pi','cg','food','clothing','roeu','dcg']
DEPOSIT_COLS = ['date','deposit_type','rate']
LOAN_COLS = ['date','loan_type','rate']
RRR_COLS = ['date','before','now','changed']
MONEY_SUPPLY_COLS = ['month','m2','m2_yoy','m1','m1_yoy','m0','m0_yoy','cd','cd_yoy','qm','qm_yoy','ftd','ftd_yoy','sd','sd_yoy','rests','rests_yoy']
MONEY_SUPPLY_BLA_COLS = ['year','m2','m1','m0','cd','qm','ftd','sd','rests']
GOLD_AND_FOREIGN_CURRENCY_RESERVES = ['month','gold','foreign_reserves']

SHIBOR_DATA_URL = '%s%s/shibor/web/html/%s?nameNew=Historical_%s_Data_%s.xls&downLoadPath=data&nameOld=%s%s.xls&shiborSrc=http://www.shibor.org/shibor/'

LPR_DATA_URL = 'http://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/LprHis'

SHIBOR_COLS = ['date', 'ON', '1W', '2W', '1M', '3M', '6M', '9M', '1Y']
SHIBOR_Q_COLS = ['date', 'bank', 'ON', '1W', '2W', '1M', '3M', '6M', '9M', '1Y']
SHIBOR_MA_COLS = ['date', 'ON_5', 'ON_10', 'ON_20', '1W_5', '1W_10', '1W_20','2W_5', '2W_10', '2W_20',
                  '1M_5', '1M_10', '1M_20', '3M_5', '3M_10', '3M_20', '6M_5', '6M_10', '6M_20',
                  '9M_5', '9M_10', '9M_20','1Y_5', '1Y_10', '1Y_20']


def random(n=13):
    from random import randint
    start = 10**(n-1)
    end = (10**n)-1
    return str(randint(start, end))

