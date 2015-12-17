#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#### txt
#### type oneline one value OLOV
#### type a = b  one line two value  OLTV delimitet
#### type a b one line two value    OLTV
def parse_txt_as_OLOV(intxt):
    f = open(intxt,'r')
    for line in f:
        yield line


def generate_org_ul(lst):
    content = ''
    for v in lst:
        string = "- {}".format(v)
        content += string
    return content


def addto_orgfile(orgfile,content):
    with open(orgfile,'a') as f:
        f.write(content)

addto_orgfile('胶粘剂原料清单.org',generate_org_ul(list(parse_txt_as_OLOV('原料清单.txt'))))

#if __name__ == '__main__':
