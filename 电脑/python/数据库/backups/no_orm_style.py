#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy import *
from sqlalchemy_utils import database_exists, create_database


engine = create_engine('sqlite:///:memory:',echo=True)

if not database_exists(engine.url):###确保目标数据库是存在的。
    create_database(engine.url)

db = MetaData(bind = engine)

try:
    users = Table('users',db,autoload=True)
except sqlalchemy.exc.NoSuchTableError:
    print('new table created')
    users = Table('users', db,
    Column('id', Integer, primary_key=True),
    Column('name', String(40)),
    Column('age', Integer),
    Column('password', String),
)

users.create(checkfirst=True)


insert_query = users.insert().prefix_with('or ignore')
insert_query.execute(id=1,name='Mary', age=30, password='secret')
insert_query.execute({'id':2,'name': 'John', 'age': 42},
    {'id':3,'name': 'Susan', 'age': 57},
    {'id':4,'name': 'Carl', 'age': 33})

delete_query = users.delete()

update_query = users.update()
update_query = update_query.where(users.c.name == 'John').values(password='123456')
update_query.execute()

def run(query):
    query.execute()

def show_squery(squery):
    res = squery.execute()
    for r in res:
        print(r)

try:
    emails = Table('emails',db,autoload=True)
except sqlalchemy.exc.NoSuchTableError:
    emails = Table('emails', db,
    Column('id', Integer, primary_key=True),
    Column('address', String),
    Column('user_id', Integer,ForeignKey('users.id')),
)

emails.create(checkfirst=True)

insert_query = emails.insert().prefix_with('or ignore')
insert_query.execute(
    {'id':1,'address': 'mary@example.com', 'user_id': 1},
    {'id':2,'address': 'john@nowhere.net', 'user_id': 2},
    {'id':3,'address': 'john@example.org', 'user_id': 2},
    {'id':4,'address': 'carl@nospam.net', 'user_id': 4},
)




#if __name__ == '__main__':
