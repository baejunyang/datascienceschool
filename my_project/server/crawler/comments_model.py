import os
import sys
from sqlalchemy import Column, Integer, CHAR, DateTime, String
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Comment(Base):
    __tablename__='comments'

    id = Column(primary_key = True, nullable = False)
    text = Column(TEXT)
