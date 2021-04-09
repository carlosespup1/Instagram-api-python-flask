import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    first_name = Column(String(25), nullable=False)
    las_name = Column(String(25))
    email = Column(String(60), nullable=False, unique=True)
    post = relationship('Post')
    comment = relationship('Comment')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = relationship('Comment')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    content = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Integer, nullable=False)
    url = Column(String(255), nullable=False, unique=True)
    post_id = Column(Integer, ForeignKey('post.id'))

"""
class Follower(Base):
    __tablename__ = follower
    user_from_id = Column(Integer)
    user_to_id = Column(Integer)
"""

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')