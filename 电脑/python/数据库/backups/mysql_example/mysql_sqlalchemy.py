#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy_utils import database_exists, create_database


engine = create_engine('mysql+pymysql://root@localhost/learning_example_python',
    echo=True)

if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))

metadata = MetaData(bind=engine)

table_department = Table(
    'department',metadata,
    Column('dept_id',SmallInteger,primary_key=True),
    Column('name',String(20),nullable=False)
    )

table_branch = Table(
    'branch',metadata,
    Column('branch_id',SmallInteger,nullable=False,primary_key=True),
    Column('name',String(20),nullable=False),
    Column('address',String(30)),
    Column('city',String(20)),
    Column('state',String(2)),
    Column('zip',String(12))
    )

table_employee = Table(
    'employee',metadata,
    Column('emp_id',SmallInteger,nullable=False,primary_key=True),
    Column('fname',String(20),nullable=False),
    Column('lname',String(20),nullable=False),
    Column('start_date',Date,nullable=False),
    Column('end_date',Date),
    Column('superior_emp_id',SmallInteger,ForeignKey('employee.emp_id')),
    Column('dept_id',SmallInteger,ForeignKey('department.dept_id')),
    Column('title',String(20)),
    Column('assigned_branch_id',SmallInteger,ForeignKey('branch.branch_id'))
    )

metadata.create_all()

conn = engine.connect()

insert_statement = table_department.insert()
print(insert_statement,insert_statement.compile().params)
insert_statement = insert_statement.values(dept_id=1,name='Operations')
print(insert_statement,insert_statement.compile().params)
insert_statement = insert_statement.prefix_with('ignore')
print(insert_statement,insert_statement.compile().params)
conn.execute(insert_statement)

insert_statement = table_department.insert()
insert_statement = insert_statement.values(dept_id=2,name='Loans')
insert_statement = insert_statement.prefix_with('ignore')
conn.execute(insert_statement)

insert_statement = table_department.insert(values=dict(dept_id=3,name='Administration')).prefix_with('ignore')
print(insert_statement,insert_statement.compile().params)
conn.execute(insert_statement)


conn.execute('''
insert ignore into branch (branch_id, name, address, city, state, zip)
values (1, 'Headquarters', '3882 Main St.', 'Waltham', 'MA', '02451');''')

conn.execute('''
insert ignore into branch (branch_id, name, address, city, state, zip)
values (2, 'Woburn Branch', '422 Maple St.', 'Woburn', 'MA', '01801');
''')

conn.execute('''
insert ignore into branch (branch_id, name, address, city, state, zip)
values (3, 'Quincy Branch', '125 Presidential Way', 'Quincy', 'MA', '02169');
''')


conn.execute('''
insert ignore into branch (branch_id, name, address, city, state, zip)
values (4, 'So. NH Branch', '378 Maynard Ln.', 'Salem', 'NH', '03079');
''')

conn.execute('''insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (1, 'Michael', 'Smith', '2001-06-22',
  (select dept_id from department where name = 'Administration'),
  'President',
  (select branch_id from branch where name = 'Headquarters'));
''')

from sqlalchemy.sql import text

conn.execute(text(
'''
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (2, 'Susan', 'Barker', '2002-09-12',
  (select dept_id from department where name = 'Administration'),
  'Vice President',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (3, 'Robert', 'Tyler', '2000-02-09',
  (select dept_id from department where name = 'Administration'),
  'Treasurer',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (4, 'Susan', 'Hawthorne', '2002-04-24',
  (select dept_id from department where name = 'Operations'),
  'Operations Manager',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (5, 'John', 'Gooding', '2003-11-14',
  (select dept_id from department where name = 'Loans'),
  'Loan Manager',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (6, 'Helen', 'Fleming', '2004-03-17',
  (select dept_id from department where name = 'Operations'),
  'Head Teller',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (7, 'Chris', 'Tucker', '2004-09-15',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (8, 'Sarah', 'Parker', '2002-12-02',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (9, 'Jane', 'Grossman', '2002-05-03',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Headquarters'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (10, 'Paula', 'Roberts', '2002-07-27',
  (select dept_id from department where name = 'Operations'),
  'Head Teller',
  (select branch_id from branch where name = 'Woburn Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (11, 'Thomas', 'Ziegler', '2000-10-23',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Woburn Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (12, 'Samantha', 'Jameson', '2003-01-08',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Woburn Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (13, 'John', 'Blake', '2000-05-11',
  (select dept_id from department where name = 'Operations'),
  'Head Teller',
  (select branch_id from branch where name = 'Quincy Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (14, 'Cindy', 'Mason', '2002-08-09',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Quincy Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (15, 'Frank', 'Portman', '2003-04-01',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Quincy Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (16, 'Theresa', 'Markham', '2001-03-15',
  (select dept_id from department where name = 'Operations'),
  'Head Teller',
  (select branch_id from branch where name = 'So. NH Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (17, 'Beth', 'Fowler', '2002-06-29',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'So. NH Branch'));
insert ignore into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (18, 'Rick', 'Tulman', '2002-12-12',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'So. NH Branch'));
'''))




#if __name__ == '__main__':
