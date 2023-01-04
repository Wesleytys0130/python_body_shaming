#coding=utf-8
from ptt_functions import geturl, comments, article
import bs4, re, json, time
import urllib.request as req
import pandas as pd


error_url = []
with open("/Users/guanlizhe/Desktop/code/python/web_crawer/ptt_/kuan/art_error/MBart_error.txt") as f:
    url = f.read()
    urllist = url.split("\n")
urllist = [i for i in urllist if i != '']


for arturl in urllist:
        error_url.append(article(arturl))
        print(time.ctime(),arturl+" is done")
with open("/Users/guanlizhe/Desktop/code/python/web_crawer/ptt_data/MuscleBeach/MB_art.json", "a") as f:
    json.dump(error_url, f, ensure_ascii=False,indent=2)