#!/usr/bin/env python3
#-*-coding:utf-8-*-

import sys

from timer import __version__ , __softname__

#
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTranslator,QLocale

from timer.Timer import Timer

#
def gui():
    app = QApplication(sys.argv)

    translator = QTranslator()
    if translator.load('wise_'+ QLocale.system().name()+'.qm',":/translations/"):
        app.installTranslator(translator)

    translator_qt = QTranslator()
    if translator_qt.load('qt_'+ QLocale.system().name()+'.qm',":/translations/"):
        print('i found qt')
        app.installTranslator(translator_qt)


    timer = Timer()
    def beep():
        print('\a')
    timer.timeout.connect(beep)
    timer.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    gui()


#if __name__ == '__main__':
