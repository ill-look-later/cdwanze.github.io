#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///test.db',echo=True)

if not database_exists(engine.url):
    print('create new database')
    create_database(engine.url)

metadata = MetaData(bind = engine)
Base = declarative_base(bind=engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    password = Column(String)
    email = relationship("Email",backref=backref('user'))

    def __init__(self,name,password):
        self.name = name
        self.password = password
    def __repr__(self):
        return '<User {}>'.format(self.name)

class Email(Base):
    __tablename__ = 'emails'

    id = Column(Integer,primary_key=True)
    email = Column(String)
    user_id = Column(Integer,ForeignKey('users.id'))

    def __init__(self,email,user_id):
        self.email = email
        self.user_id = user_id
    def __repr__(self):
        return '<Email {}>'.format(self.email)

Base.metadata.create_all(checkfirst=True)### create table


Session = sessionmaker(bind=engine)
session = Session()

admin = User('admin','admin')
session.add(admin)
session.add_all([User('Mary','secret'),
    User('John','123456'),
    User('Susan','123456'),
    User('Carl','123456')])

session.add_all([Email('mary@example.com',2),
    Email('john@nowhere.net',3),
    Email('john@example.org',3),
    Email('carl@nospam.net',4)])

john = session.query(User).filter(User.name == 'John').one()
e1 = session.query(Email).filter(Email.email == 'john@example.org').one()


#if __name__ == '__main__':
