#!/usr/bin/env python3
#-*-coding:utf-8-*-

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton,QLineEdit, QMessageBox

class Form(QWidget):
    def __init__(self):
        super().__init__()
        nameLabel = QLabel("Name:")
        self.nameLine = QLineEdit()
        self.submitButton = QPushButton("Submit")
        bodyLayout = QVBoxLayout()
        bodyLayout.addWidget(nameLabel)
        bodyLayout.addWidget(self.nameLine)
        bodyLayout.addWidget(self.submitButton)

        self.submitButton.clicked.connect(self.submit)

        self.setLayout(bodyLayout)
        self.setWindowTitle("Hello Qt")
        self.show()

    def submit(self):
        name = self.nameLine.text()

        if name == "":
            QMessageBox.information(self, "Empty Field",
                                    "Please enter a name.")
            return
        else:
            QMessageBox.information(self, "Success!",
                                    "Hello %s!" % name)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = Form()
    sys.exit(app.exec_())
