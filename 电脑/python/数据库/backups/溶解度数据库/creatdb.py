#!/usr/bin/env python3
#-*-coding:utf-8-*-

import xlrd
import sqlite3
import logging

from actionbrain import setup_logging


def xls2sql(infile,outfile,tablename):
    workbook =xlrd.open_workbook(infile)
    sheet1=workbook.sheet_by_index(0)
    data=[[sheet1.cell_value(r,c) for c in range(sheet1.ncols)] for r in range(sheet1.nrows)]

    dbname=outfile
    db=sqlite3.connect(dbname)
    conn = db.cursor()

    execute_sql = 'create table if not exists {}(id integer primary key autoincrement ,'.format(tablename)
    lst = []
    for i,d in enumerate(data[0]):
        if isinstance(data[1][i],int):
            t = 'integer'
        elif isinstance(data[1][i],float):
            t = 'real'
        else:
            t = 'text'
        lst.append('{} {}'.format(d,t))
    execute_sql = execute_sql + ','.join(lst) + ')'
    logging.debug(execute_sql)

    db.execute(execute_sql)

    conn.execute('select * from {}'.format(tablename))
    if conn.fetchone():
        logging.debug('not insert and closed the db')
        db.close()
        return False
    else:
        for row in range(1,len(data)):
            execute_sql = 'insert into {} values(?,{})'.format(tablename, ','.join(['?']*len(data[0])))
            logging.debug(execute_sql)
            db.execute(execute_sql , [row] + data[row])
        db.commit()
        db.close()
        return True


if __name__ == '__main__':
    setup_logging('test')
    xls2sql('solubility.xls','solubility.db','inwater')
