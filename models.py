# coding: utf-8
from sqlalchemy import Column, Integer, JSON, Table, Text
from database import Base

class Tweet(Base):
    __tablename__ = 'tweets'
    user = Column(JSON)
    id = Column(Text, primary_key=True)
    conversation_id = Column(Text)
    full_text = Column(Text)
    reply_count = Column(Integer)
    retweet_count = Column(Integer)
    favorite_count = Column(Integer)
    hashtags = Column(JSON)
    symbols = Column(JSON)
    user_mentions = Column(JSON)
    urls = Column(JSON)
    url = Column(Text)
    created_at = Column(Text)

