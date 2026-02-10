# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainView.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainView(object):
    def setupUi(self, MainView):
        if not MainView.objectName():
            MainView.setObjectName(u"MainView")
        MainView.resize(1200, 700)
        self.centralwidget = QWidget(MainView)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(240, 0))
        self.frame_menu.setMaximumSize(QSize(240, 16777215))
        self.verticalLayout = QVBoxLayout(self.frame_menu)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 40, -1, 20)
        self.label_logo = QLabel(self.frame_menu)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(0, 120))
        self.label_logo.setMaximumSize(QSize(240, 120))
        self.label_logo.setPixmap(QPixmap(u"logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_logo)

        self.btn_dashboard = QPushButton(self.frame_menu)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        self.btn_dashboard.setMinimumSize(QSize(0, 50))
        self.btn_dashboard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_dashboard)

        self.btn_reports = QPushButton(self.frame_menu)
        self.btn_reports.setObjectName(u"btn_reports")
        self.btn_reports.setMinimumSize(QSize(0, 50))
        self.btn_reports.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_reports)

        self.btn_settings = QPushButton(self.frame_menu)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(0, 50))
        self.btn_settings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_settings)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_exit = QPushButton(self.frame_menu)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(0, 50))
        self.btn_exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_exit)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.stack_content = QStackedWidget(self.centralwidget)
        self.stack_content.setObjectName(u"stack_content")

        self.horizontalLayout.addWidget(self.stack_content)

        MainView.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainView)

        QMetaObject.connectSlotsByName(MainView)
    # setupUi

    def retranslateUi(self, MainView):
        MainView.setWindowTitle(QCoreApplication.translate("MainView", u"CyberSprint - Panel de Control", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainView", u"Ranking Global", None))
        self.btn_reports.setText(QCoreApplication.translate("MainView", u"Generar Informe", None))
        self.btn_settings.setText(QCoreApplication.translate("MainView", u"Configuraci\u00f3n", None))
        self.btn_exit.setText(QCoreApplication.translate("MainView", u"Cerrar Sesi\u00f3n", None))
    # retranslateUi

