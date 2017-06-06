# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/mainwidget.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.setWindowModality(QtCore.Qt.NonModal)
        mainForm.resize(672, 320)
        self.horizontalLayout = QtWidgets.QHBoxLayout(mainForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cameraLabel = QtWidgets.QLabel(mainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameraLabel.sizePolicy().hasHeightForWidth())
        self.cameraLabel.setSizePolicy(sizePolicy)
        self.cameraLabel.setStyleSheet("background: black; color: rgb(128, 128, 128)")
        self.cameraLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cameraLabel.setObjectName("cameraLabel")
        self.horizontalLayout.addWidget(self.cameraLabel)
        self.controlWidget = QtWidgets.QWidget(mainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlWidget.sizePolicy().hasHeightForWidth())
        self.controlWidget.setSizePolicy(sizePolicy)
        self.controlWidget.setObjectName("controlWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.controlWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addDataWidget = QtWidgets.QWidget(self.controlWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.addDataWidget.sizePolicy().hasHeightForWidth())
        self.addDataWidget.setSizePolicy(sizePolicy)
        self.addDataWidget.setObjectName("addDataWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.addDataWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.capturedLabel = QtWidgets.QLabel(self.addDataWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.capturedLabel.sizePolicy().hasHeightForWidth())
        self.capturedLabel.setSizePolicy(sizePolicy)
        self.capturedLabel.setStyleSheet("background: rgb(128, 128, 128); padding: 5")
        self.capturedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.capturedLabel.setWordWrap(True)
        self.capturedLabel.setObjectName("capturedLabel")
        self.verticalLayout_2.addWidget(self.capturedLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.addDataWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLineEdit.sizePolicy().hasHeightForWidth())
        self.nameLineEdit.setSizePolicy(sizePolicy)
        self.nameLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.nameLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLineEdit.setDragEnabled(True)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.verticalLayout_2.addWidget(self.nameLineEdit)
        self.addDataButton = QtWidgets.QPushButton(self.addDataWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addDataButton.sizePolicy().hasHeightForWidth())
        self.addDataButton.setSizePolicy(sizePolicy)
        self.addDataButton.setObjectName("addDataButton")
        self.verticalLayout_2.addWidget(self.addDataButton)
        self.statusLabel = QtWidgets.QLabel(self.addDataWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel.setFont(font)
        self.statusLabel.setAutoFillBackground(False)
        self.statusLabel.setStyleSheet("color: rgb(128, 128, 128)")
        self.statusLabel.setLineWidth(0)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout_2.addWidget(self.statusLabel)
        self.verticalLayout.addWidget(self.addDataWidget)
        self.line = QtWidgets.QFrame(self.controlWidget)
        self.line.setStyleSheet("")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.recognizeWidget = QtWidgets.QWidget(self.controlWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.recognizeWidget.sizePolicy().hasHeightForWidth())
        self.recognizeWidget.setSizePolicy(sizePolicy)
        self.recognizeWidget.setObjectName("recognizeWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.recognizeWidget)
        self.verticalLayout_3.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.trainButton = QtWidgets.QPushButton(self.recognizeWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainButton.sizePolicy().hasHeightForWidth())
        self.trainButton.setSizePolicy(sizePolicy)
        self.trainButton.setObjectName("trainButton")
        self.verticalLayout_3.addWidget(self.trainButton)
        self.recognizeButton = QtWidgets.QPushButton(self.recognizeWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.recognizeButton.sizePolicy().hasHeightForWidth())
        self.recognizeButton.setSizePolicy(sizePolicy)
        self.recognizeButton.setStyleSheet("")
        self.recognizeButton.setObjectName("recognizeButton")
        self.verticalLayout_3.addWidget(self.recognizeButton)
        self.verticalLayout.addWidget(self.recognizeWidget)
        self.horizontalLayout.addWidget(self.controlWidget)

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "JH Face"))
        self.cameraLabel.setText(_translate("mainForm", "No Supported Camera"))
        self.capturedLabel.setText(_translate("mainForm", "Enter name then click \"Add Training Image\" button to capture and add image to training data"))
        self.nameLineEdit.setPlaceholderText(_translate("mainForm", "Name"))
        self.addDataButton.setText(_translate("mainForm", "Add Training Image"))
        self.statusLabel.setText(_translate("mainForm", "No Image Added"))
        self.trainButton.setText(_translate("mainForm", "Train"))
        self.recognizeButton.setText(_translate("mainForm", "RECOGNIZE"))
