#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import Interface

class ExampleApp(QtWidgets.QMainWindow, Interface.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

        self.laser1.clicked.connect(self.btnclicked)
        self.laser2.clicked.connect(self.btnclicked)
        self.laser3.clicked.connect(self.btnclicked)
        self.laser4.clicked.connect(self.btnclicked)
        self.laser5.clicked.connect(self.btnclicked)

        self.warning.hide()

        self.freqs = []

        self.btnclicked()
        self.parse()

    def btnclicked(self):
        self.freqs = []

        self.glasses1transparent.hide()
        self.glasses2transparent.hide()
        self.glasses3transparent.hide()
        self.glasses4transparent.hide()
        self.glasses5transparent.hide()

        if self.laser1.isChecked():
            self.freqs.append(300)
            self.glasses1transparent.show()
            self.glasses2transparent.show()
            self.glasses5transparent.show()
        if self.laser2.isChecked():
            self.freqs.append(400)
            self.glasses2transparent.show()
            self.glasses4transparent.show()
        if self.laser3.isChecked():
            self.freqs.append(500)
            self.glasses3transparent.show()
        if self.laser4.isChecked():
            self.freqs.append(600)
            self.glasses4transparent.show()
        if self.laser5.isChecked():
            self.freqs.append(700)
            self.glasses5transparent.show()

        s = ""
        for f in self.freqs:
            s += str(f) + " nm<br>"
        self.freqlist.setText("<html><head/><body><p><span style=\" color:#b0b7c1;\">" + str(s) + "</span></p></body></html>")

        if (self.glasses1transparent.isVisible() and
            self.glasses2transparent.isVisible() and
            self.glasses3transparent.isVisible() and
            self.glasses4transparent.isVisible() and
            self.glasses5transparent.isVisible()):
            print("Warning")
            self.warning.show()
        else:
            self.warning.hide()

    def parse(self):
        print("Parsing files...")

        text = ""
        with open("data/glasses.txt", "r") as f:
            text = f.read()

        lines = text.split("\n")

        print("Glasses:")
        for line in lines:
            print(line)

        with open("data/lasers.txt", "r") as f:
            text = f.read()

        lines = text.split("\n")

        print("Lasers:")
        for line in lines:
            print(line)




def main():
    app = QApplication(sys.argv)
    form = ExampleApp()

    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
