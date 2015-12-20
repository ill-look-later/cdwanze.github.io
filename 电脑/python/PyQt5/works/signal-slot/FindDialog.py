#!/usr/bin/env python3
#-*-coding:utf-8-*-

from PyQt5.QtWidgets import QDialog,QLabel,QLineEdit,QCheckBox,QPushButton,QHBoxLayout,QVBoxLayout,QApplication
from PyQt5.QtCore import  Qt ,pyqtSignal,QObject,pyqtSlot


class FindDialog(QDialog):
    findNext = pyqtSignal(str,Qt.CaseSensitivity)
    findPrevious = pyqtSignal(str,Qt.CaseSensitivity)

    def __init__(self,parent=None):
        super().__init__(parent)
        label = QLabel(self.tr("Find &what:"))
        self.lineEdit = QLineEdit()
        label.setBuddy(self.lineEdit)

        self.caseCheckBox=QCheckBox(self.tr("Match &case"))
        self.backwardCheckBox=QCheckBox(self.tr("Search &backward"))
        self.findButton = QPushButton(self.tr("&Find"))
        self.findButton.setDefault(True)
        self.findButton.setEnabled(False)
        closeButton=QPushButton(self.tr("Close"))

        self.lineEdit.textChanged.connect(self.enableFindButton)
        self.findButton.clicked.connect(self.findClicked)
        closeButton.clicked.connect(self.close)

        topLeftLayout=QHBoxLayout()
        topLeftLayout.addWidget(label)
        topLeftLayout.addWidget(self.lineEdit)
        leftLayout=QVBoxLayout()
        leftLayout.addLayout(topLeftLayout)
        leftLayout.addWidget(self.caseCheckBox)
        leftLayout.addWidget(self.backwardCheckBox)
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.findButton)
        rightLayout.addWidget(closeButton)
        rightLayout.addStretch()
        mainLayout=QHBoxLayout()
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)
        self.setLayout(mainLayout)

        self.setWindowTitle(self.tr("Find"))
        self.setFixedHeight(self.sizeHint().height())


    def enableFindButton(self,text):
        self.findButton.setEnabled(bool(text))
    @pyqtSlot()
    def findClicked(self):
        text = self.lineEdit.text()
        if self.caseCheckBox.isChecked():
            cs=Qt.CaseSensitive
        else:
            cs=Qt.CaseInsensitive

        if self.backwardCheckBox.isChecked():
            self.findPrevious.emit(text,cs)
        else:
            self.findNext.emit(text,cs)



if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    findDialog = FindDialog()
    def find(text,cs):
        print('find:',text,'cs',cs)
    def findp(text,cs):
        print('findp:',text,'cs',cs)

    findDialog.findNext.connect(find)
    findDialog.findPrevious.connect(findp)
    findDialog.show()
    sys.exit(app.exec_())
