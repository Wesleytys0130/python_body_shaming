#coding=utf-8
from ptt_functions import geturl, comments, article
import bs4, re, json, time
import urllib.request as req
import pandas as pd



with open("/Users/guanlizhe/Desktop/code/python/web_crawer/ptt_/kuan/com_error/MBcom_error.txt") as f:
    url = f.read()
    urllist = url.split("\n")
urllist = [i for i in urllist if i != '']

for url in urllist:
    (pd.DataFrame.from_dict(data=comments(url))
        .to_csv('/Users/guanlizhe/Desktop/code/python/web_crawer/ptt_data/MuscleBeach/MB_com.csv', mode='a'))
    print(time.ctime(),url+" is done")