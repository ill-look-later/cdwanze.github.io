#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import  *

import editor_rc

from PyQt5.uic import loadUi

class Editor(QMainWindow):
    def __init__(self,parent=None, *args):
        super().__init__(parent, *args)

        self.curFile = ''

        self.mainUi = loadUi('editor.ui', self)

        self.mainUi.action_New.triggered.connect(self.newFile)
        self.mainUi.action_Open.triggered.connect(self.open)
        self.mainUi.action_Save.triggered.connect(self.save)
        self.mainUi.action_SaveAs.triggered.connect(self.saveAs)
        self.mainUi.action_Quit.triggered.connect(self.close)


        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.mainUi.action_Cut.triggered.connect(self.textEdit.cut)
        self.mainUi.action_Copy.triggered.connect(self.textEdit.copy)
        self.mainUi.action_Paste.triggered.connect(self.textEdit.paste)

        self.mainUi.action_About.triggered.connect(self.about)
        self.mainUi.action_AboutQt.triggered.connect(QApplication.instance().aboutQt)

        self.getaction_Cut().setEnabled(False)
        self.getaction_Copy().setEnabled(False)
        self.textEdit.copyAvailable.connect(self.getaction_Cut().setEnabled)
        self.textEdit.copyAvailable.connect(self.getaction_Copy().setEnabled)

        self.statusBar().showMessage(self.tr("Ready"))

        self.readSettings()

        self.textEdit.textChanged.connect(self.setWindowModified)

        self.setCurrentFile('')

    @pyqtSlot()
    def closeEvent(self, event):
        if self.maybeSave():
            self.writeSettings()
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()
    def newFile(self):
        print('hello')
        if self.maybeSave():
            self.textEdit.clear()
            self.setCurrentFile('')
    @pyqtSlot()
    def open(self):
        if self.maybeSave():
            fileName, _ = QFileDialog.getOpenFileName(self)
            if fileName:
                self.loadFile(fileName)
    @pyqtSlot()
    def save(self):
        if self.curFile:
            return self.saveFile(self.curFile)

        return self.saveAs()
    @pyqtSlot()
    def saveAs(self):
        fileName, _ = QFileDialog.getSaveFileName(self)
        if fileName:
            return self.saveFile(fileName)

        return False
    @pyqtSlot()
    def about(self):
        QMessageBox.about(self, self.tr("About Application"),
                self.tr("The <b>Application</b> example demonstrates how to write "
                "modern GUI applications using Qt, with a menu bar, "
                "toolbars, and a status bar."))

    def readSettings(self):
        settings = QSettings("Trolltech", "Application Example")
        pos = settings.value("pos", QPoint(200, 200))
        size = settings.value("size", QSize(400, 400))
        self.resize(size)
        self.move(pos)

    def writeSettings(self):
        settings = QSettings("Trolltech", "Application Example")
        settings.setValue("pos", self.pos())
        settings.setValue("size", self.size())

    def maybeSave(self):
        if self.textEdit.document().isModified():
            ret = QMessageBox.warning(self, self.tr("Application"),
                    self.tr('''The document has been modified.
                    Do you want to save your changes?'''),
                    QMessageBox.Save | QMessageBox.Discard \
                    | QMessageBox.Cancel)

            if ret == QMessageBox.Save:
                return self.save()

            if ret == QMessageBox.Cancel:
                return False

        return True

    def loadFile(self, fileName):
        file = QFile(fileName)
        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            QMessageBox.warning(self, self.tr("Application"),
                    self.tr("Cannot read file %s:\n%s." % (fileName, file.errorString())) )
            return

        inf = QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.textEdit.setPlainText(inf.readAll())
        QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName)
        self.statusBar().showMessage("File loaded", 2000)

    def saveFile(self, fileName):
        file = QFile(fileName)
        if not file.open(QIODevice.WriteOnly | QIODevice.Text):
            QMessageBox.warning(self, "Application",
                    "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            return False

        outf = QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        outf << self.textEdit.toPlainText()
        QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName);
        self.statusBar().showMessage("File saved", 2000)
        return True

    def setCurrentFile(self, fileName):
        self.curFile = fileName
        self.textEdit.document().setModified(False)
        if self.curFile:
            shownName = self.strippedName(self.curFile)
        else:
            shownName = 'untitled.txt'
        self.setWindowTitle("%s-Application" % shownName)


    def setWindowModified(self):
        if self.curFile:
            shownName = self.strippedName(self.curFile)
        else:
            shownName = 'untitled.txt'
        self.setWindowTitle("-*-%s-Application" % shownName)

    def strippedName(self, fullFileName):
        return QFileInfo(fullFileName).fileName()

########################################
    def getaction_New(self):
        return self.mainUi.action_New
    def getaction_Cut(self):
        return self.mainUi.action_Cut
    def getaction_Copy(self):
        return self.mainUi.action_Copy
