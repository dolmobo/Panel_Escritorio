# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReportView.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ReportsView(object):
    def setupUi(self, ReportsView):
        if not ReportsView.objectName():
            ReportsView.setObjectName(u"ReportsView")
        ReportsView.resize(1000, 700)
        self.verticalLayout = QVBoxLayout(ReportsView)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, 40, 40, 40)
        self.label_title = QLabel(ReportsView)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.gridLayout_stats = QGridLayout()
        self.gridLayout_stats.setSpacing(20)
        self.gridLayout_stats.setObjectName(u"gridLayout_stats")
        self.card_players = QFrame(ReportsView)
        self.card_players.setObjectName(u"card_players")
        self.vbox_1 = QVBoxLayout(self.card_players)
        self.vbox_1.setObjectName(u"vbox_1")
        self.lbl_monedas_va = QLabel(self.card_players)
        self.lbl_monedas_va.setObjectName(u"lbl_monedas_va")
        self.lbl_monedas_va.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox_1.addWidget(self.lbl_monedas_va)

        self.lbl_monedas = QLabel(self.card_players)
        self.lbl_monedas.setObjectName(u"lbl_monedas")
        self.lbl_monedas.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox_1.addWidget(self.lbl_monedas)


        self.gridLayout_stats.addWidget(self.card_players, 0, 0, 1, 1)

        self.card_record = QFrame(ReportsView)
        self.card_record.setObjectName(u"card_record")
        self.vbox_2 = QVBoxLayout(self.card_record)
        self.vbox_2.setObjectName(u"vbox_2")
        self.lbl_recordva = QLabel(self.card_record)
        self.lbl_recordva.setObjectName(u"lbl_recordva")
        self.lbl_recordva.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox_2.addWidget(self.lbl_recordva)

        self.lbl_record = QLabel(self.card_record)
        self.lbl_record.setObjectName(u"lbl_record")
        self.lbl_record.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox_2.addWidget(self.lbl_record)


        self.gridLayout_stats.addWidget(self.card_record, 0, 1, 1, 1)

        self.card_games = QFrame(ReportsView)
        self.card_games.setObjectName(u"card_games")
        self.vbox_3 = QVBoxLayout(self.card_games)
        self.vbox_3.setObjectName(u"vbox_3")
        self.lbl_partidasva = QLabel(self.card_games)
        self.lbl_partidasva.setObjectName(u"lbl_partidasva")
        self.lbl_partidasva.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox_3.addWidget(self.lbl_partidasva)

        self.lbl_partidas = QLabel(self.card_games)
        self.lbl_partidas.setObjectName(u"lbl_partidas")
        self.lbl_partidas.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox_3.addWidget(self.lbl_partidas)


        self.gridLayout_stats.addWidget(self.card_games, 1, 0, 1, 1)

        self.card_jumps = QFrame(ReportsView)
        self.card_jumps.setObjectName(u"card_jumps")
        self.vbox_4 = QVBoxLayout(self.card_jumps)
        self.vbox_4.setObjectName(u"vbox_4")
        self.lbl_saltosva = QLabel(self.card_jumps)
        self.lbl_saltosva.setObjectName(u"lbl_saltosva")
        self.lbl_saltosva.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox_4.addWidget(self.lbl_saltosva)

        self.lbl_saltos = QLabel(self.card_jumps)
        self.lbl_saltos.setObjectName(u"lbl_saltos")
        self.lbl_saltos.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox_4.addWidget(self.lbl_saltos)


        self.gridLayout_stats.addWidget(self.card_jumps, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_stats)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_generate_pdf = QPushButton(ReportsView)
        self.btn_generate_pdf.setObjectName(u"btn_generate_pdf")
        self.btn_generate_pdf.setMinimumSize(QSize(0, 60))
        self.btn_generate_pdf.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_generate_pdf)


        self.retranslateUi(ReportsView)

        QMetaObject.connectSlotsByName(ReportsView)
    # setupUi

    def retranslateUi(self, ReportsView):
        ReportsView.setWindowTitle(QCoreApplication.translate("ReportsView", u"Informes", None))
        self.label_title.setText(QCoreApplication.translate("ReportsView", u"Resumen del Informe a Generar", None))
        self.lbl_monedas_va.setText(QCoreApplication.translate("ReportsView", u"MONEDAS ACTUALES", None))
        self.lbl_monedas.setText(QCoreApplication.translate("ReportsView", u"<html><head/><body><p><span style=\" font-size:27pt; color:#55ffff;\">1,245</span></p></body></html>", None))
        self.lbl_recordva.setText(QCoreApplication.translate("ReportsView", u"R\u00c9CORD MAXIMO", None))
        self.lbl_record.setText(QCoreApplication.translate("ReportsView", u"<html><head/><body><p><span style=\" font-size:27pt; color:#55ffff;\">9999</span></p></body></html>", None))
        self.lbl_partidasva.setText(QCoreApplication.translate("ReportsView", u"PARTIDAS JUGADAS", None))
        self.lbl_partidas.setText(QCoreApplication.translate("ReportsView", u"<html><head/><body><p><span style=\" font-size:27pt; color:#ffaa00;\">8,530</span></p></body></html>", None))
        self.lbl_saltosva.setText(QCoreApplication.translate("ReportsView", u"SALTOS TOTALES", None))
        self.lbl_saltos.setText(QCoreApplication.translate("ReportsView", u"<html><head/><body><p><span style=\" font-size:27pt; color:#ffaa00;\">120,400</span></p></body></html>", None))
        self.btn_generate_pdf.setText(QCoreApplication.translate("ReportsView", u"Imprimir Informe PDF", None))
    # retranslateUi

