#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import Interface
import Simple
import lasers
from lasers import *

class ExampleApp(QtWidgets.QMainWindow, Interface.Ui_MainWindow):
    def __init__(self, simpleForm, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.simpleForm = simpleForm


        icon = QtGui.QIcon("images/boxgreen.png")

        icon2 = QtGui.QIcon("")
        icon2.addPixmap(QtGui.QPixmap("images/unchecked2.png"))
        icon2.addPixmap(QtGui.QPixmap("images/unchecked2.png"), QtGui.QIcon.Disabled)
        icon2.addPixmap(QtGui.QPixmap("images/unchecked2.png"), QtGui.QIcon.Active)
        icon2.addPixmap(QtGui.QPixmap("images/checked2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)

        x = 0
        y = -1
        for laser in lasers:
            laser.label = QLabel(laser.name)
            laser.label.setText("<html><head/><body><p><span style=\"color:#b0b7c1;\">" + laser.name + "</span></p></body></html>")

            laser.desc = QLabel(laser.description)
            laser.desc.setText("<html><head/><body><p><span style=\"color:#b0b7c1;\">" + laser.description + "</span></p></body></html>")

            self.lasernames.addWidget(laser.label)
            self.descriptions.addWidget(laser.desc)

            laser.button = QPushButton(laser.name + "_onoff")
            laser.button.setText("")
            laser.button.setGeometry(200, 200, 200, 200)
            laser.button.clicked.connect(self.btnclicked)
            laser.button.setIconSize(QtCore.QSize(35, 35))
            laser.button.setCheckable(True)
            laser.button.setFlat(True)
            laser.button.setIcon(icon2)
            laser.button.setStyleSheet("background-color: rgb(50, 56, 69)")

            self.laseronoff.addWidget(laser.button)

            y += 1
            x = 0

            for stage in laser.stages:
                #stage.button = QPushButton(laser.name + stage.name + "_stage")
                stage.button = Button(laser.name + stage.name + "_stage")
                stage.button.setText("")
                stage.button.flat = True
                stage.button.setCheckable(False)
                stage.button.setFlat(True)
                stage.button.setIcon(icon)
                stage.button.setStyleSheet("background-color: rgb(50, 56, 69)")

                #stage.button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                stage.button.setGeometry(200, 200, 200, 200)
                stage.button.clicked.connect(self.btnclicked)
                stage.button.setIconSize(QtCore.QSize(35, 35))

                stage.button.hoverConnect(self.btnHovered)

                self.lasergrid.addWidget(stage.button, y, x)
                x += 1

        self.simpleForm.warning.hide()

        self.freqs = []

        #self.showFullScreen()

        self.btnclicked()


    def btnclicked(self):
        try:
            button = self.sender()
            #print("Clicked: " + str(button))
            button.nextState()

        except Exception as e:
            print(e)


        self.freqszone1 = []
        self.freqszone2 = []

        self.simpleForm.glasses1transparent.hide()
        self.simpleForm.glasses2transparent.hide()
        self.simpleForm.glasses3transparent.hide()
        self.simpleForm.glasses4transparent.hide()
        self.simpleForm.glasses5transparent.hide()


        self.simpleForm.glasses1transparent2.hide()
        self.simpleForm.glasses2transparent2.hide()
        self.simpleForm.glasses3transparent2.hide()
        self.simpleForm.glasses4transparent2.hide()
        self.simpleForm.glasses5transparent2.hide()

        self.simpleForm.zonelred.hide()
        self.simpleForm.zonebred.hide()

        wavelengthsL = []
        wavelengthsB = []

        for laser in lasers:
            if laser.button.isChecked():
                for stage in laser.stages:
                    if not stage.button.getState() == 0:
                        if stage.lca == "Zone L":
                            wavelengthsL.append(stage.wavelength)
                        if stage.lca == "Zone B":
                            wavelengthsB.append(stage.wavelength)

        sl = ""
        sb = ""
        for w in wavelengthsB:
            sb += str(w) + " nm<br>"
        for w in wavelengthsL:
            sl += str(w) + " nm<br>"
        self.simpleForm.freqlistl.setText("<html><head/><body><p><span style=\" color:#b0b7c1;\">" + str(sl) + "</span></p></body></html>")
        self.simpleForm.freqlistb.setText("<html><head/><body><p><span style=\" color:#b0b7c1;\">" + str(sb) + "</span></p></body></html>")

        self.warning.hide()

        if len(wavelengthsL) > 0:
            self.simpleForm.glasses1transparent.show()
            self.simpleForm.zonelred.show()

        for w in wavelengthsL:
            if not (190 <= w <= 398 or 9000 <= w <= 11000):
                self.simpleForm.glasses2transparent.show()
            if not (190 <= w <= 400 or 808 <= w <= 840 or 840 <= w <= 950 or 950 <= w <= 1080 or 1080 <= w <= 1090):
                self.simpleForm.glasses3transparent.show()
            if not (190 <= w <= 400 or 651 <= w <= 670 or 671 <= w <= 715 or 680 <= w <= 710 or 690 <= w <= 700):
                self.simpleForm.glasses4transparent.show()
            if not (180 <= w <= 534 or 720 <= w <= 730 or 730 <= w <= 740 or 740 <= w <= 1070):
                self.simpleForm.glasses5transparent.show()

        if len(wavelengthsB) > 0:
            self.simpleForm.glasses1transparent2.show()
            self.simpleForm.zonebred.show()

        for w in wavelengthsB:
            if not (190 <= w <= 398 or 9000 <= w <= 11000):
                self.simpleForm.glasses2transparent2.show()
            if not (190 <= w <= 400 or 808 <= w <= 840 or 840 <= w <= 950 or 950 <= w <= 1080 or 1080 <= w <= 1090):
                self.simpleForm.glasses3transparent2.show()
            if not (190 <= w <= 400 or 651 <= w <= 670 or 671 <= w <= 715 or 680 <= w <= 710 or 690 <= w <= 700):
                self.simpleForm.glasses4transparent2.show()
            if not (180 <= w <= 534 or 720 <= w <= 730 or 730 <= w <= 740 or 740 <= w <= 1070):
                self.simpleForm.glasses5transparent2.show()

        if (self.simpleForm.glasses1transparent.isVisible() and
            self.simpleForm.glasses2transparent.isVisible() and
            self.simpleForm.glasses3transparent.isVisible() and
            self.simpleForm.glasses4transparent.isVisible() and
            self.simpleForm.glasses5transparent.isVisible()):
            self.simpleForm.warning.show()

        if (self.simpleForm.glasses1transparent2.isVisible() and
            self.simpleForm.glasses2transparent2.isVisible() and
            self.simpleForm.glasses3transparent2.isVisible() and
            self.simpleForm.glasses4transparent2.isVisible() and
            self.simpleForm.glasses5transparent2.isVisible()):
            self.simpleForm.warning.show()

    def btnHovered(self):
        try:
            self.zoneinfo.setText("<html><head/><body><p><span style=\" color:#b0b7c1;\">" + "</span></p></body></html>")
            for laser in lasers:
                for stage in laser.stages:
                    if stage.button.isHovered():
                        #print("Hovered: " + stage.name)
                        self.zoneinfo.setText("<html><head/><body><p><span style=\" color:#b0b7c1;\">" + "Name: " + str(stage.name) + ", Maker: " + str(stage.maker) + ", Model: " + str(stage.model) + "</span></p></body></html>")
        except:
            print("Hover failed")

class Button(QPushButton):

    def __init__(self, parent=None):
        super(Button, self).__init__(parent)
        self.setIcon(QtGui.QIcon("images/unchecked2.png"))
        self.state = 0
        self.hover = False

    def hoverConnect(self, hoverFunc):
        self.hoverFunc = hoverFunc

    def enterEvent(self, QEvent):
        self.hover = True
        self.hoverFunc()

    def leaveEvent(self, QEvent):
        self.hover = False
        self.hoverFunc()

    def isHovered(self):
        return self.hover

    def getState(self):
        return self.state

    def nextState(self):
        if self.state == 0:
            self.setIcon(QtGui.QIcon("images/boxyellow.png"))
            self.state += 1
        elif self.state == 1:
            self.setIcon(QtGui.QIcon("images/boxred.png"))
            self.state = 2
        elif self.state == 2:
            self.setIcon(QtGui.QIcon("images/boxgreen.png"))
            self.state = 0

class ExampleApp2(QtWidgets.QMainWindow, Simple.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp2, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    form2 = ExampleApp2()
    form1 = ExampleApp(form2)

    form1.show()
    form2.show()
    app.exec_()

if __name__ == '__main__':
    main()
