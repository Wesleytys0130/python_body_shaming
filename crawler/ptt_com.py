#coding=utf-8
from ptt_functions import geturl, comments, article
import bs4, re, json, time
import urllib.request as req
import pandas as pd



for i in range(9,11):
    pageurl = "https://www.ptt.cc/bbs/FITNESS/index"+str(i)+".html"
    for arturl in geturl(pageurl):
        try:
            (pd.DataFrame.from_dict(data=comments(arturl))
                .to_csv('/Users/guanlizhe/Desktop/code/python/web_crawer/ptt_/kuan/com_index.csv', mode='a'))
            print(time.ctime(),arturl+" is done")
        except:
            with open("/Users/guanlizhe/Desktop/code/python/web_crawer/ptt_/kuan/com_error.txt", "a") as f:
                f.write(arturl+'\n')
            print("Stop at "+arturl)
    print(time.ctime(),"\n",pageurl+" is done")