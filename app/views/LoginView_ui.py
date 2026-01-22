# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginView.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.lblEmail = QLabel(Form)
        self.lblEmail.setObjectName(u"lblEmail")
        self.lblEmail.setGeometry(QRect(60, 110, 49, 16))
        font = QFont()
        font.setPointSize(10)
        self.lblEmail.setFont(font)
        self.lblPassword = QLabel(Form)
        self.lblPassword.setObjectName(u"lblPassword")
        self.lblPassword.setGeometry(QRect(50, 160, 81, 16))
        self.lblPassword.setFont(font)
        self.lblTitulo = QLabel(Form)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setGeometry(QRect(140, 30, 111, 16))
        font1 = QFont()
        font1.setPointSize(12)
        self.lblTitulo.setFont(font1)
        self.btnLogin = QPushButton(Form)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(150, 230, 79, 24))
        self.inputEmail = QLineEdit(Form)
        self.inputEmail.setObjectName(u"inputEmail")
        self.inputEmail.setGeometry(QRect(140, 110, 113, 22))
        self.inputPassword = QLineEdit(Form)
        self.inputPassword.setObjectName(u"inputPassword")
        self.inputPassword.setGeometry(QRect(140, 160, 113, 22))
        self.lblError = QLabel(Form)
        self.lblError.setObjectName(u"lblError")
        self.lblError.setGeometry(QRect(160, 200, 49, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblEmail.setText(QCoreApplication.translate("Form", u"E-mail:", None))
        self.lblPassword.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a:", None))
        self.lblTitulo.setText(QCoreApplication.translate("Form", u"Inicio de sesion", None))
        self.btnLogin.setText(QCoreApplication.translate("Form", u"Entrar", None))
        self.lblError.setText("")
    # retranslateUi

