# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingView.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_SettingsView(object):
    def setupUi(self, SettingsView):
        if not SettingsView.objectName():
            SettingsView.setObjectName(u"SettingsView")
        SettingsView.resize(800, 600)
        self.verticalLayout = QVBoxLayout(SettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, 50, 50, 50)
        self.label_title = QLabel(SettingsView)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setStyleSheet(u"font-size: 24px; font-weight: bold; color: white; margin-bottom: 30px;")

        self.verticalLayout.addWidget(self.label_title)

        self.label_theme = QLabel(SettingsView)
        self.label_theme.setObjectName(u"label_theme")
        self.label_theme.setStyleSheet(u"font-size: 14px; color: #ccc;")

        self.verticalLayout.addWidget(self.label_theme)

        self.combo_theme = QComboBox(SettingsView)
        self.combo_theme.addItem("")
        self.combo_theme.addItem("")
        self.combo_theme.setObjectName(u"combo_theme")
        self.combo_theme.setMinimumSize(QSize(300, 40))
        self.combo_theme.setStyleSheet(u"QComboBox {\n"
"	background-color: #444;\n"
"	color: white;\n"
"	padding: 5px;\n"
"	border: 1px solid #555;\n"
"}")

        self.verticalLayout.addWidget(self.combo_theme)

        self.label_lang = QLabel(SettingsView)
        self.label_lang.setObjectName(u"label_lang")
        self.label_lang.setStyleSheet(u"font-size: 14px; color: #ccc; margin-top: 20px;")

        self.verticalLayout.addWidget(self.label_lang)

        self.combo_language = QComboBox(SettingsView)
        self.combo_language.addItem("")
        self.combo_language.addItem("")
        self.combo_language.setObjectName(u"combo_language")
        self.combo_language.setMinimumSize(QSize(300, 40))
        self.combo_language.setStyleSheet(u"QComboBox {\n"
"	background-color: #444;\n"
"	color: white;\n"
"	padding: 5px;\n"
"	border: 1px solid #555;\n"
"}")

        self.verticalLayout.addWidget(self.combo_language)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SettingsView)

        QMetaObject.connectSlotsByName(SettingsView)
    # setupUi

    def retranslateUi(self, SettingsView):
        SettingsView.setWindowTitle(QCoreApplication.translate("SettingsView", u"Configuraci\u00f3n", None))
        self.label_title.setText(QCoreApplication.translate("SettingsView", u"Configuraci\u00f3n del Sistema", None))
        self.label_theme.setText(QCoreApplication.translate("SettingsView", u"Apariencia de la aplicaci\u00f3n:", None))
        self.combo_theme.setItemText(0, QCoreApplication.translate("SettingsView", u"Claro", None))
        self.combo_theme.setItemText(1, QCoreApplication.translate("SettingsView", u"Oscuro", None))

        self.label_lang.setText(QCoreApplication.translate("SettingsView", u"Idioma / Language:", None))
        self.combo_language.setItemText(0, QCoreApplication.translate("SettingsView", u"Espa\u00f1ol", None))
        self.combo_language.setItemText(1, QCoreApplication.translate("SettingsView", u"Ingl\u00e9s", None))

    # retranslateUi

