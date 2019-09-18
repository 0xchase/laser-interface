#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import Interface
import lasers
from lasers import *

class ExampleApp(QtWidgets.QMainWindow, Interface.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

        x = 0
        y = -1
        for laser in lasers:
            laser.label = QLabel(laser.name)
            laser.label.setText(laser.name)
            self.lasernames.addWidget(laser.label)
            y += 1
            x = 0

            for stage in laser.stages:
                stage.button = QPushButton(laser.name + stage.name)
                stage.button.setCheckable(True)
                stage.button.setText(stage.name)
                stage.button.clicked.connect(self.btnclicked)
                self.lasergrid.addWidget(stage.button, x, y)
                x += 1

        self.laser1.clicked.connect(self.btnclicked)
        self.laser2.clicked.connect(self.btnclicked)
        self.laser3.clicked.connect(self.btnclicked)
        self.laser4.clicked.connect(self.btnclicked)
        self.laser5.clicked.connect(self.btnclicked)

        self.warning.hide()

        self.freqs = []

        self.btnclicked()


    def btnclicked(self):
        self.freqs = []

        self.freqszone1 = []
        self.freqszone2 = []


        self.glasses1transparent.hide()
        self.glasses2transparent.hide()
        self.glasses3transparent.hide()
        self.glasses4transparent.hide()
        self.glasses5transparent.hide()


        self.glasses1transparent2.hide()
        self.glasses2transparent2.hide()
        self.glasses3transparent2.hide()
        self.glasses4transparent2.hide()
        self.glasses5transparent2.hide()

        self.zone1red.hide()
        self.zone2red.hide()

        if self.laser1.isChecked():
            self.freqs.append(300)
            self.glasses1transparent.show()
            self.glasses2transparent.show()
            self.glasses5transparent.show()
            self.zone1red.show()
        if self.laser2.isChecked():
            self.freqs.append(400)
            self.glasses1transparent.show()
            self.glasses3transparent.show()
            self.glasses4transparent.show()
            self.zone1red.show()
        if self.laser3.isChecked():
            self.freqs.append(500)
            self.glasses1transparent2.show()
            self.glasses2transparent2.show()
            self.glasses4transparent2.show()
            self.zone2red.show()
        if self.laser4.isChecked():
            self.glasses1transparent2.show()
            self.glasses3transparent2.show()
            self.freqs.append(600)
            self.zone2red.show()
        if self.laser5.isChecked():
            self.glasses1transparent2.show()
            self.glasses5transparent2.show()
            self.freqs.append(700)
            self.zone2red.show()

        s = ""
        for f in self.freqs:
            s += str(f) + " nm<br>"
        self.freqlist.setText("<html><head/><body><p><span style=\" color:#b0b7c1;\">" + str(s) + "</span></p></body></html>")

        self.warning.hide()

        if (self.glasses1transparent.isVisible() and
            self.glasses2transparent.isVisible() and
            self.glasses3transparent.isVisible() and
            self.glasses4transparent.isVisible() and
            self.glasses5transparent.isVisible()):
            #print("Warning")
            self.warning.show()

        if (self.glasses1transparent2.isVisible() and
            self.glasses2transparent2.isVisible() and
            self.glasses3transparent2.isVisible() and
            self.glasses4transparent2.isVisible() and
            self.glasses5transparent2.isVisible()):
            #print("Warning")
            self.warning.show()


def main():
    app = QApplication(sys.argv)
    form = ExampleApp()

    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
