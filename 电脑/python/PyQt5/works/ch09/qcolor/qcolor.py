#!/usr/bin/env python3
#-*-coding:utf-8-*-

from PyQt5.QtWidgets import QDialog,QLabel,QApplication,QVBoxLayout,QLabel,QFormLayout,QSlider
from PyQt5.QtGui import QPalette,QColor,QPainter,QBrush
from PyQt5.QtCore import Qt
class ColorConvertor(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.colorR = 255
        self.colorG = 255
        self.colorB = 255
        self.opacity = 255
        self.color = QColor(self.colorR,self.colorG,self.colorB)
        #RGB
        rgbLayout=QFormLayout()
        labelR = QLabel("R")
        self.sliderR = QSlider(Qt.Horizontal)
        labelG = QLabel("G")
        self.sliderG = QSlider(Qt.Horizontal)
        labelB = QLabel("B")
        self.sliderB = QSlider(Qt.Horizontal)
        labelOpacity = QLabel("opacity")
        self.sliderOpacity = QSlider(Qt.Horizontal)
        for (l,s) in ((labelR,self.sliderR),(labelG,self.sliderG),(labelB,self.sliderB),(labelOpacity,self.sliderOpacity)):
            rgbLayout.addRow(l,s)
            s.setMinimum(0)
            s.setMaximum(255)
            s.setValue(255)
            s.setSingleStep(10)
            s.valueChanged.connect(self.changeColor)


        self.label = QLabel()
        self.label.setTextInteractionFlags(Qt.TextSelectableByMouse)#可复制
        self.label.setText('''RGB:{colorR} {colorG} {colorB}  HTML:#{colorR:02X}{colorG:02X}{colorB:02X}
opacity:{opacity}'''.format(colorR=self.colorR,colorG=self.colorG,colorB=self.colorB,opacity=self.opacity))

        mainLayout=QVBoxLayout()
        mainLayout.addLayout(rgbLayout)
        mainLayout.addWidget(self.label)

        self.setLayout(mainLayout)

    def paintEvent(self,event):
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(event.rect(),QBrush(self.color))
        painter.end()


    def changeColor(self,value):
        self.colorR = self.sliderR.value()
        self.colorG = self.sliderG.value()
        self.colorB = self.sliderB.value()
        self.opacity = self.sliderOpacity.value()
        self.color = QColor(self.colorR,self.colorG,self.colorB,self.opacity)

        self.label.setText('''RGB:{colorR} {colorG} {colorB}  HTML:#{colorR:02X}{colorG:02X}{colorB:02X}
opacity:{opacity}'''.format(colorR=self.colorR,colorG=self.colorG,colorB=self.colorB,opacity=self.opacity))
        self.update()


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    colorConvertor = ColorConvertor()
    colorConvertor.show()

    sys.exit(app.exec_())
