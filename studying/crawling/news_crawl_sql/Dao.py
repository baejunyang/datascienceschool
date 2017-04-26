class Dao(object):
    def __init__(self, n_dict):
        self.n_dict = n_dict

    def session_add(self):
        import Model
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        import datetime
        import config

        connection_string = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(config.DB_USER, config.DB_PWD,
                                                                              config.DB_HOST, config.DB_PORT, config.DB_DB)
        engine = create_engine(connection_string, pool_recycle = 3600, encoding='utf-8')
        Session = sessionmaker(bind=engine)
        session = Session()

        for url in self.n_dict :
            news = Model.It(ID = url, Title = self.n_dict[url]['Title'], Body = self.n_dict[url]['Body'], Date = self.n_dict[url]['Date'])
            session.add(news)

        session.commit()
        session.close()
