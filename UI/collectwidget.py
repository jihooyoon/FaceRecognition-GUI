# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collectwidget.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(540, 416)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainForm.sizePolicy().hasHeightForWidth())
        mainForm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        mainForm.setFont(font)
        mainForm.setStyleSheet("QWidget#mainForm {\n"
"background-color: rgb(23, 23, 23)\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(mainForm)
        self.verticalLayout.setContentsMargins(0, 0, 0, 12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cameraLabel = QtWidgets.QLabel(mainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.cameraLabel.sizePolicy().hasHeightForWidth())
        self.cameraLabel.setSizePolicy(sizePolicy)
        self.cameraLabel.setStyleSheet("background: black; \n"
"color: rgb(128, 128, 128);\n"
"border-bottom: 1px solid rgb(133, 34, 140);")
        self.cameraLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cameraLabel.setObjectName("cameraLabel")
        self.verticalLayout.addWidget(self.cameraLabel)
        self.controlWidget = QtWidgets.QWidget(mainForm)
        self.controlWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.controlWidget.setObjectName("controlWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.controlWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.statusLabel = QtWidgets.QLabel(self.controlWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.statusLabel.setFont(font)
        self.statusLabel.setAutoFillBackground(False)
        self.statusLabel.setStyleSheet("QLabel {\n"
"color: rgb(128, 128, 128)\n"
"}")
        self.statusLabel.setLineWidth(0)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout_2.addWidget(self.statusLabel)
        self.startButton = QtWidgets.QPushButton(self.controlWidget)
        self.startButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QtCore.QSize(105, 0))
        self.startButton.setMaximumSize(QtCore.QSize(105, 16777215))
        self.startButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.startButton.setStyleSheet("QPushButton {\n"
"margin: 5px 0px 0px 0px;\n"
"padding-bottom: 4px;\n"
"border: 1px solid rgb(133, 34, 140);\n"
"border-top: none;\n"
"border-left: none;\n"
"border-right: none;\n"
"border-radius: 0px;\n"
"color: rgb(133, 34, 140);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(133, 34, 140, 235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: rgba(133, 34, 140, 190);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"color: rgb(92, 92, 92);\n"
"border-color: rgb(92, 92, 92);\n"
"}")
        self.startButton.setFlat(False)
        self.startButton.setObjectName("startButton")
        self.verticalLayout_2.addWidget(self.startButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.controlWidget)

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "JH Face Data Collector"))
        self.cameraLabel.setText(_translate("mainForm", "No Supported Camera"))
        self.statusLabel.setText(_translate("mainForm", "Click \"start\" to begin"))
        self.startButton.setText(_translate("mainForm", "START"))

