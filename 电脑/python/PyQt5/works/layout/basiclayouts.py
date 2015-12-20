#!/usr/bin/env python

from PyQt5.QtWidgets import (QApplication, QDialog,QDialogButtonBox, QFormLayout, QGroupBox,QLabel, QLineEdit, QSpinBox,QVBoxLayout,QTextEdit)


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.createFormGroupBox()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("user info")

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("your infomation")
        layout = QFormLayout()
        layout.addRow(QLabel("name:"), QLineEdit())
        layout.addRow("age:", QSpinBox())
        layout.addRow(QLabel("other infomation:"), QTextEdit())
        self.formGroupBox.setLayout(layout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
