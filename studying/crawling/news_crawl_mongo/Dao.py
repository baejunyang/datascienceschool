class Dao(object):
    def __init__(self, news_dict):
        self.news_dict = news_dict

    def insert_all(self):
        import pymongo
        from pymongo import MongoClient
        import config

        mongo = MongoClient(config.DB_HOST, config.DB_PORT_MONGO)

        it_news = mongo.news.it_news
        article_list = []

        for url in self.news_dict:
            article = {'_id':url, 'title':self.news_dict[url]['Title'], 'body':self.news_dict[url]['Body'], 'date':self.news_dict[url]['Date']}
            article_list.append(article)

        it_news.insert_many(article_list)
