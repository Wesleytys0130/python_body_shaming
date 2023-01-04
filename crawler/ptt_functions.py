import bs4, re
import urllib.request as req
def changedate(str):
    if 'Jan' in str:
        return '01'
    elif 'Feb' in str:
        return '02'
    elif 'Mar' in str:
        return '03'
    elif 'Apr' in str:
        return '04'
    elif 'May' in str:
        return '05'
    elif 'Jun' in str:
        return '06'
    elif 'Jul' in str:
        return '07'
    elif 'Aug' in str:
        return '08'
    elif 'Sep' in str:
        return '09'
    elif 'Oct' in str:
        return '10'
    elif 'Nov' in str:
        return '11'
    elif 'Dec' in str:
        return '12'

def article(url):
    #建立一個Request物件，附加Request Headers 的資訊
    request = req.Request(url, headers={"cookie" : "over18=1","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36(KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    html = bs4.BeautifulSoup(data, "html.parser")
    # artdic = {'art':{"artID":[],"art_title":[],"art_time":[],"art_text":[]},'com':{"userID":[], "tag":[], "content":[], "date":[], "year":[]}}
    artdic = {"artID":[],"art_title":[],"art_time":[],"art_text":[]}
   
    arthtml = html.find_all("div", class_="article-metaline")
    artID =re.search('作者<\/span><span class="article-meta-value">.*<\/span><\/div>, <div class="article-metaline"><span class="article-meta-tag">標題',str(arthtml))
    art_title = re.search('標題<\/span><span class="article-meta-value">.*<\/span><\/div>, <div class="article-metaline"><span class="article-meta-tag">時間',str(arthtml))
    art_time = re.search(' [A-Za-z]+ .*\d',str(arthtml))
    if artID == None or art_title == None or art_time == None:
        print("None")
    else:
        artID=re.sub('作者<\/span><span class="article-meta-value">',"",artID.group())
        artID=re.sub('<\/span><\/div>, <div class="article-metaline"><span class="article-meta-tag">標題',"",artID)
        artdic["artID"].append(str(artID))
        
        art_title = re.sub('標題<\/span><span class="article-meta-value">',"",art_title.group())
        art_title = re.sub('<\/span><\/div>, <div class="article-metaline"><span class="article-meta-tag">時間',"",art_title)
        artdic["art_title"].append(str(art_title))

        art_time = re.sub('\w*:\w*:\w* ',"",art_time.group())
        mon = changedate(art_time)
        art_time = re.sub(' [A-Z].. ',mon+'/',art_time)
        artdic["art_time"].append(str(art_time))

    art_text = html.find_all("div", class_="bbs-screen")
    art_text = re.sub("\[<div.*<\/span><\/div>\n","",str(art_text))
    art_text = re.sub('<div class="push">.*\n<\/span><\/div>',"",art_text)
    art_text = re.sub('<span.*\n<\/span>',"",art_text)
    art_text = re.sub('\n--\n',"",art_text)
    art_text = re.sub('</div>]',"",art_text)
    if '<a' in art_text:
        art_text = re.sub('<a.*<\/a>',"",art_text)
    if '<div' in art_text:
        art_text = re.sub('<div.*<\/div>',"",art_text)
    if '<span' in art_text:
        art_text = re.sub('<span.*<\/span>',"",art_text)    
    artdic["art_text"].append(str(art_text))
    
    return artdic

def comments(url):
    #建立一個Request物件，附加Request Headers 的資訊
    request = req.Request(url, headers={"cookie" : "over18=1","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36(KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    html = bs4.BeautifulSoup(data, "html.parser")
    comdic = {"userID":[], "tag":[], "content":[], "date":[], "year":[]}
    

    comments=html.find_all("div", class_="push") #尋找所有 class="push"的 div 標籤
    year=html.find_all("span", class_="article-meta-value")
    year=re.search(":\d\d \d+<\/span>",str(year))
    if year == None:
        print(year)
    else:
        year=re.sub("<\/span>","",year.group())
        year=re.sub(":\d*","",year)

    for comment in comments:
        if "warning-box" not in str(comment):
            userID = comment.find("span",class_="push-userid").string
            tag = comment.find("span",class_="push-tag").string
            content = comment.find("span",class_="push-content").string
            date = comment.find("span",class_="push-ipdatetime").string
            date = re.search("\d+\/\d+",str(date))
            if userID != None and tag != None and content != None and date != None:
                comdic["userID"].append(str(userID))

                tag_clear = re.sub(' ','',str(tag))
                comdic["tag"].append(tag_clear)

                content_clear = re.sub(': ','',str(content)) #清理留言特殊符號和空白
                content_clear = re.sub("', ",'',content_clear)
                comdic["content"].append(content_clear)

                comdic["date"].append(date.group())
                comdic["year"].append(year)
            else:
                continue

    return comdic

# arturl = 'https://www.ptt.cc/bbs/FITNESS/M.1670330731.A.7FA.html'
# print(article(arturl))
    
def geturl(url):
    #建立一個 Resquest 物件，附加 Request Headers 的資訊
    request = req.Request(url, headers=
    {"cookie" : "over18=1","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data,"html.parser")#讓Beautifulsoup 協助我們解析 HTML 格式文件
    titles= root.find_all("div", class_="title")# 尋找所有 class="title" 的 div 標籤    
    articles =[]
    for title in titles:
        if title.a != None: # 如果標題包含 a 標籤（"沒有被刪除"），增加標題網址進articles
            articles.append("https://www.ptt.cc"+title.a["href"])
    return articles


