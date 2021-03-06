# 爬PTT文章

import requests
from bs4 import BeautifulSoup as bs4
import logging
import json
import sqlite3
import pdb
import time
class PTTData():
    def __init__(self):
        self.url = 'https://www.ptt.cc/bbs/Stock/index.html'
        self.articles_list = []
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
            try:
                time = article_soup.find_all('div',{'class':'article-metaline'})[2].text.replace('時間','')
            except IndexError as e:
                print(article['href'])
                print(e)
                continue
            content = article_soup.find('div',{'id':"main-content",'class':"bbs-screen bbs-content"})
            main_content = content.find_all(text = True , recursive = False)
            main_content = ''.join(main_content)
            push_content = content.find_all('div',{'class',"push"})
            push_content = [push.text for push in push_content]
            result_dict = {
                    'title':article.text,
                    'time':time,
                    'main_content':main_content,
                    'push_content':push_content,
                    }
            self.articles_list.append(result_dict) 
    def GetPTTData(self,pages = 100):
        for page in range(pages):
            self.Connect()
        return self.articles_list

if __name__ == '__main__':
    Data = PTTData()
    articles = Data.GetPTTData()
    with open('test.txt','w') as file:
        json.dump(articles, file)
