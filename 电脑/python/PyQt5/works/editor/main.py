#!/usr/bin/env python3
#-*-coding:utf-8-*-

import sys

#
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTranslator,QLocale

from Editor import Editor


#
def main():
    app = QApplication(sys.argv)

    translator = QTranslator()
    if translator.load('editor_'+ QLocale.system().name()+'.qm',":/translations/"):
        app.installTranslator(translator)

    translator_qt = QTranslator()
    if translator_qt.load('qt_'+ QLocale.system().name()+'.qm',":/translations/"):
    #    print('i found qt')
        app.installTranslator(translator_qt)


    mainwindow = Editor()
    mainwindow.setWindowTitle('simple text editor')
    mainwindow.setWindowIcon(QIcon(':/icons/editor.ico'))
    mainwindow.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
