#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path ## for better path operation

def ls_dir(path="."):
    return [p for p in Path(path).iterdir() if p.is_dir()]

from lxml import etree
import os
import re

import logging
logging.basicConfig(level = logging.DEBUG)
allfiles = []###所有文件的path


def gen_filetree(startpath='.',filetype=""):
    '''利用os.walk 遍历某个目录，收集其内的文件，返回
    (文件路径列表, 本路径下的文件列表)
    比如:
    (['shortly'], ['shortly.py'])
(['shortly', 'templates'], ['shortly.py'])
(['shortly', 'static'], ['shortly.py'])

    第一个可选参数 startpath  默认值 '.'
    第二个参数  filetype  正则表达式模板 默认值是"" 其作用是只选择某些文件
    如果是空值，则所有的文件都将被选中。比如 "html$|pdf$" 将只选中 html和pdf文件。
    '''
    for root, dirs, files in os.walk(startpath):
        dirs.sort()#排序
        filelist = []
        for f in files:
            fileName,fileExt = os.path.splitext(f)
            if filetype:
                if re.search(filetype,fileExt):
                    filelist.append(f)
            else:
                filelist = files
        if filelist:#空文件夹不加入
            dirlist = root.split(os.path.sep)
            dirlist = dirlist[1:]
            if dirlist:
                yield (dirlist, filelist)
            else:
                yield (['.'], filelist)


THE_INIT_STRING = r'''
#+TITLE: 我的网站
#+AUTHOR: 万泽(德山书生)
#+CREATOR: wanze(<a href="mailto:a358003542@163.com">a358003542@163.com</a>)
#+DESCRIPTION: 制作者邮箱：a358003542@gmail.com
#+OPTIONS: toc:2
#+HTML_HEAD: <link rel="stylesheet"  href="index.css"/>

----------------------
'''

def get_dirpath(dirlist):
    return os.path.join(*dirlist)

def get_filepath(dirlist,filename):
    return os.path.join(get_dirpath(dirlist),filename)

def inner_writer(indexorg,dirlist,filelist,last_dirlist):
    if dirlist:
        for i,d in enumerate(dirlist):
            logging.debug('{} {}'.format(dirlist,last_dirlist))
            try:
                if dirlist[i] != last_dirlist[i]:
                    indexorg.write("{} {}\n".format('*'*(i+1),d))
            except IndexError:
                indexorg.write("{} {}\n".format('*'*(i+1),d))

        for c,f in enumerate(filelist):

            indexorg.write("{count}. [[file:{path}][{filename}]]\n".format(path=get_filepath(dirlist,f),count=c+1,filename=f))


def make_sitemap():
    filename = os.path.join('.','index.org')
    with open(filename,'w') as indexorg:
        indexorg.write(THE_INIT_STRING)

        last_dirlist = []
        for dirlist,filelist in gen_filetree(filetype="html$|pdf$"):
            if 'templates' in dirlist:
                continue
            elif 'backups' in dirlist:
                continue
            elif 'images' in dirlist:
                continue
            elif dirlist == ['.']:
                continue

            print(dirlist,filelist)

            inner_writer(indexorg,dirlist,filelist,last_dirlist)
            last_dirlist = dirlist #remenber it


if __name__ == '__main__':
    make_sitemap()
    print('make indexorg complete')


