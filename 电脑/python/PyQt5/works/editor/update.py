#!/usr/bin/env python3
#-*-coding:utf-8-*-

PROJECT_NAME = 'editor'


import subprocess
#update the translation
try:
    subprocess.call('pylupdate5 translations/{PROJECT_NAME}.pro'.format(PROJECT_NAME=PROJECT_NAME),shell=True)
except:
    sys.exit('build translation failed')

try:
    subprocess.call('pyrcc5 {PROJECT_NAME}.qrc -o {PROJECT_NAME}_rc.py'.format(PROJECT_NAME=PROJECT_NAME),shell=True)
except:
    sys.exit('build translation failed')

#if __name__ == '__main__':
