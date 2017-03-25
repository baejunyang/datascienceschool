class Dao(object):
    def __init__(self, n_dict):
        self.n_dict = n_dict

    def session_add(self):
        import comments_model
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        import datetime
        import config

        connection_string = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(config.DB_USER, config.DB_PWD,
                                                                              config.DB_HOST, config.DB_PORT, config.DB_Comment)
        engine = create_engine(connection_string, pool_recycle = 3600, encoding='utf-8')
        Session = sessionmaker(bind=engine)
        session = Session()

        for i in range(len(self.n_dict['date'])) :
            comment = comments_model.Comment(text = self.n_dict['text'][i], date = self.n_dict['date'][i])
            session.add(comment)

        session.commit()
        session.close()
