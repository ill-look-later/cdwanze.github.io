#!/usr/bin/env python3
#-*-coding:utf-8-*-

from PyQt5.QtGui import QColor,QPalette,QBrush,QPixmap,QPolygon,QPainter
from PyQt5.QtCore import QPoint,QTimer,Qt
from PyQt5.QtWidgets import QWidget,QApplication,QAction

import math,sys,os
from datetime import datetime
from collections import *
try:
    import funnyclock.funnyclock_rc
    imgPath = ":/icons/clock.png"
except:
    imgPath = './icons/clock.png'

class Clock(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent,Qt.FramelessWindowHint)

        self.checktime()

        self.hourColor=QColor(127, 0, 127);
        self.minuteColor=QColor(0, 127, 127, 191)
        self.secondColor=QColor(127, 127,0,120)

        self.initUI()

        quitAction = QAction("E&xit", self, shortcut="Ctrl+Q",
                triggered=self.close)
        self.addAction(quitAction)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.timer = QTimer()
        self.timer.setInterval(1000)#毫秒
        self.timer.timeout.connect(self.update)
        self.timer.start()



    def handChange(self):
        self.side = min(self.width(), self.height())
        self.hand=(max(self.side/200,4), max(self.side/100,8), max(self.side/40,30))
        self.hourHand=QPolygon([QPoint(self.hand[0],self.hand[1]),QPoint(-self.hand[0],self.hand[1]),QPoint(0,-self.hand[2])])
        self.minuteHand=QPolygon([QPoint(self.hand[0],self.hand[1]),QPoint(-self.hand[0],self.hand[1]),QPoint(0,-self.hand[2]*1.6)])
        self.secondHand=QPolygon([QPoint(self.hand[0],self.hand[1]),QPoint(-self.hand[0],self.hand[1]),QPoint(0,-self.hand[2]*1.6*1.6)])


    def initUI(self):
        self.setFixedSize(291, 291)
        self.handChange()

    def paintEvent(self, pe):
        painter = QPainter()
        painter.begin(self)
        self.draw(pe, painter)
        painter.end()

    def draw(self, pe, painter):
        self.checktime()
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(self.side / 200.0, self.side / 200.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(self.hourColor)
        painter.save()
        painter.rotate(30.0 * ((self.time.hour + self.time.minute/ 60.0)))
        painter.drawConvexPolygon(self.hourHand)
        painter.restore()

        painter.setPen(Qt.NoPen)
        painter.setBrush(self.minuteColor)
        painter.save()

        painter.rotate(6.0 * ((self.time.minute + (self.time.second) / 60.0)))
        painter.drawConvexPolygon(self.minuteHand)
        painter.restore()

        painter.setPen(Qt.NoPen)
        painter.setBrush(self.secondColor)
        painter.save()
        painter.rotate(6.0*(self.time.second))
        painter.drawConvexPolygon(self.secondHand)
        painter.restore()


    def checktime(self):
        self.time = datetime.now()
        self.hour=self.time.hour
        self.minute=self.time.minute
        self.second=self.time.second

    #拖拽
    def mouseMoveEvent(self, me):
     #   print(me.globalPos())
        if me.buttons() & Qt.LeftButton:
            self.move(me.globalPos()-self.dragPos)
            me.accept()
    def mousePressEvent(self, me):
        if me.button() == Qt.LeftButton:
            self.dragPos=me.globalPos()-self.frameGeometry().topLeft()
            me.accept()

def main():
    app = QApplication(sys.argv)
    palette = QPalette()
    brush = QBrush(QPixmap(imgPath))
    palette.setBrush(QPalette.Window,brush)
    clock = Clock()
    clock.setPalette(palette)


    clock.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
