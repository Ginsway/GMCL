# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)
import gmcl_rc

class Ui_GMCL(object):
    def setupUi(self, GMCL):
        if not GMCL.objectName():
            GMCL.setObjectName(u"GMCL")
        GMCL.resize(854, 480)
        self.centralwidget = QWidget(GMCL)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 881, 581))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.layoutWidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.layoutWidget1 = QWidget(self.page_1)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 721, 551))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.quit = QPushButton(self.layoutWidget1)
        self.quit.setObjectName(u"quit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quit.sizePolicy().hasHeightForWidth())
        self.quit.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.quit)

        self.horizontalSpacer = QSpacerItem(178, 268, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(88, 98, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.rungameButton = QPushButton(self.layoutWidget1)
        self.rungameButton.setObjectName(u"rungameButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.rungameButton.sizePolicy().hasHeightForWidth())
        self.rungameButton.setSizePolicy(sizePolicy1)
        self.rungameButton.setMinimumSize(QSize(300, 0))
        self.rungameButton.setMaximumSize(QSize(300, 100))
        font = QFont()
        font.setPointSize(26)
        self.rungameButton.setFont(font)
        self.rungameButton.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_3.addWidget(self.rungameButton)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.version_label = QLabel(self.layoutWidget1)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.version_label)

        self.comboBox = QComboBox(self.layoutWidget1)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.toolButton_4 = QToolButton(self.layoutWidget1)
        self.toolButton_4.setObjectName(u"toolButton_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.toolButton_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.stackedWidget.addWidget(self.page_1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.layoutWidget2 = QWidget(self.page2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 791, 461))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.game_path = QHBoxLayout()
        self.game_path.setObjectName(u"game_path")
        self.game_path_label = QLabel(self.layoutWidget2)
        self.game_path_label.setObjectName(u"game_path_label")

        self.game_path.addWidget(self.game_path_label)

        self.game_path_lineEdit = QLineEdit(self.layoutWidget2)
        self.game_path_lineEdit.setObjectName(u"game_path_lineEdit")

        self.game_path.addWidget(self.game_path_lineEdit)

        self.game_select = QToolButton(self.layoutWidget2)
        self.game_select.setObjectName(u"game_select")
        icon = QIcon()
        icon.addFile(u":/gmcl/assets/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.game_select.setIcon(icon)

        self.game_path.addWidget(self.game_select)


        self.verticalLayout.addLayout(self.game_path)

        self.java_path = QHBoxLayout()
        self.java_path.setObjectName(u"java_path")
        self.java_path_label = QLabel(self.layoutWidget2)
        self.java_path_label.setObjectName(u"java_path_label")

        self.java_path.addWidget(self.java_path_label)

        self.java_path_lineEdit = QLineEdit(self.layoutWidget2)
        self.java_path_lineEdit.setObjectName(u"java_path_lineEdit")

        self.java_path.addWidget(self.java_path_lineEdit)

        self.java_select = QToolButton(self.layoutWidget2)
        self.java_select.setObjectName(u"java_select")
        self.java_select.setIcon(icon)

        self.java_path.addWidget(self.java_select)


        self.verticalLayout.addLayout(self.java_path)

        self.username = QHBoxLayout()
        self.username.setObjectName(u"username")
        self.username_label = QLabel(self.layoutWidget2)
        self.username_label.setObjectName(u"username_label")

        self.username.addWidget(self.username_label)

        self.username_lineEdit = QLineEdit(self.layoutWidget2)
        self.username_lineEdit.setObjectName(u"username_lineEdit")

        self.username.addWidget(self.username_lineEdit)


        self.verticalLayout.addLayout(self.username)

        self.men = QHBoxLayout()
        self.men.setObjectName(u"men")
        self.maxmen_label = QLabel(self.layoutWidget2)
        self.maxmen_label.setObjectName(u"maxmen_label")

        self.men.addWidget(self.maxmen_label)

        self.horizontalSlider = QSlider(self.layoutWidget2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.men.addWidget(self.horizontalSlider)


        self.verticalLayout.addLayout(self.men)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.stackedWidget.addWidget(self.page2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 4, 1)

        self.to1 = QToolButton(self.widget)
        self.to1.setObjectName(u"to1")
        self.to1.setCheckable(True)
        self.to1.setAutoExclusive(True)
        self.to1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.gridLayout.addWidget(self.to1, 1, 0, 1, 1)

        self.to2 = QToolButton(self.widget)
        self.to2.setObjectName(u"to2")
        self.to2.setCheckable(True)
        self.to2.setAutoExclusive(True)
        self.to2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.gridLayout.addWidget(self.to2, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.to0 = QToolButton(self.widget)
        self.to0.setObjectName(u"to0")
        self.to0.setCheckable(True)
        self.to0.setAutoExclusive(True)
        self.to0.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.gridLayout.addWidget(self.to0, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        GMCL.setCentralWidget(self.centralwidget)

        self.retranslateUi(GMCL)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(GMCL)
    # setupUi

    def retranslateUi(self, GMCL):
        GMCL.setWindowTitle(QCoreApplication.translate("GMCL", u"GMCL Alpha-1", None))
        self.quit.setText(QCoreApplication.translate("GMCL", u"\u9000\u51fa", None))
        self.rungameButton.setText(QCoreApplication.translate("GMCL", u"\u542f\u52a8\u6e38\u620f", None))
        self.version_label.setText(QCoreApplication.translate("GMCL", u"\u9009\u62e9\u7248\u672c", None))
        self.toolButton_4.setText(QCoreApplication.translate("GMCL", u"...", None))
        self.game_path_label.setText(QCoreApplication.translate("GMCL", u"\u6e38\u620f\u6839\u76ee\u5f55", None))
        self.game_path_lineEdit.setText("")
        self.game_path_lineEdit.setPlaceholderText(QCoreApplication.translate("GMCL", u"\u8bf7\u8f93\u5165\u6e38\u620f\u6839\u76ee\u5f55\uff08.minecraft\uff09", None))
        self.game_select.setText(QCoreApplication.translate("GMCL", u"...", None))
        self.java_path_label.setText(QCoreApplication.translate("GMCL", u"java\u8def\u5f84", None))
        self.java_path_lineEdit.setPlaceholderText(QCoreApplication.translate("GMCL", u"\u8bf7\u8f93\u5165Java\u8def\u5f84\uff08java.exe\uff09", None))
        self.java_select.setText(QCoreApplication.translate("GMCL", u"...", None))
        self.username_label.setText(QCoreApplication.translate("GMCL", u"\u7528\u6237\u540d", None))
        self.username_lineEdit.setPlaceholderText(QCoreApplication.translate("GMCL", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d\uff08\u6682\u65f6\u4ec5\u652f\u6301\u79bb\u7ebf\u767b\u5f55\uff09", None))
        self.maxmen_label.setText(QCoreApplication.translate("GMCL", u"\u6700\u5927\u5185\u5b58", None))
        self.to1.setText(QCoreApplication.translate("GMCL", u"\u8bbe\u7f6e", None))
        self.to2.setText(QCoreApplication.translate("GMCL", u"...", None))
        self.to0.setText(QCoreApplication.translate("GMCL", u"\u4e3b\u9875", None))
    # retranslateUi

