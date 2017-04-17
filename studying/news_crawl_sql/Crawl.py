import requests
from bs4 import BeautifulSoup
import numpy as np
import re
from Dao import Dao

class Crawl(object):
    def __init__(self):
        pass

    def crawl_news(self):
        res = requests.get('http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105')
        soup = BeautifulSoup(res.content)
        div = soup.find('div', attrs = {'id' : 'section_body'})
        lis = div.find_all('li')
        links = []
        for i, li in enumerate(lis):
            links.append(li.a['href'])

        news_dict= {}
        for url in links:
            try:
                res2 = requests.get(url)
                soup2 = BeautifulSoup(res2.content)

                h3 = soup2.find('h3', {'id' : 'articleTitle'})
                Title = h3.get_text().encode('utf-8')
            except :
                Title = 'no Title'

            news_dict[url] = {'Title' : Title}

            try:
                div = soup2.find('div', {'id':'articleBodyContents'})
                div.script.extract()
                Body = div.get_text().strip().encode('utf-8')
            except :
                Body = 'no Body'

            news_dict[url]['Body'] = Body

            try:
                span = soup2.find('span', {'class' : 't11'})
                Date = span.get_text()
            except :
                Date = '2001-01-01 01:01'

            news_dict[url]['Date'] = Date

        news_dao = Dao(news_dict)
        news_dao.session_add()

crawler = Crawl()
crawler.crawl_news()
