# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Simple.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1364, 1028)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-10, -20, 1511, 1171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background.sizePolicy().hasHeightForWidth())
        self.background.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        self.background.setFont(font)
        self.background.setAutoFillBackground(False)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("images/gui1background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.element2 = QtWidgets.QLabel(self.centralwidget)
        self.element2.setGeometry(QtCore.QRect(49, 268, 601, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.element2.sizePolicy().hasHeightForWidth())
        self.element2.setSizePolicy(sizePolicy)
        self.element2.setAutoFillBackground(False)
        self.element2.setFrameShape(QtWidgets.QFrame.Box)
        self.element2.setText("")
        self.element2.setPixmap(QtGui.QPixmap("images/gui1element1.png"))
        self.element2.setScaledContents(True)
        self.element2.setObjectName("element2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(49, 278, 601, 102))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.glasses1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glasses1.sizePolicy().hasHeightForWidth())
        self.glasses1.setSizePolicy(sizePolicy)
        self.glasses1.setMaximumSize(QtCore.QSize(100, 100))
        self.glasses1.setText("")
        self.glasses1.setPixmap(QtGui.QPixmap("images/checkgreen2.png"))
        self.glasses1.setScaledContents(True)
        self.glasses1.setObjectName("glasses1")
        self.horizontalLayout.addWidget(self.glasses1)
        self.glasses2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glasses2.sizePolicy().hasHeightForWidth())
        self.glasses2.setSizePolicy(sizePolicy)
        self.glasses2.setMaximumSize(QtCore.QSize(100, 100))
        self.glasses2.setText("")
        self.glasses2.setPixmap(QtGui.QPixmap("images/checkgreen2.png"))
        self.glasses2.setScaledContents(True)
        self.glasses2.setObjectName("glasses2")
        self.horizontalLayout.addWidget(self.glasses2)
        self.glasses3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glasses3.sizePolicy().hasHeightForWidth())
        self.glasses3.setSizePolicy(sizePolicy)
        self.glasses3.setMaximumSize(QtCore.QSize(100, 100))
        self.glasses3.setText("")
        self.glasses3.setPixmap(QtGui.QPixmap("images/checkgreen2.png"))
        self.glasses3.setScaledContents(True)
        self.glasses3.setObjectName("glasses3")
        self.horizontalLayout.addWidget(self.glasses3)
        self.glasses4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glasses4.sizePolicy().hasHeightForWidth())
        self.glasses4.setSizePolicy(sizePolicy)
        self.glasses4.setMaximumSize(QtCore.QSize(100, 100))
        self.glasses4.setText("")
        self.glasses4.setPixmap(QtGui.QPixmap("images/checkgreen2.png"))
        self.glasses4.setScaledContents(True)
        self.glasses4.setObjectName("glasses4")
        self.horizontalLayout.addWidget(self.glasses4)
        self.glasses5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glasses5.sizePolicy().hasHeightForWidth())
        self.glasses5.setSizePolicy(sizePolicy)
        self.glasses5.setMaximumSize(QtCore.QSize(100, 100))
        self.glasses5.setText("")
        self.glasses5.setPixmap(QtGui.QPixmap("images/checkgreen2.png"))
        self.glasses5.setScaledContents(True)
        self.glasses5.setObjectName("glasses5")
        self.horizontalLayout.addWidget(self.glasses5)
        self.element2_2 = QtWidgets.QLabel(self.centralwidget)
        self.element2_2.setGeometry(QtCore.QRect(670, 150, 171, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.element2_2.sizePolicy().hasHeightForWidth())
        self.element2_2.setSizePolicy(sizePolicy)
        self.element2_2.setAutoFillBackground(False)
        self.element2_2.setFrameShape(QtWidgets.QFrame.Box)
        self.element2_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.element2_2.setText("")
        self.element2_2.setPixmap(QtGui.QPixmap("images/gui1element1.png"))
        self.element2_2.setScaledContents(True)
        self.element2_2.setObjectName("element2_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(690, 150, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(900, 50, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.element3_3 = QtWidgets.QLabel(self.centralwidget)
        self.element3_3.setGeometry(QtCore.QRect(880, 40, 471, 941))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.element3_3.sizePolicy().hasHeightForWidth())
        self.element3_3.setSizePolicy(sizePolicy)
        self.element3_3.setAutoFillBackground(False)
        self.element3_3.setFrameShape(QtWidgets.QFrame.Box)
        self.element3_3.setText("")
        self.element3_3.setPixmap(QtGui.QPixmap("images/gui1element6.png"))
        self.element3_3.setScaledContents(True)
        self.element3_3.setObjectName("element3_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 550, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(49, 686, 601, 102))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.glasses1_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glasses1_2.sizePolicy().hasHeightForWidth())
        self.glasses1_2.setSizePolicy(sizePolicy)
        self.glasses1_2.setMaximumSize(QtCore.QSize(100, 100))
        self.glasses1_2.setText("")
        self.glasses1_2.setPixmap(QtGui.QPixmap("images/checkgreen2.png"))
        self.glasses1_2.setScaledContents(True)
        self.glasses1_2.setObjectName("glasses1_2")
        self.horizontalLayout_2.addWidget(self.glasses1_2)
        self.glasses2_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glasses2_2.sizePolicy().hasHeightForWidth())
        self.glasses2_2.setSizePolicy(sizePolicy)
        self.glasses2_2.setMaximumSize(QtCore.QSize(100, 100))
        self.glasses2_2.setText("")
        self.glasses2_2.setPixmap(QtGui.QPixmap("images/checkgreen2.png"))
        self.glasses2_2.setScaledContents(True)
        self.glasses2_2.setObjectName("glasses2_2")
        self.horizontalLayout_2.addWidget(self.glasses2_2)
        self.glasses3_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glasses3_2.sizePolicy().hasHeightForWidth())
        self.glasses3_2.setSizePolicy(sizePolicy)
        self.glasses3_2.setMaximumSize(QtCore.QSize(100, 100))
        self.glasses3_2.setText("")
        self.glasses3_2.setPixmap(QtGui.QPixmap("images/checkgreen2.png"))
        self.glasses3_2.setScaledContents(True)
        self.glasses3_2.setObjectName("glasses3_2")
        self.horizontalLayout_2.addWidget(self.glasses3_2)
        self.glasses4_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glasses4_2.sizePolicy().hasHeightForWidth())
        self.glasses4_2.setSizePolicy(sizePolicy)
        self.glasses4_2.setMaximumSize(QtCore.QSize(100, 100))
        self.glasses4_2.setText("")
        self.glasses4_2.setPixmap(QtGui.QPixmap("images/checkgreen2.png"))
        self.glasses4_2.setScaledContents(True)
        self.glasses4_2.setObjectName("glasses4_2")
        self.horizontalLayout_2.addWidget(self.glasses4_2)
        self.glasses5_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glasses5_2.sizePolicy().hasHeightForWidth())
        self.glasses5_2.setSizePolicy(sizePolicy)
        self.glasses5_2.setMaximumSize(QtCore.QSize(100, 100))
        self.glasses5_2.setText("")
        self.glasses5_2.setPixmap(QtGui.QPixmap("images/checkgreen2.png"))
        self.glasses5_2.setScaledContents(True)
        self.glasses5_2.setObjectName("glasses5_2")
        self.horizontalLayout_2.addWidget(self.glasses5_2)
        self.element2_3 = QtWidgets.QLabel(self.centralwidget)
        self.element2_3.setGeometry(QtCore.QRect(49, 676, 601, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.element2_3.sizePolicy().hasHeightForWidth())
        self.element2_3.setSizePolicy(sizePolicy)
        self.element2_3.setAutoFillBackground(False)
        self.element2_3.setFrameShape(QtWidgets.QFrame.Box)
        self.element2_3.setText("")
        self.element2_3.setPixmap(QtGui.QPixmap("images/gui1element1.png"))
        self.element2_3.setScaledContents(True)
        self.element2_3.setObjectName("element2_3")
        self.freqlistl = QtWidgets.QLabel(self.centralwidget)
        self.freqlistl.setGeometry(QtCore.QRect(690, 200, 131, 201))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(12)
        self.freqlistl.setFont(font)
        self.freqlistl.setScaledContents(False)
        self.freqlistl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.freqlistl.setObjectName("freqlistl")
        self.warning_2 = QtWidgets.QLabel(self.centralwidget)
        self.warning_2.setGeometry(QtCore.QRect(880, 90, 491, 871))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warning_2.sizePolicy().hasHeightForWidth())
        self.warning_2.setSizePolicy(sizePolicy)
        self.warning_2.setMinimumSize(QtCore.QSize(0, 0))
        self.warning_2.setMaximumSize(QtCore.QSize(500, 1000))
        self.warning_2.setText("")
        self.warning_2.setPixmap(QtGui.QPixmap("images/map5_rotated.png"))
        self.warning_2.setScaledContents(True)
        self.warning_2.setObjectName("warning_2")
        self.element2_4 = QtWidgets.QLabel(self.centralwidget)
        self.element2_4.setGeometry(QtCore.QRect(48, 209, 601, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.element2_4.sizePolicy().hasHeightForWidth())
        self.element2_4.setSizePolicy(sizePolicy)
        self.element2_4.setAutoFillBackground(False)
        self.element2_4.setFrameShape(QtWidgets.QFrame.Box)
        self.element2_4.setText("")
        self.element2_4.setPixmap(QtGui.QPixmap("images/gui1element1.png"))
        self.element2_4.setScaledContents(True)
        self.element2_4.setObjectName("element2_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(53, 210, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(169, 210, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(287, 210, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(406, 210, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(520, 210, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.zonebred = QtWidgets.QLabel(self.centralwidget)
        self.zonebred.setGeometry(QtCore.QRect(880, 90, 491, 871))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zonebred.sizePolicy().hasHeightForWidth())
        self.zonebred.setSizePolicy(sizePolicy)
        self.zonebred.setMinimumSize(QtCore.QSize(0, 0))
        self.zonebred.setMaximumSize(QtCore.QSize(500, 1000))
        self.zonebred.setText("")
        self.zonebred.setPixmap(QtGui.QPixmap("images/zone2red2_rotated.png"))
        self.zonebred.setScaledContents(True)
        self.zonebred.setObjectName("zonebred")
        self.zonelred = QtWidgets.QLabel(self.centralwidget)
        self.zonelred.setGeometry(QtCore.QRect(880, 90, 491, 871))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zonelred.sizePolicy().hasHeightForWidth())
        self.zonelred.setSizePolicy(sizePolicy)
        self.zonelred.setMinimumSize(QtCore.QSize(0, 0))
        self.zonelred.setMaximumSize(QtCore.QSize(500, 1000))
        self.zonelred.setText("")
        self.zonelred.setPixmap(QtGui.QPixmap("images/zone1red2_rotated.png"))
        self.zonelred.setScaledContents(True)
        self.zonelred.setObjectName("zonelred")
        self.element2_5 = QtWidgets.QLabel(self.centralwidget)
        self.element2_5.setGeometry(QtCore.QRect(670, 560, 171, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.element2_5.sizePolicy().hasHeightForWidth())
        self.element2_5.setSizePolicy(sizePolicy)
        self.element2_5.setAutoFillBackground(False)
        self.element2_5.setFrameShape(QtWidgets.QFrame.Box)
        self.element2_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.element2_5.setText("")
        self.element2_5.setPixmap(QtGui.QPixmap("images/gui1element1.png"))
        self.element2_5.setScaledContents(True)
        self.element2_5.setObjectName("element2_5")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(687, 560, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.freqlistb = QtWidgets.QLabel(self.centralwidget)
        self.freqlistb.setGeometry(QtCore.QRect(690, 610, 131, 201))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(12)
        self.freqlistb.setFont(font)
        self.freqlistb.setScaledContents(False)
        self.freqlistb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.freqlistb.setObjectName("freqlistb")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(970, 650, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(24)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1200, 590, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(24)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.element2_6 = QtWidgets.QLabel(self.centralwidget)
        self.element2_6.setGeometry(QtCore.QRect(49, 619, 601, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.element2_6.sizePolicy().hasHeightForWidth())
        self.element2_6.setSizePolicy(sizePolicy)
        self.element2_6.setAutoFillBackground(False)
        self.element2_6.setFrameShape(QtWidgets.QFrame.Box)
        self.element2_6.setText("")
        self.element2_6.setPixmap(QtGui.QPixmap("images/gui1element1.png"))
        self.element2_6.setScaledContents(True)
        self.element2_6.setObjectName("element2_6")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(288, 620, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(521, 620, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(407, 620, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(54, 620, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(170, 620, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.element2_7 = QtWidgets.QLabel(self.centralwidget)
        self.element2_7.setGeometry(QtCore.QRect(20, 130, 841, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.element2_7.sizePolicy().hasHeightForWidth())
        self.element2_7.setSizePolicy(sizePolicy)
        self.element2_7.setAutoFillBackground(False)
        self.element2_7.setFrameShape(QtWidgets.QFrame.Box)
        self.element2_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.element2_7.setText("")
        self.element2_7.setPixmap(QtGui.QPixmap("images/gui1element6.png"))
        self.element2_7.setScaledContents(True)
        self.element2_7.setObjectName("element2_7")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(40, 140, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(24)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.element2_8 = QtWidgets.QLabel(self.centralwidget)
        self.element2_8.setGeometry(QtCore.QRect(20, 540, 841, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.element2_8.sizePolicy().hasHeightForWidth())
        self.element2_8.setSizePolicy(sizePolicy)
        self.element2_8.setAutoFillBackground(False)
        self.element2_8.setFrameShape(QtWidgets.QFrame.Box)
        self.element2_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.element2_8.setText("")
        self.element2_8.setPixmap(QtGui.QPixmap("images/gui1element6.png"))
        self.element2_8.setScaledContents(True)
        self.element2_8.setObjectName("element2_8")
        self.warning = QtWidgets.QLabel(self.centralwidget)
        self.warning.setGeometry(QtCore.QRect(720, 230, 500, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warning.sizePolicy().hasHeightForWidth())
        self.warning.setSizePolicy(sizePolicy)
        self.warning.setMinimumSize(QtCore.QSize(500, 500))
        self.warning.setMaximumSize(QtCore.QSize(500, 500))
        self.warning.setText("")
        self.warning.setPixmap(QtGui.QPixmap("images/exclamation.png"))
        self.warning.setScaledContents(True)
        self.warning.setObjectName("warning")
        self.background.raise_()
        self.element2_7.raise_()
        self.element2_8.raise_()
        self.element2_3.raise_()
        self.element2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.element2_2.raise_()
        self.label_4.raise_()
        self.element3_3.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.freqlistl.raise_()
        self.warning_2.raise_()
        self.element2_4.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.zonebred.raise_()
        self.zonelred.raise_()
        self.element2_5.raise_()
        self.label_16.raise_()
        self.freqlistb.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.element2_6.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_17.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_23.raise_()
        self.warning.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#b0b7c1;\">Wavelengths</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"color:#b0b7c1;\">MAP</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#b0b7c1;\">Laser Containment Area 2</span></p></body></html>"))
        self.freqlistl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#b0b7c1;\">Zone 1</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"color:#b0b7c1;\">None</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"color:#b0b7c1;\">LG6</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"color:#b0b7c1;\">LG1</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"color:#b0b7c1;\">LG7</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"color:#b0b7c1;\">LG12</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#b0b7c1;\">Wavelengths</span></p></body></html>"))
        self.freqlistb.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#b0b7c1;\">Zone 1</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "LCA 1"))
        self.label_19.setText(_translate("MainWindow", "LCA 2"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"color:#b0b7c1;\">LG1</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"color:#b0b7c1;\">LG12</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"color:#b0b7c1;\">LG7</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"color:#b0b7c1;\">None</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\"color:#b0b7c1;\">LG6</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#b0b7c1;\">Laser Containment Area 1</span></p></body></html>"))
