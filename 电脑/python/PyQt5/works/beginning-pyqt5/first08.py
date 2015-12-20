#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys

from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800,600)
        self.center()
        self.setWindowTitle('myapp')
        self.setWindowIcon(QIcon\
        ('icons/myapp.ico'))
    #菜单栏
        menu_control = self.menuBar().addMenu('Contorl')
        act_quit = menu_control.addAction('quit')
        act_quit.triggered.connect(self.close)

        menu_help = self.menuBar().addMenu('Help')
        act_about = menu_help.addAction('about...')
        act_about.triggered.connect(self.about)
        act_aboutqt = menu_help.addAction('aboutqt')
        act_aboutqt.triggered.connect(self.aboutqt)


    #状态栏
        self.statusBar().showMessage('程序已就绪...')
        self.show()

    def about(self):
        QMessageBox.about(self,"about this software","wise system")
    def aboutqt(self):
        QMessageBox.aboutQt(self)

    def closeEvent(self, event):
        #重新定义colseEvent
        reply = QMessageBox.question\
        (self, '信息',
            "你确定要退出吗？",
             QMessageBox.Yes,
             QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
     #center method
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2,\
         (screen.height()-size.height())/2)

myapp = QApplication(sys.argv)
mainwindow = MainWindow()
sys.exit(myapp.exec_())


