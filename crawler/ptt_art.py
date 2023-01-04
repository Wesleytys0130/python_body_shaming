#coding=utf-8
from ptt_functions import geturl, comments, article
import bs4, re, json, time
import urllib.request as req
import pandas as pd

alllist = []
board = "MuscleBeach"
for i in range(1,2):
    pageurl = "https://www.ptt.cc/bbs/"+board+"/index"+str(i)+".html"
    for arturl in geturl(pageurl):
        try:
            alllist.append(article(arturl))
            print(time.ctime(),arturl+" is done")
        except:
            with open("/ptt_/kuan/art_error/art_error.txt", "a") as f:
                f.write(arturl+'\n')
            print("Stop at "+arturl)
    print(time.ctime(),"\n",pageurl+" is done")
with open("/Users/guanlizhe/Desktop/code/python/web_crawer/ptt_data/MuscleBeach/MB_art.json", "a") as f:
    json.dump(alllist, f, ensure_ascii=False,indent=2)