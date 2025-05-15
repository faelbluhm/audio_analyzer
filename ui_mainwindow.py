# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(812, 599)
        self.meniLoadFile = QAction(MainWindow)
        self.meniLoadFile.setObjectName(u"meniLoadFile")
        self.menuExit = QAction(MainWindow)
        self.menuExit.setObjectName(u"menuExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.controlsWidget = QWidget(self.centralwidget)
        self.controlsWidget.setObjectName(u"controlsWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlsWidget.sizePolicy().hasHeightForWidth())
        self.controlsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.controlsWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.selectFileButton = QPushButton(self.controlsWidget)
        self.selectFileButton.setObjectName(u"selectFileButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.selectFileButton.sizePolicy().hasHeightForWidth())
        self.selectFileButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.selectFileButton)

        self.label = QLabel(self.controlsWidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.playButton = QPushButton(self.controlsWidget)
        self.playButton.setObjectName(u"playButton")

        self.horizontalLayout_2.addWidget(self.playButton)

        self.stopButton = QPushButton(self.controlsWidget)
        self.stopButton.setObjectName(u"stopButton")

        self.horizontalLayout_2.addWidget(self.stopButton)

        self.horizontalSpacer = QSpacerItem(578, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_5.addWidget(self.controlsWidget)

        self.plotWidget = QWidget(self.centralwidget)
        self.plotWidget.setObjectName(u"plotWidget")
        self.verticalLayout_4 = QVBoxLayout(self.plotWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.timePlotWidget = PlotWidget(self.plotWidget)
        self.timePlotWidget.setObjectName(u"timePlotWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.timePlotWidget.sizePolicy().hasHeightForWidth())
        self.timePlotWidget.setSizePolicy(sizePolicy3)
        self.timePlotWidget.setMinimumSize(QSize(300, 200))

        self.verticalLayout_2.addWidget(self.timePlotWidget)

        self.freqPlotWidget = PlotWidget(self.plotWidget)
        self.freqPlotWidget.setObjectName(u"freqPlotWidget")
        sizePolicy3.setHeightForWidth(self.freqPlotWidget.sizePolicy().hasHeightForWidth())
        self.freqPlotWidget.setSizePolicy(sizePolicy3)
        self.freqPlotWidget.setMinimumSize(QSize(300, 200))

        self.verticalLayout_2.addWidget(self.freqPlotWidget)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addWidget(self.plotWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 812, 28))
        self.menuOption = QMenu(self.menubar)
        self.menuOption.setObjectName(u"menuOption")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOption.menuAction())
        self.menuOption.addAction(self.meniLoadFile)
        self.menuOption.addAction(self.menuExit)

        self.retranslateUi(MainWindow)
        self.menuExit.triggered["bool"].connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.meniLoadFile.setText(QCoreApplication.translate("MainWindow", u"Load file", None))
        self.menuExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.selectFileButton.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"No file selected", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.menuOption.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

