import requests
from bs4 import BeautifulSoup
import numpy as np
import re
import json
import datetime
from Dao import Dao

class Crawl(object):
    def __init__(self):
        pass

    def crawl_news(self):
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers = {'User-Agent' : user_agent,}
        base_url = 'http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105'
        base_url2 = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105'

        page_url = 'http://news.naver.com/main/mainNews.nhn?componentId=949984&firstLoad=Y'
        page_res = requests.get(page_url)
        data = json.loads(page_res.content)
        page_counts = data['pagerInfo']['totalPages']

        news_dict= {}
        article_url_list = []
        for i in range(1, page_counts+1):
            url = 'http://news.naver.com/main/mainNews.nhn?componentId=949984&date={}%2000:00:00&page={}'.format(datetime.date.today(),i)

            res = requests.get(url, headers=headers)
            data = json.loads(res.text)

            for i in range(len(data['itemList'])):
                articleId = data['itemList'][i]['articleId']
                officeId = data['itemList'][i]['officeId']
                article_url = '{}&oid={}&aid={}'.format(base_url2, officeId, articleId)

                article_url_list.append(article_url)
                Title = data['itemList'][i]['title']

        for url in article_url_list:
            res2 = requests.get(url)
            soup2 = BeautifulSoup(res2.content)

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

        it_news_dao = Dao(news_dict)
        it_news_dao.insert_all()

crawling = Crawl()
crawling.crawl_news()
