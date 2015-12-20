create table if not exists department
 (dept_id int primary key,
  name varchar not null
 );


create table if not exists branch
 (branch_id int  primary key,
  name varchar not null,
  address varchar,
  city varchar,
  state varchar,
  zip varchar
 );

PRAGMA foreign_keys = ON;

create table if not exists employee
 (emp_id int  primary key,
  fname varchar not null,
  lname varchar not null,
  start_date date not null,
  end_date date,
  superior_emp_id int ,
  dept_id int ,
  title varchar,
  assigned_branch_id int ,
    foreign key (superior_emp_id) references employee (emp_id),
    foreign key (dept_id) references department (dept_id),
    foreign key (assigned_branch_id) references branch (branch_id)
 );

create table if not exists product_type
 (product_type_cd varchar not null,
  name varchar not null,
  primary key (product_type_cd)
 );

 create table if not exists product
 (product_cd varchar(10) not null,
  name varchar(50) not null,
  product_type_cd varchar(10) not null,
  date_offered date,
  date_retired date,
  foreign key (product_type_cd)
    references product_type (product_type_cd),
   primary key (product_cd)
 );

 create table if not exists customer
 (cust_id integer  not null ,
  fed_id varchar(12) not null,
  cust_type_cd  not null check(cust_type_cd in ('I','B')),
  address varchar(30),
  city varchar(20),
  state varchar(20),
  postal_code varchar(10),
    primary key (cust_id)
 );

 create table if not exists individual
 (cust_id integer  not null,
  fname varchar(30) not null,
  lname varchar(30) not null,
  birth_date date,
   foreign key (cust_id)
    references customer (cust_id),
   primary key (cust_id)
 );

 create table if not exists business
 (cust_id integer  not null,
  name varchar(40) not null,
  state_id varchar(10) not null,
  incorp_date date,
   foreign key (cust_id)
    references customer (cust_id),
   primary key (cust_id)
 );


 create table if not exists officer
 (officer_id smallint  not null ,
  cust_id integer  not null,
  fname varchar(30) not null,
  lname varchar(30) not null,
  title varchar(20),
  start_date date not null,
  end_date date,
   foreign key (cust_id)
    references business (cust_id),
   primary key (officer_id)
 );

 create table if not exists account
 (account_id integer  not null ,
  product_cd varchar(10) not null,
  cust_id integer  not null,
  open_date date not null,
  close_date date,
  last_activity_date date,
  status check(status in ('ACTIVE','CLOSED','FROZEN')),
  open_branch_id smallint ,
  open_emp_id smallint ,
  avail_balance float(10,2),
  pending_balance float(10,2),
   foreign key (product_cd)
    references product (product_cd),
   foreign key (cust_id)
    references customer (cust_id),
   foreign key (open_branch_id)
    references branch (branch_id),
   foreign key (open_emp_id)
    references employee (emp_id),
   primary key (account_id)
 );

 create table if not exists transaction_t
 (txn_id integer not null ,
  txn_date datetime not null,
  account_id integer  not null,
  txn_type_cd check(txn_type_cd in ('DBT','CDT')),
  amount float not null,
  teller_emp_id smallint ,
  execution_branch_id smallint ,
  funds_avail_date datetime,
   foreign key (account_id)
    references account (account_id),
   foreign key (teller_emp_id)
    references employee (emp_id),
   foreign key (execution_branch_id)
    references branch (branch_id),
  primary key (txn_id)
 );



 /* begin data population */
insert  or ignore   into department (dept_id, name)
values (1, 'Operations');
insert  or ignore   into department (dept_id, name)
values (2, 'Loans');
insert  or ignore   into department (dept_id, name)
values (3, 'Administration');



insert or ignore  into branch (branch_id, name, address, city, state, zip)
values (1, 'Headquarters', '3882 Main St.', 'Waltham', 'MA', '02451');
insert or ignore  into branch (branch_id, name, address, city, state, zip)
values (2, 'Woburn Branch', '422 Maple St.', 'Woburn', 'MA', '01801');
insert or ignore  into branch (branch_id, name, address, city, state, zip)
values (3, 'Quincy Branch', '125 Presidential Way', 'Quincy', 'MA', '02169');
insert or ignore  into branch (branch_id, name, address, city, state, zip)
values (4, 'So. NH Branch', '378 Maynard Ln.', 'Salem', 'NH', '03079');

/* employee data */
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (1, 'Michael', 'Smith', '2001-06-22',
  (select dept_id from department where name = 'Administration'),
  'President',
  (select branch_id from branch where name = 'Headquarters'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (2, 'Susan', 'Barker', '2002-09-12',
  (select dept_id from department where name = 'Administration'),
  'Vice President',
  (select branch_id from branch where name = 'Headquarters'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (3, 'Robert', 'Tyler', '2000-02-09',
  (select dept_id from department where name = 'Administration'),
  'Treasurer',
  (select branch_id from branch where name = 'Headquarters'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (4, 'Susan', 'Hawthorne', '2002-04-24',
  (select dept_id from department where name = 'Operations'),
  'Operations Manager',
  (select branch_id from branch where name = 'Headquarters'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (5, 'John', 'Gooding', '2003-11-14',
  (select dept_id from department where name = 'Loans'),
  'Loan Manager',
  (select branch_id from branch where name = 'Headquarters'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (6, 'Helen', 'Fleming', '2004-03-17',
  (select dept_id from department where name = 'Operations'),
  'Head Teller',
  (select branch_id from branch where name = 'Headquarters'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (7, 'Chris', 'Tucker', '2004-09-15',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Headquarters'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (8, 'Sarah', 'Parker', '2002-12-02',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Headquarters'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (9, 'Jane', 'Grossman', '2002-05-03',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Headquarters'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (10, 'Paula', 'Roberts', '2002-07-27',
  (select dept_id from department where name = 'Operations'),
  'Head Teller',
  (select branch_id from branch where name = 'Woburn Branch'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (11, 'Thomas', 'Ziegler', '2000-10-23',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Woburn Branch'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (12, 'Samantha', 'Jameson', '2003-01-08',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Woburn Branch'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (13, 'John', 'Blake', '2000-05-11',
  (select dept_id from department where name = 'Operations'),
  'Head Teller',
  (select branch_id from branch where name = 'Quincy Branch'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (14, 'Cindy', 'Mason', '2002-08-09',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Quincy Branch'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (15, 'Frank', 'Portman', '2003-04-01',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'Quincy Branch'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (16, 'Theresa', 'Markham', '2001-03-15',
  (select dept_id from department where name = 'Operations'),
  'Head Teller',
  (select branch_id from branch where name = 'So. NH Branch'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (17, 'Beth', 'Fowler', '2002-06-29',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'So. NH Branch'));
insert or ignore  into employee (emp_id, fname, lname, start_date,
  dept_id, title, assigned_branch_id)
values (18, 'Rick', 'Tulman', '2002-12-12',
  (select dept_id from department where name = 'Operations'),
  'Teller',
  (select branch_id from branch where name = 'So. NH Branch'));


/* create data for self-referencing foreign key 'superior_emp_id' */
create temporary table emp_tmp as
select emp_id, fname, lname from employee;

update employee set superior_emp_id =
 (select emp_id from emp_tmp where lname = 'Smith' and fname = 'Michael')
where ((lname = 'Barker' and fname = 'Susan')
  or (lname = 'Tyler' and fname = 'Robert'));
update employee set superior_emp_id =
 (select emp_id from emp_tmp where lname = 'Tyler' and fname = 'Robert')
where lname = 'Hawthorne' and fname = 'Susan';
update employee set superior_emp_id =
 (select emp_id from emp_tmp where lname = 'Hawthorne' and fname = 'Susan')
where ((lname = 'Gooding' and fname = 'John')
  or (lname = 'Fleming' and fname = 'Helen')
  or (lname = 'Roberts' and fname = 'Paula')
  or (lname = 'Blake' and fname = 'John')
  or (lname = 'Markham' and fname = 'Theresa'));
update employee set superior_emp_id =
 (select emp_id from emp_tmp where lname = 'Fleming' and fname = 'Helen')
where ((lname = 'Tucker' and fname = 'Chris')
  or (lname = 'Parker' and fname = 'Sarah')
  or (lname = 'Grossman' and fname = 'Jane'));
update employee set superior_emp_id =
 (select emp_id from emp_tmp where lname = 'Roberts' and fname = 'Paula')
where ((lname = 'Ziegler' and fname = 'Thomas')
  or (lname = 'Jameson' and fname = 'Samantha'));
update employee set superior_emp_id =
 (select emp_id from emp_tmp where lname = 'Blake' and fname = 'John')
where ((lname = 'Mason' and fname = 'Cindy')
  or (lname = 'Portman' and fname = 'Frank'));
update employee set superior_emp_id =
 (select emp_id from emp_tmp where lname = 'Markham' and fname = 'Theresa')
where ((lname = 'Fowler' and fname = 'Beth')
  or (lname = 'Tulman' and fname = 'Rick'));

drop table emp_tmp;


/* product type data */
insert or ignore  into product_type (product_type_cd, name)
values ('ACCOUNT','Customer Accounts');
insert or ignore  into product_type (product_type_cd, name)
values ('LOAN','Individual and Business Loans');
insert or ignore  into product_type (product_type_cd, name)
values ('INSURANCE','Insurance Offerings');


/* product data */
insert or ignore  into product (product_cd, name, product_type_cd, date_offered)
values ('CHK','checking account','ACCOUNT','2000-01-01');
insert or ignore  into product (product_cd, name, product_type_cd, date_offered)
values ('SAV','savings account','ACCOUNT','2000-01-01');
insert or ignore  into product (product_cd, name, product_type_cd, date_offered)
values ('MM','money market account','ACCOUNT','2000-01-01');
insert or ignore  into product (product_cd, name, product_type_cd, date_offered)
values ('CD','certificate of deposit','ACCOUNT','2000-01-01');
insert or ignore  into product (product_cd, name, product_type_cd, date_offered)
values ('MRT','home mortgage','LOAN','2000-01-01');
insert or ignore  into product (product_cd, name, product_type_cd, date_offered)
values ('AUT','auto loan','LOAN','2000-01-01');
insert or ignore  into product (product_cd, name, product_type_cd, date_offered)
values ('BUS','business line of credit','LOAN','2000-01-01');
insert or ignore  into product (product_cd, name, product_type_cd, date_offered)
values ('SBL','small business loan','LOAN','2000-01-01');



/* residential customer data */
insert or ignore  into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (1, '111-11-1111', 'I', '47 Mockingbird Ln', 'Lynnfield', 'MA', '01940');
insert or ignore  into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (2, '222-22-2222', 'I', '372 Clearwater Blvd', 'Woburn', 'MA', '01801');
insert or ignore  into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (3, '333-33-3333', 'I', '18 Jessup Rd', 'Quincy', 'MA', '02169');
insert or ignore  into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (4, '444-44-4444', 'I', '12 Buchanan Ln', 'Waltham', 'MA', '02451');
insert or ignore  into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (5, '555-55-5555', 'I', '2341 Main St', 'Salem', 'NH', '03079');
insert or ignore  into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (6, '666-66-6666', 'I', '12 Blaylock Ln', 'Waltham', 'MA', '02451');
insert or ignore  into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (7, '777-77-7777', 'I', '29 Admiral Ln', 'Wilmington', 'MA', '01887');
insert or ignore  into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (8, '888-88-8888', 'I', '472 Freedom Rd', 'Salem', 'NH', '03079');
insert or ignore  into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (9, '999-99-9999', 'I', '29 Maple St', 'Newton', 'MA', '02458');
insert or ignore  into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (10, '04-1111111', 'B', '7 Industrial Way', 'Salem', 'NH', '03079');
insert or ignore  into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (11, '04-2222222', 'B', '287A Corporate Ave', 'Wilmington', 'MA', '01887');
insert or ignore  into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (12, '04-3333333', 'B', '789 Main St', 'Salem', 'NH', '03079');
insert or ignore  into customer (cust_id, fed_id, cust_type_cd,
  address, city, state, postal_code)
values (13, '04-4444444', 'B', '4772 Presidential Way', 'Quincy', 'MA', '02169');


insert or ignore  into individual (cust_id, fname, lname, birth_date)
select cust_id, 'James', 'Hadley', '1972-04-22' from customer
where fed_id = '111-11-1111';
insert or ignore  into individual (cust_id, fname, lname, birth_date)
select cust_id, 'Susan', 'Tingley', '1968-08-15' from customer
where fed_id = '222-22-2222';
insert or ignore  into individual (cust_id, fname, lname, birth_date)
select cust_id, 'Frank', 'Tucker', '1958-02-06' from customer
where fed_id = '333-33-3333';
insert or ignore  into individual (cust_id, fname, lname, birth_date)
select cust_id, 'John', 'Hayward', '1966-12-22' from customer
where fed_id = '444-44-4444';
insert or ignore  into individual (cust_id, fname, lname, birth_date)
select cust_id, 'Charles', 'Frasier', '1971-08-25' from customer
where fed_id = '555-55-5555';
insert or ignore  into individual (cust_id, fname, lname, birth_date)
select cust_id, 'John', 'Spencer', '1962-09-14' from customer
where fed_id = '666-66-6666';
insert or ignore  into individual (cust_id, fname, lname, birth_date)
select cust_id, 'Margaret', 'Young', '1947-03-19' from customer
where fed_id = '777-77-7777';
insert or ignore  into individual (cust_id, fname, lname, birth_date)
select cust_id, 'Louis', 'Blake', '1977-07-01' from customer
where fed_id = '888-88-8888';
insert or ignore  into individual (cust_id, fname, lname, birth_date)
select cust_id, 'Richard', 'Farley', '1968-06-16' from customer
where fed_id = '999-99-9999';


insert or ignore  into business (cust_id, name, state_id, incorp_date)
select cust_id, 'Chilton Engineering', '12-345-678', '1995-05-01' from customer
where fed_id = '04-1111111';
insert or ignore  into business (cust_id, name, state_id, incorp_date)
select cust_id, 'Northeast Cooling Inc.', '23-456-789', '2001-01-01' from customer
where fed_id = '04-2222222';
insert or ignore  into business (cust_id, name, state_id, incorp_date)
select cust_id, 'Superior Auto Body', '34-567-890', '2002-06-30' from customer
where fed_id = '04-3333333';
insert or ignore  into business (cust_id, name, state_id, incorp_date)
select cust_id, 'AAA Insurance Inc.', '45-678-901', '1999-05-01' from customer
where fed_id = '04-4444444';



insert or ignore  into officer (officer_id, cust_id, fname, lname,
  title, start_date)
select 1, cust_id, 'John', 'Chilton', 'President', '1995-05-01'
from customer
where fed_id = '04-1111111';
insert or ignore  into officer (officer_id, cust_id, fname, lname,
  title, start_date)
select 2, cust_id, 'Paul', 'Hardy', 'President', '2001-01-01'
from customer
where fed_id = '04-2222222';
insert or ignore  into officer (officer_id, cust_id, fname, lname,
  title, start_date)
select 3, cust_id, 'Carl', 'Lutz', 'President', '2002-06-30'
from customer
where fed_id = '04-3333333';
insert or ignore  into officer (officer_id, cust_id, fname, lname,
  title, start_date)
select 4, cust_id, 'Stanley', 'Cheswick', 'President', '1999-05-01'
from customer
where fed_id = '04-4444444';


insert or ignore  into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 1, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Woburn' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2000-01-15' open_date, '2005-01-04' last_date,
    1057.75 avail, 1057.75 pend union all
  select 'SAV' prod_cd, '2000-01-15' open_date, '2004-12-19' last_date,
    500.00 avail, 500.00 pend union all
  select 'CD' prod_cd, '2004-06-30' open_date, '2004-06-30' last_date,
    3000.00 avail, 3000.00 pend) a
where c.fed_id = '111-11-1111';
insert or ignore  into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 2, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Woburn' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2001-03-12' open_date, '2004-12-27' last_date,
    2258.02 avail, 2258.02 pend union all
  select 'SAV' prod_cd, '2001-03-12' open_date, '2004-12-11' last_date,
    200.00 avail, 200.00 pend) a
where c.fed_id = '222-22-2222';
insert or ignore  into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 3, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Quincy' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2002-11-23' open_date, '2004-11-30' last_date,
    1057.75 avail, 1057.75 pend union all
  select 'MM' prod_cd, '2002-12-15' open_date, '2004-12-05' last_date,
    2212.50 avail, 2212.50 pend) a
where c.fed_id = '333-33-3333';
insert or ignore  into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 4, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Waltham' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2003-09-12' open_date, '2005-01-03' last_date,
    534.12 avail, 534.12 pend union all
  select 'SAV' prod_cd, '2000-01-15' open_date, '2004-10-24' last_date,
    767.77 avail, 767.77 pend union all
  select 'MM' prod_cd, '2004-09-30' open_date, '2004-11-11' last_date,
    5487.09 avail, 5487.09 pend) a
where c.fed_id = '444-44-4444';
insert or ignore  into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 5, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Salem' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2004-01-27' open_date, '2005-01-05' last_date,
    2237.97 avail, 2897.97 pend) a
where c.fed_id = '555-55-5555';
insert or ignore  into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 6, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Waltham' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2002-08-24' open_date, '2004-11-29' last_date,
    122.37 avail, 122.37 pend union all
  select 'CD' prod_cd, '2004-12-28' open_date, '2004-12-28' last_date,
    10000.00 avail, 10000.00 pend) a
where c.fed_id = '666-66-6666';
insert or ignore  into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 7, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Woburn' limit 1) e
  cross join
 (select 'CD' prod_cd, '2004-01-12' open_date, '2004-01-12' last_date,
    5000.00 avail, 5000.00 pend) a
where c.fed_id = '777-77-7777';
insert or ignore  into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 8, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Salem' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2001-05-23' open_date, '2005-01-03' last_date,
    3487.19 avail, 3487.19 pend union all
  select 'SAV' prod_cd, '2001-05-23' open_date, '2004-10-12' last_date,
    387.99 avail, 387.99 pend) a
where c.fed_id = '888-88-8888';
insert or ignore  into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 9, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Waltham' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2003-07-30' open_date, '2004-12-15' last_date,
    125.67 avail, 125.67 pend union all
  select 'MM' prod_cd, '2004-10-28' open_date, '2004-10-28' last_date,
    9345.55 avail, 9845.55 pend union all
  select 'CD' prod_cd, '2004-06-30' open_date, '2004-06-30' last_date,
    1500.00 avail, 1500.00 pend) a
where c.fed_id = '999-99-9999';


insert or ignore  into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 10, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Salem' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2002-09-30' open_date, '2004-12-15' last_date,
    23575.12 avail, 23575.12 pend union all
  select 'BUS' prod_cd, '2002-10-01' open_date, '2004-08-28' last_date,
    0 avail, 0 pend) a
where c.fed_id = '04-1111111';
insert or ignore  into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 11, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Woburn' limit 1) e
  cross join
 (select 'BUS' prod_cd, '2004-03-22' open_date, '2004-11-14' last_date,
    9345.55 avail, 9345.55 pend) a
where c.fed_id = '04-2222222';
insert or ignore  into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 12, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Salem' limit 1) e
  cross join
 (select 'CHK' prod_cd, '2003-07-30' open_date, '2004-12-15' last_date,
    38552.05 avail, 38552.05 pend) a
where c.fed_id = '04-3333333';
insert or ignore  into account (account_id, product_cd, cust_id, open_date,
  last_activity_date, status, open_branch_id,
  open_emp_id, avail_balance, pending_balance)
select 13, a.prod_cd, c.cust_id, a.open_date, a.last_date, 'ACTIVE',
  e.branch_id, e.emp_id, a.avail, a.pend
from customer c cross join
 (select b.branch_id, e.emp_id
  from branch b inner join employee e on e.assigned_branch_id = b.branch_id
  where b.city = 'Quincy' limit 1) e
  cross join
 (select 'SBL' prod_cd, '2004-02-22' open_date, '2004-12-17' last_date,
    50000.00 avail, 50000.00 pend) a
where c.fed_id = '04-4444444';

/* put $100 in all checking/savings accounts on date account opened */
insert or ignore  into transaction_t (txn_id, txn_date, account_id, txn_type_cd,
  amount, funds_avail_date)
select 1, a.open_date, a.account_id, 'CDT', 100, a.open_date
from account a
where a.product_cd IN ('CHK','SAV','CD','MM');

/* end data population */

