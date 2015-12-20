#!/usr/bin/env python3
#-*-coding:utf-8-*-

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QGridLayout

class Form(QWidget):
    def __init__(self):
        super().__init__()
        bodyLayout = QGridLayout()
        for i in range(1,10):
            button = QPushButton(str(i))
            bodyLayout.addWidget(button,(i-1)//3,(i-1)%3)
            print(i,(i-1)//3,(i-1)%3)
        self.setLayout(bodyLayout)
        self.setWindowTitle("the grid layout")
        self.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = Form()
    sys.exit(app.exec_())
