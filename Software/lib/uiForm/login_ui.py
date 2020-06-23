# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'development/Form/login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(1000, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login.sizePolicy().hasHeightForWidth())
        login.setSizePolicy(sizePolicy)
        login.setMinimumSize(QtCore.QSize(1000, 700))
        self.back_layout = QtWidgets.QVBoxLayout(login)
        self.back_layout.setContentsMargins(0, 0, 0, 0)
        self.back_layout.setSpacing(0)
        self.back_layout.setObjectName("back_layout")
        self.back_frame = QtWidgets.QFrame(login)
        self.back_frame.setObjectName("back_frame")
        self.layoutback_frame = QtWidgets.QVBoxLayout(self.back_frame)
        self.layoutback_frame.setContentsMargins(1, 1, -1, -1)
        self.layoutback_frame.setObjectName("layoutback_frame")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutback_frame.addItem(spacerItem)
        self.horizontalFrame = QtWidgets.QFrame(self.back_frame)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.center_login = QtWidgets.QFrame(self.horizontalFrame)
        self.center_login.setObjectName("center_login")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.center_login)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalFrame_2 = QtWidgets.QFrame(self.center_login)
        self.verticalFrame_2.setMinimumSize(QtCore.QSize(0, 100))
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_3.setContentsMargins(-1, 1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalFrame_2)
        self.label.setStyleSheet("image: url(:/icons svg/icons/svg/fullaxis.svg);")
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalFrame_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.verticalFrame_2)
        self.input_user = QtWidgets.QLineEdit(self.center_login)
        self.input_user.setText("")
        self.input_user.setObjectName("input_user")
        self.verticalLayout_2.addWidget(self.input_user)
        self.input_pass = QtWidgets.QLineEdit(self.center_login)
        self.input_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_pass.setObjectName("input_pass")
        self.verticalLayout_2.addWidget(self.input_pass)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_requestlogin = QtWidgets.QPushButton(self.center_login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_requestlogin.sizePolicy().hasHeightForWidth())
        self.btn_requestlogin.setSizePolicy(sizePolicy)
        self.btn_requestlogin.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_requestlogin.setStyleSheet("QPushButton {\n"
" Text-align:center;\n"
" border: none;\n"
" color:rgb(238, 238, 236);\n"
"background-color: rgb(55, 144, 152);\n"
"}\n"
" QPushButton:hover {\n"
" background-color: rgb(0, 98, 106);\n"
"}\n"
"QPushButton:pressed {\n"
" text-decoration: underline;}")
        self.btn_requestlogin.setObjectName("btn_requestlogin")
        self.horizontalLayout.addWidget(self.btn_requestlogin)
        self.btn_cancel = QtWidgets.QPushButton(self.center_login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        self.btn_cancel.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_cancel.setStyleSheet("QPushButton {\n"
" Text-align:center;\n"
" border: none;\n"
" color:rgb(238, 238, 236);\n"
"background-color: rgb(204, 0, 0);\n"
"}\n"
" QPushButton:hover {\n"
" background-color: rgb(164, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
" text-decoration: underline;}")
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.center_login)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-position: center;\n"
"border: none;\n"
"color:rgb(52, 101, 164)\n"
"}\n"
"QPushButton:hover {\n"
"color:rgb(114, 159, 207)\n"
"}\n"
"QPushButton:pressed {\n"
"}")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 10)
        self.verticalLayout_2.setStretch(3, 10)
        self.verticalLayout_2.setStretch(4, 10)
        self.horizontalLayout_2.addWidget(self.center_login)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.layoutback_frame.addWidget(self.horizontalFrame)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutback_frame.addItem(spacerItem3)
        self.back_layout.addWidget(self.back_frame)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.label_2.setText(_translate("login", "FullAxis"))
        self.input_user.setPlaceholderText(_translate("login", "Identificación"))
        self.input_pass.setPlaceholderText(_translate("login", "Contraseña"))
        self.btn_requestlogin.setText(_translate("login", "Ingresar"))
        self.btn_cancel.setText(_translate("login", "Cancelar"))
        self.pushButton.setText(_translate("login", "Cambiar configuración"))

from resource import resource_rc