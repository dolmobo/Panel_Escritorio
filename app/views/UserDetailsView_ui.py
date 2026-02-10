# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserDetailsView.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_UserDetailsDialog(object):
    def setupUi(self, UserDetailsDialog):
        if not UserDetailsDialog.objectName():
            UserDetailsDialog.setObjectName(u"UserDetailsDialog")
        UserDetailsDialog.resize(320, 380)
        self.verticalLayout = QVBoxLayout(UserDetailsDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_card = QFrame(UserDetailsDialog)
        self.frame_card.setObjectName(u"frame_card")
        self.frame_card.setFrameShape(QFrame.StyledPanel)
        self.frame_card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_card)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 25, 20, 25)
        self.lbl_username = QLabel(self.frame_card)
        self.lbl_username.setObjectName(u"lbl_username")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.lbl_username.setFont(font)
        self.lbl_username.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_username)

        self.line = QFrame(self.frame_card)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(12)
        self.label_2 = QLabel(self.frame_card)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lbl_record = QLabel(self.frame_card)
        self.lbl_record.setObjectName(u"lbl_record")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.lbl_record.setFont(font1)
        self.lbl_record.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_record, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_card)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.lbl_games = QLabel(self.frame_card)
        self.lbl_games.setObjectName(u"lbl_games")
        self.lbl_games.setFont(font1)
        self.lbl_games.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_games, 1, 1, 1, 1)

        self.label_6 = QLabel(self.frame_card)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.lbl_jumps = QLabel(self.frame_card)
        self.lbl_jumps.setObjectName(u"lbl_jumps")
        self.lbl_jumps.setFont(font1)
        self.lbl_jumps.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_jumps, 2, 1, 1, 1)

        self.label_8 = QLabel(self.frame_card)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.lbl_coins = QLabel(self.frame_card)
        self.lbl_coins.setObjectName(u"lbl_coins")
        self.lbl_coins.setFont(font1)
        self.lbl_coins.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_coins, 3, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_close = QPushButton(self.frame_card)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(0, 35))
        self.btn_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.frame_card)


        self.retranslateUi(UserDetailsDialog)

        QMetaObject.connectSlotsByName(UserDetailsDialog)
    # setupUi

    def retranslateUi(self, UserDetailsDialog):
        UserDetailsDialog.setWindowTitle(QCoreApplication.translate("UserDetailsDialog", u"Detalle de Usuario", None))
        self.lbl_username.setText(QCoreApplication.translate("UserDetailsDialog", u"USERNAME", None))
        self.label_2.setText(QCoreApplication.translate("UserDetailsDialog", u"R\u00e9cord M\u00e1ximo", None))
        self.lbl_record.setText(QCoreApplication.translate("UserDetailsDialog", u"0 pts", None))
        self.label_4.setText(QCoreApplication.translate("UserDetailsDialog", u"Partidas Jugadas", None))
        self.lbl_games.setText(QCoreApplication.translate("UserDetailsDialog", u"0", None))
        self.label_6.setText(QCoreApplication.translate("UserDetailsDialog", u"Saltos Totales", None))
        self.lbl_jumps.setText(QCoreApplication.translate("UserDetailsDialog", u"0", None))
        self.label_8.setText(QCoreApplication.translate("UserDetailsDialog", u"Monedas", None))
        self.lbl_coins.setText(QCoreApplication.translate("UserDetailsDialog", u"0", None))
        self.btn_close.setText(QCoreApplication.translate("UserDetailsDialog", u"Cerrar", None))
    # retranslateUi

