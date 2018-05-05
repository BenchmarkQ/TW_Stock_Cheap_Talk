import requests
from bs4 import BeautifulSoup as bs4
import logging
import json
import sqlite3
import pdb
class PTTData():
    def __init__(self):
        self.url = 'https://www.ptt.cc/bbs/Stock/index.html'
        self.articles_dict = {}
    def Connect(self):
        page = requests.get(self.url)
        soup = bs4(page.text,'lxml')
        articles = soup.select('div.title a') 
        self.Articles(articles)
        paging = soup.select("div.btn-group-paging a")
        self.url = 'https://www.ptt.cc' + paging[1]['href']
    def Articles(self,articles):
        for article in articles:
            print(article.text,article['href'])
            article_page = requests.get('http://www.ptt.cc'+article['href'])
            article_soup = bs4(article_page.text,'lxml')
            content = article_soup.find('div',{'id':"main-content",'class':"bbs-screen bbs-content"})
            main_content = content.find(text = True , recursive = False)
            push_content = content.find_all('div',{'class',"push"})
            push_content = [push.text for push in push_content]
            self.articles_dict.update({article.text:[main_content]+push_content}) 
    def GetPTTData(self,pages=3):
        for page in range(pages):
            self.Connect()
        return self.articles_dict
Data = PTTData()
articles = Data.GetPTTData()
with open('test.txt','w') as file:
    file.write(json.dumps(articles,ensure_ascii=False))
pdb.set_trace()
