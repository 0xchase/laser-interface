#!/usr/bin/python3

from PyQt5.QtWidgets import *
import sys

global layout
global w

def main():
    initializeWindow()

def initializeWindow():
    global layout
    global w

    app = QApplication([])
    w = QWidget()
    layout = QVBoxLayout()
    w.resize(800, 500)
    w.setWindowTitle("Window Title")

    addLabel("Title")
    btn = addButton("Click Me", 100, 100, messageBox)
    btn.clicked.connect(messageBox)
    addCheck("Check box 1")

    w.setLayout(layout)
    w.show()
    app.exec_()

def messageBox():
    mbox = QMessageBox()
    mbox.setText("This is some title stuff")
    mbox.setDetailedText("This is some more detailed message stuff")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    mbox.exec_()

def addLabel(text):
    global w
    layout.addWidget(QLabel(text))

def addCheck(text):
    global w
    check = QCheckBox(w)
    check.move(30, 30)
    check.show()

def addButton(text, x, y, function):
    global w
    btn = QPushButton(w)
    btn.setText(text)
    btn.move(x, y)
    btn.show()
    return btn

main()
