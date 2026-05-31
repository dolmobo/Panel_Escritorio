# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginView.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_LoginView(object):
    def setupUi(self, LoginView):
        if not LoginView.objectName():
            LoginView.setObjectName(u"LoginView")
        LoginView.resize(450, 320)
        LoginView.setMinimumSize(QSize(450, 320))
        LoginView.setMaximumSize(QSize(450, 320))
        self.verticalLayout = QVBoxLayout(LoginView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, 40, 50, 40)
        self.label_title = QLabel(LoginView)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.verticalSpacer_title = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_title)

        self.input_user = QLineEdit(LoginView)
        self.input_user.setObjectName(u"input_user")
        self.input_user.setMinimumSize(QSize(0, 45))

        self.verticalLayout.addWidget(self.input_user)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.input_password = QLineEdit(LoginView)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setMinimumSize(QSize(0, 45))
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.input_password)

        self.lbl_error = QLabel(LoginView)
        self.lbl_error.setObjectName(u"lbl_error")
        self.lbl_error.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_error.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_error)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_login = QPushButton(LoginView)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(0, 45))
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_login)


        self.retranslateUi(LoginView)

        self.btn_login.setDefault(True)


        QMetaObject.connectSlotsByName(LoginView)
    # setupUi

    def retranslateUi(self, LoginView):
        LoginView.setWindowTitle(QCoreApplication.translate("LoginView", u"Iniciar Sesi\u00f3n - CyberSprint", None))
        self.label_title.setText(QCoreApplication.translate("LoginView", u"Inicio de Sesion", None))
        self.input_user.setPlaceholderText(QCoreApplication.translate("LoginView", u"Email", None))
        self.input_password.setPlaceholderText(QCoreApplication.translate("LoginView", u"Contrase\u00f1a", None))
        self.lbl_error.setText("")
        self.btn_login.setText(QCoreApplication.translate("LoginView", u"Entrar", None))
    # retranslateUi

