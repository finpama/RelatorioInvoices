# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 701)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(740, 450))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(33, 0))
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.DataTable = QTableWidget(self.centralwidget)
        if (self.DataTable.columnCount() < 8):
            self.DataTable.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.DataTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.DataTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.DataTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.DataTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.DataTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.DataTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.DataTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.DataTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.DataTable.setObjectName(u"DataTable")
        self.DataTable.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DataTable.sizePolicy().hasHeightForWidth())
        self.DataTable.setSizePolicy(sizePolicy1)
        self.DataTable.setMinimumSize(QSize(0, 24))
        self.DataTable.setMaximumSize(QSize(16777215, 300))
        self.DataTable.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.DataTable.setDragEnabled(True)
        self.DataTable.setShowGrid(True)
        self.DataTable.setGridStyle(Qt.PenStyle.SolidLine)
        self.DataTable.setSortingEnabled(True)
        self.DataTable.setCornerButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.DataTable)


        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, -1, 0, 0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(30, -1, -1, -1)
        self.FileList = QListWidget(self.centralwidget)
        self.FileList.setObjectName(u"FileList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.FileList.sizePolicy().hasHeightForWidth())
        self.FileList.setSizePolicy(sizePolicy2)
        self.FileList.setMinimumSize(QSize(366, 189))
        self.FileList.setMaximumSize(QSize(16777215, 189))

        self.horizontalLayout_3.addWidget(self.FileList)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout_2.setContentsMargins(-1, -1, 13, -1)
        self.FileButton = QPushButton(self.centralwidget)
        self.FileButton.setObjectName(u"FileButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.FileButton.sizePolicy().hasHeightForWidth())
        self.FileButton.setSizePolicy(sizePolicy3)
        self.FileButton.setMinimumSize(QSize(163, 31))
        self.FileButton.setMaximumSize(QSize(195, 31))
        self.FileButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.FileButton.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"\n"
"background-color: #00358F;\n"
"font-weight: bold;\n"
"color: white;")

        self.gridLayout_2.addWidget(self.FileButton, 0, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 40, -1, -1)
        self.GenerateButton = QPushButton(self.centralwidget)
        self.GenerateButton.setObjectName(u"GenerateButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.GenerateButton.sizePolicy().hasHeightForWidth())
        self.GenerateButton.setSizePolicy(sizePolicy5)
        self.GenerateButton.setMinimumSize(QSize(163, 31))
        self.GenerateButton.setMaximumSize(QSize(163, 31))
        self.GenerateButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.GenerateButton.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"\n"
"background-color: rgb(19, 140, 19);\n"
"font-weight: bold;\n"
"color: white;")
        self.GenerateButton.setCheckable(False)

        self.verticalLayout.addWidget(self.GenerateButton)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 5, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 7, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, 14, -1)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy6)

        self.horizontalLayout_7.addWidget(self.widget_2)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy7)
        self.widget_5.setMinimumSize(QSize(709, 0))
        self.SaveButton = QPushButton(self.widget_5)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setGeometry(QRect(550, 50, 161, 31))
        self.SaveButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SaveButton.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"\n"
"background-color: rgb(19, 140, 19);\n"
"font-weight: bold;\n"
"color: white;")
        self.PathButton = QPushButton(self.widget_5)
        self.PathButton.setObjectName(u"PathButton")
        self.PathButton.setGeometry(QRect(510, 10, 201, 31))
        self.PathButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.PathButton.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"\n"
"\n"
"background-color: #00358F;\n"
"font-weight: bold;\n"
"color: white;")
        self.PathInput = QPlainTextEdit(self.widget_5)
        self.PathInput.setObjectName(u"PathInput")
        self.PathInput.setEnabled(False)
        self.PathInput.setGeometry(QRect(20, 10, 481, 31))
        self.PathInput.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.BlankCursor))
        self.PathInput.setStyleSheet(u"")
        self.PathInput.setLineWidth(1)
        self.PathInput.setReadOnly(False)

        self.horizontalLayout_7.addWidget(self.widget_5)


        self.gridLayout.addLayout(self.horizontalLayout_7, 8, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.PathButton, self.SaveButton)
        QWidget.setTabOrder(self.SaveButton, self.FileList)
        QWidget.setTabOrder(self.FileList, self.DataTable)

        self.retranslateUi(MainWindow)

        self.GenerateButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tabelador de Invoices", None))
        ___qtablewidgetitem = self.DataTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Processo", None))
        ___qtablewidgetitem1 = self.DataTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Invoice", None))
        ___qtablewidgetitem2 = self.DataTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        ___qtablewidgetitem3 = self.DataTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        ___qtablewidgetitem4 = self.DataTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        ___qtablewidgetitem5 = self.DataTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Container", None))
        ___qtablewidgetitem6 = self.DataTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Peso", None))
        ___qtablewidgetitem7 = self.DataTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Caixas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tabulador de Invoices", None))
        self.FileButton.setText(QCoreApplication.translate("MainWindow", u"Selecionar Arquivos", None))
        self.GenerateButton.setText(QCoreApplication.translate("MainWindow", u"Gerar Relat\u00f3rio", None))
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"Salvar em Excel", None))
        self.PathButton.setText(QCoreApplication.translate("MainWindow", u"Selecionar local de salvamento", None))
        self.PathInput.setPlainText(QCoreApplication.translate("MainWindow", u"Onde salvar o relat\u00f3rio?", None))
    # retranslateUi

