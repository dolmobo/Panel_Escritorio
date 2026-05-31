# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashBoardView.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_DashboardView(object):
    def setupUi(self, DashboardView):
        if not DashboardView.objectName():
            DashboardView.setObjectName(u"DashboardView")
        DashboardView.resize(1100, 700)
        self.verticalLayout = QVBoxLayout(DashboardView)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.horizontalLayout_top = QHBoxLayout()
        self.horizontalLayout_top.setObjectName(u"horizontalLayout_top")
        self.label_title = QLabel(DashboardView)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setStyleSheet(u"font-size: 26px; font-weight: bold; color: white;")

        self.horizontalLayout_top.addWidget(self.label_title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_top.addItem(self.horizontalSpacer)

        self.btn_refresh = QPushButton(DashboardView)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setMinimumSize(QSize(150, 40))
        self.btn_refresh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"background-color: #e0e0e0; color: black; font-weight: bold; border-radius: 5px;")

        self.horizontalLayout_top.addWidget(self.btn_refresh)


        self.verticalLayout.addLayout(self.horizontalLayout_top)

        self.layout_rankings = QHBoxLayout()
        self.layout_rankings.setSpacing(15)
        self.layout_rankings.setObjectName(u"layout_rankings")
        self.group_score = QGroupBox(DashboardView)
        self.group_score.setObjectName(u"group_score")
        self.group_score.setStyleSheet(u"QGroupBox { \n"
"            color: white; font-weight: bold; font-size: 16px; border: 1px solid #444; margin-top: 20px; border-radius: 5px; \n"
"        }\n"
"        QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; }")
        self.vbox_score = QVBoxLayout(self.group_score)
        self.vbox_score.setObjectName(u"vbox_score")
        self.table_score = QTableWidget(self.group_score)
        if (self.table_score.columnCount() < 2):
            self.table_score.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_score.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_score.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_score.setObjectName(u"table_score")
        self.table_score.setAlternatingRowColors(True)
        self.table_score.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.vbox_score.addWidget(self.table_score)

        self.btnTOPPuntuacion = QPushButton(self.group_score)
        self.btnTOPPuntuacion.setObjectName(u"btnTOPPuntuacion")

        self.vbox_score.addWidget(self.btnTOPPuntuacion)


        self.layout_rankings.addWidget(self.group_score)

        self.group_active = QGroupBox(DashboardView)
        self.group_active.setObjectName(u"group_active")
        self.group_active.setStyleSheet(u"QGroupBox { \n"
"            color: white; font-weight: bold; font-size: 16px; border: 1px solid #444; margin-top: 20px; border-radius: 5px; \n"
"        }\n"
"        QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; }")
        self.vbox_active = QVBoxLayout(self.group_active)
        self.vbox_active.setObjectName(u"vbox_active")
        self.table_active = QTableWidget(self.group_active)
        if (self.table_active.columnCount() < 2):
            self.table_active.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_active.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_active.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.table_active.setObjectName(u"table_active")
        self.table_active.setAlternatingRowColors(True)
        self.table_active.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.vbox_active.addWidget(self.table_active)

        self.btnTOPActivos = QPushButton(self.group_active)
        self.btnTOPActivos.setObjectName(u"btnTOPActivos")

        self.vbox_active.addWidget(self.btnTOPActivos)


        self.layout_rankings.addWidget(self.group_active)

        self.group_jumps = QGroupBox(DashboardView)
        self.group_jumps.setObjectName(u"group_jumps")
        self.group_jumps.setStyleSheet(u"QGroupBox { \n"
"            color: white; font-weight: bold; font-size: 16px; border: 1px solid #444; margin-top: 20px; border-radius: 5px; \n"
"        }\n"
"        QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; }")
        self.vbox_jumps = QVBoxLayout(self.group_jumps)
        self.vbox_jumps.setObjectName(u"vbox_jumps")
        self.table_jumps = QTableWidget(self.group_jumps)
        if (self.table_jumps.columnCount() < 2):
            self.table_jumps.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_jumps.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_jumps.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.table_jumps.setObjectName(u"table_jumps")
        self.table_jumps.setAlternatingRowColors(True)
        self.table_jumps.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.vbox_jumps.addWidget(self.table_jumps)

        self.btnTOPSaltos = QPushButton(self.group_jumps)
        self.btnTOPSaltos.setObjectName(u"btnTOPSaltos")

        self.vbox_jumps.addWidget(self.btnTOPSaltos)


        self.layout_rankings.addWidget(self.group_jumps)


        self.verticalLayout.addLayout(self.layout_rankings)


        self.retranslateUi(DashboardView)

        QMetaObject.connectSlotsByName(DashboardView)
    # setupUi

    def retranslateUi(self, DashboardView):
        DashboardView.setWindowTitle(QCoreApplication.translate("DashboardView", u"Dashboard", None))
        self.label_title.setText(QCoreApplication.translate("DashboardView", u"Panel de Control - Rankings", None))
        self.btn_refresh.setText(QCoreApplication.translate("DashboardView", u"Actualizar Datos", None))
        self.group_score.setTitle(QCoreApplication.translate("DashboardView", u"Top Puntuaci\u00f3n", None))
        ___qtablewidgetitem = self.table_score.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DashboardView", u"Jugador", None));
        ___qtablewidgetitem1 = self.table_score.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DashboardView", u"R\u00e9cord", None));
        self.btnTOPPuntuacion.setText(QCoreApplication.translate("DashboardView", u"Exportar TOP Puntuaci\u00f3n", None))
        self.group_active.setTitle(QCoreApplication.translate("DashboardView", u"M\u00e1s Activos", None))
        ___qtablewidgetitem2 = self.table_active.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DashboardView", u"Jugador", None));
        ___qtablewidgetitem3 = self.table_active.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DashboardView", u"Partidas", None));
        self.btnTOPActivos.setText(QCoreApplication.translate("DashboardView", u"Exportar TOP Activos", None))
        self.group_jumps.setTitle(QCoreApplication.translate("DashboardView", u"M\u00e1s Saltos", None))
        ___qtablewidgetitem4 = self.table_jumps.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DashboardView", u"Jugador", None));
        ___qtablewidgetitem5 = self.table_jumps.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DashboardView", u"Saltos", None));
        self.btnTOPSaltos.setText(QCoreApplication.translate("DashboardView", u"Exportar TOP Saltos", None))
    # retranslateUi

