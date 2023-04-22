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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QToolButton, QVBoxLayout, QWidget)
import gmcl_rc

class Ui_MinecraftLauncher(object):
    def setupUi(self, MinecraftLauncher):
        if not MinecraftLauncher.objectName():
            MinecraftLauncher.setObjectName(u"MinecraftLauncher")
        MinecraftLauncher.resize(854, 480)
        icon = QIcon()
        icon.addFile(u":/resources/reinforced_deepslate.png", QSize(), QIcon.Normal, QIcon.On)
        MinecraftLauncher.setWindowIcon(icon)
        MinecraftLauncher.setAnimated(True)
        self.centralwidget = QWidget(MinecraftLauncher)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_btn = QToolButton(self.centralwidget)
        self.home_btn.setObjectName(u"home_btn")
        icon1 = QIcon()
        icon1.addFile(u":/resources/home.svg", QSize(), QIcon.Normal, QIcon.On)
        self.home_btn.setIcon(icon1)
        self.home_btn.setAutoRepeat(False)
        self.home_btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.home_btn.setAutoRaise(False)

        self.verticalLayout.addWidget(self.home_btn)

        self.core_btn = QToolButton(self.centralwidget)
        self.core_btn.setObjectName(u"core_btn")

        self.verticalLayout.addWidget(self.core_btn)

        self.user_btn = QToolButton(self.centralwidget)
        self.user_btn.setObjectName(u"user_btn")
        icon2 = QIcon()
        icon2.addFile(u":/resources/user.svg", QSize(), QIcon.Normal, QIcon.On)
        self.user_btn.setIcon(icon2)
        self.user_btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.user_btn)

        self.toolButton_4 = QToolButton(self.centralwidget)
        self.toolButton_4.setObjectName(u"toolButton_4")

        self.verticalLayout.addWidget(self.toolButton_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.quit_btn = QToolButton(self.centralwidget)
        self.quit_btn.setObjectName(u"quit_btn")
        icon3 = QIcon()
        icon3.addFile(u":/resources/exit.svg", QSize(), QIcon.Normal, QIcon.On)
        self.quit_btn.setIcon(icon3)

        self.horizontalLayout.addWidget(self.quit_btn)

        self.setting_btn = QToolButton(self.centralwidget)
        self.setting_btn.setObjectName(u"setting_btn")
        icon4 = QIcon()
        icon4.addFile(u":/resources/settings.svg", QSize(), QIcon.Normal, QIcon.On)
        self.setting_btn.setIcon(icon4)
        self.setting_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.setting_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.stackedWidget.setLineWidth(1)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_3 = QVBoxLayout(self.home)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.home)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setTextFormat(Qt.AutoText)

        self.horizontalLayout_3.addWidget(self.label)

        self.comboBox = QComboBox(self.home)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.toolButton_7 = QToolButton(self.home)
        self.toolButton_7.setObjectName(u"toolButton_7")
        icon5 = QIcon()
        icon5.addFile(u":/resources/sliders.svg", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_7.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.toolButton_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.run_btn = QPushButton(self.home)
        self.run_btn.setObjectName(u"run_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_btn.sizePolicy().hasHeightForWidth())
        self.run_btn.setSizePolicy(sizePolicy)
        self.run_btn.setMinimumSize(QSize(200, 50))

        self.verticalLayout_2.addWidget(self.run_btn)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.home)
        self.core = QWidget()
        self.core.setObjectName(u"core")
        self.stackedWidget.addWidget(self.core)
        self.user = QWidget()
        self.user.setObjectName(u"user")
        self.stackedWidget.addWidget(self.user)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.setting = QWidget()
        self.setting.setObjectName(u"setting")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.setting.sizePolicy().hasHeightForWidth())
        self.setting.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.setting)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.game_path = QHBoxLayout()
        self.game_path.setObjectName(u"game_path")
        self.game_path_label = QLabel(self.setting)
        self.game_path_label.setObjectName(u"game_path_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.game_path_label.sizePolicy().hasHeightForWidth())
        self.game_path_label.setSizePolicy(sizePolicy2)

        self.game_path.addWidget(self.game_path_label)

        self.game_path_lineEdit = QLineEdit(self.setting)
        self.game_path_lineEdit.setObjectName(u"game_path_lineEdit")

        self.game_path.addWidget(self.game_path_lineEdit)

        self.game_select = QToolButton(self.setting)
        self.game_select.setObjectName(u"game_select")
        icon6 = QIcon()
        icon6.addFile(u":/resources/folder-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.game_select.setIcon(icon6)

        self.game_path.addWidget(self.game_select)


        self.verticalLayout_4.addLayout(self.game_path)

        self.java_path = QHBoxLayout()
        self.java_path.setSpacing(6)
        self.java_path.setObjectName(u"java_path")
        self.java_path_label = QLabel(self.setting)
        self.java_path_label.setObjectName(u"java_path_label")
        sizePolicy2.setHeightForWidth(self.java_path_label.sizePolicy().hasHeightForWidth())
        self.java_path_label.setSizePolicy(sizePolicy2)

        self.java_path.addWidget(self.java_path_label)

        self.java_path_lineEdit = QLineEdit(self.setting)
        self.java_path_lineEdit.setObjectName(u"java_path_lineEdit")

        self.java_path.addWidget(self.java_path_lineEdit)

        self.java_select = QToolButton(self.setting)
        self.java_select.setObjectName(u"java_select")
        self.java_select.setIcon(icon6)

        self.java_path.addWidget(self.java_select)


        self.verticalLayout_4.addLayout(self.java_path)

        self.username = QHBoxLayout()
        self.username.setObjectName(u"username")
        self.username_label = QLabel(self.setting)
        self.username_label.setObjectName(u"username_label")
        sizePolicy2.setHeightForWidth(self.username_label.sizePolicy().hasHeightForWidth())
        self.username_label.setSizePolicy(sizePolicy2)

        self.username.addWidget(self.username_label)

        self.username_lineEdit = QLineEdit(self.setting)
        self.username_lineEdit.setObjectName(u"username_lineEdit")

        self.username.addWidget(self.username_lineEdit)


        self.verticalLayout_4.addLayout(self.username)

        self.men = QHBoxLayout()
        self.men.setObjectName(u"men")
        self.maxmen_label = QLabel(self.setting)
        self.maxmen_label.setObjectName(u"maxmen_label")
        sizePolicy2.setHeightForWidth(self.maxmen_label.sizePolicy().hasHeightForWidth())
        self.maxmen_label.setSizePolicy(sizePolicy2)

        self.men.addWidget(self.maxmen_label)

        self.horizontalSlider = QSlider(self.setting)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.men.addWidget(self.horizontalSlider)


        self.verticalLayout_4.addLayout(self.men)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.setting)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        MinecraftLauncher.setCentralWidget(self.centralwidget)

        self.retranslateUi(MinecraftLauncher)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MinecraftLauncher)
    # setupUi

    def retranslateUi(self, MinecraftLauncher):
        MinecraftLauncher.setWindowTitle(QCoreApplication.translate("MinecraftLauncher", u"GMCL \u03b1-1", None))
        self.home_btn.setText(QCoreApplication.translate("MinecraftLauncher", u"\u4e3b\u9875", None))
        self.core_btn.setText(QCoreApplication.translate("MinecraftLauncher", u"\u6838\u5fc3", None))
        self.user_btn.setText(QCoreApplication.translate("MinecraftLauncher", u"\u8d26\u6237", None))
        self.toolButton_4.setText(QCoreApplication.translate("MinecraftLauncher", u"PushButton", None))
        self.quit_btn.setText(QCoreApplication.translate("MinecraftLauncher", u"...", None))
        self.setting_btn.setText(QCoreApplication.translate("MinecraftLauncher", u"...", None))
        self.label.setText(QCoreApplication.translate("MinecraftLauncher", u"\u9009\u62e9\u7248\u672c", None))
        self.toolButton_7.setText(QCoreApplication.translate("MinecraftLauncher", u"...", None))
        self.run_btn.setText(QCoreApplication.translate("MinecraftLauncher", u"\u542f\u52a8\u6e38\u620f", None))
        self.game_path_label.setText(QCoreApplication.translate("MinecraftLauncher", u"\u6e38\u620f\u6839\u76ee\u5f55", None))
        self.game_path_lineEdit.setText("")
        self.game_path_lineEdit.setPlaceholderText(QCoreApplication.translate("MinecraftLauncher", u"\u8bf7\u8f93\u5165\u6e38\u620f\u6839\u76ee\u5f55\uff08.minecraft\uff09", None))
        self.game_select.setText(QCoreApplication.translate("MinecraftLauncher", u"...", None))
        self.java_path_label.setText(QCoreApplication.translate("MinecraftLauncher", u"java\u8def\u5f84", None))
        self.java_path_lineEdit.setPlaceholderText(QCoreApplication.translate("MinecraftLauncher", u"\u8bf7\u8f93\u5165Java\u8def\u5f84\uff08java.exe\uff09", None))
        self.java_select.setText(QCoreApplication.translate("MinecraftLauncher", u"...", None))
        self.username_label.setText(QCoreApplication.translate("MinecraftLauncher", u"\u7528\u6237\u540d", None))
        self.username_lineEdit.setPlaceholderText(QCoreApplication.translate("MinecraftLauncher", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d\uff08\u6682\u65f6\u4ec5\u652f\u6301\u79bb\u7ebf\u767b\u5f55\uff09", None))
        self.maxmen_label.setText(QCoreApplication.translate("MinecraftLauncher", u"\u6700\u5927\u5185\u5b58", None))
    # retranslateUi

