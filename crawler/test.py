from ptt_functions import geturl, comments
import bs4, re, json
import urllib.request as req
import pandas as pd



# with open("/Users/guanlizhe/Desktop/code/python/web_crawer/ptt_/kuan/art_index.json", "r") as password_file:
#     dic = json.load(password_file)
# df = pd.DataFrame.from_dict(dic)
# print(df)
data = pd.read_csv("/Users/guanlizhe/Desktop/code/python/web_crawer/ptt_/kuan/com_index.csv", index_col=[0])
print(data)



