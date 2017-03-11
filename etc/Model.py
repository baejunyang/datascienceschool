import os
import sys
from sqlalchemy import Column, Integer, CHAR, DateTime, String
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class It(Base):
    __tablename__='it'

    ID = Column(String(100), primary_key = True, nullable = False)
    Title = Column(String(400), nullable = False, default = 'it news')
    Body = Column(TEXT)
    Date = Column(DateTime, nullable = False, default = '2001-01-01 01:01:01')
