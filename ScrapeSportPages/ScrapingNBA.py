# -*- coding = utf-8 -*-

from bs4 import BeautifulSoup, SoupStrainer
import re
import urllib.error
import random
import socket
import urllib.request,sys,time
import requests


def getPageSource(baseurl):
    datalist = []
    html = askURL(baseurl)
    bs = BeautifulSoup(html, 'html.parser')

    return bs

def getAuthor(baseurl):
    authorList = []
    bs = getPageSource(baseurl)
    authorList = bs.find_all('p', attrs = {'class': 'contributor__text--name'})
    authors = []
    for author in authorList:
        authors.append(author.text.strip())

    return authors

def getParagraphList(baseurl):
    paraGraphlist = []
    bs = getPageSource(baseurl)
    paraGraphlist = bs.find_all('p', attrs={'class': 'Component-root-0-2-146 Component-p-0-2-137'})

    return paraGraphlist

def getSubTitle(baseurl):
    bs = getPageSource(baseurl)
    subTitle = bs.find('h2').text.strip()

    return(subTitle)

def getParagraphs(baseurl):
    paraGraphlist = getParagraphList(baseurl)
    paragraphs = []
    for paragraph in paraGraphlist:
        paragraphs.append(paragraph.text.strip())

    return paragraphs

def getArticleTime(baseurl):
    bs = getPageSource(baseurl)
    articleTime = bs.find('time').text.strip()

    return articleTime


def getArticleTitle(baseurl):
    title = ""
    bs = getPageSource(baseurl)
    title = bs.find('h1', attrs = {'class': 'h9'}).text.strip()
    return title

def getAllAttributes(baseurl):

    articleTitle = getArticleTitle(baseurl)
    articleTime = getArticleTime(baseurl)
    paragraphs = getParagraphs(baseurl)
    subTitle = getSubTitle(baseurl)
    author = getAuthor(baseurl)

    return((articleTitle, subTitle, author, articleTime, paragraphs))


def findUrls(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)

    return [x[0] for x in url]


def main():
    baseurl = "https://www.nba.com/"
    hawks_Hunter_surgery = "https://www.nba.com/news/hawks-forward-deandre-hunter-to-undergo-surgery-on-ailing-right-knee"
    print(getAllAttributes(hawks_Hunter_surgery))



def askURL(url):
    head = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58"
    }

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request, timeout=8)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    except socket.timeout as e:
        print(type(e))

    return html


if __name__ == '__main__':
    main()