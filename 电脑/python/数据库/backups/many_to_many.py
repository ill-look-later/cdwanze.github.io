#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///test2.db',echo=True)

if not database_exists(engine.url):
    print('create new database')
    create_database(engine.url)

metadata = MetaData(bind = engine)
Base = declarative_base(bind=engine)

blog_tags = Table('blog_tags',Base.metadata,
    Column('blog_id',Integer,ForeignKey('blogs.id')),
    Column('tag_id',Integer,ForeignKey('tags.id')))

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer,primary_key=True)
    title = Column(String)
    body = Column(String)

    tags = relationship("Tag",secondary=blog_tags,backref=backref('blogs'))

    def __init__(self,title,body):
        self.title = title
        self.body = body
    def __repr__(self):
        return '<BLog {}>'.format(self.title)

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer,primary_key=True)
    tag = Column(String)

    def __init__(self,tag):
        self.tag = tag
    def __repr__(self):
        return '<Tag {}>'.format(self.tag)

Base.metadata.create_all(checkfirst=True)### create table

Session = sessionmaker(bind=engine)
session = Session()

blog1 = Blog('learning mysql','how to learning mysql')
tag1 = Tag('python')
blog2 = Blog('learning sqlalchemy','how to learning sqlalchemy')
tag2 = Tag('sql')
tag3 = Tag('sqlalchemy')
tag4 = Tag('mysql')

blog1.tags.append(tag2)
blog1.tags.append(tag4)

blog2.tags.append(tag1)
blog2.tags.append(tag2)
blog2.tags.append(tag3)

session.add_all([blog1,blog2,tag1,tag2,tag3,tag4])

session.commit()

#if __name__ == '__main__':
