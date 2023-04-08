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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QTabWidget, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MinecraftLauncher(object):
    def setupUi(self, MinecraftLauncher):
        if not MinecraftLauncher.objectName():
            MinecraftLauncher.setObjectName(u"MinecraftLauncher")
        MinecraftLauncher.resize(872, 498)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MinecraftLauncher.sizePolicy().hasHeightForWidth())
        MinecraftLauncher.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(MinecraftLauncher)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(MinecraftLauncher)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QSize(854, 480))
        self.tabWidget.setMaximumSize(QSize(836, 16777215))
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.main.setMinimumSize(QSize(0, 0))
        self.widget = QWidget(self.main)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 9, 831, 431))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(178, 268, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(88, 98, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.version_label = QLabel(self.widget)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.version_label)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.toolButton = QToolButton(self.widget)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.toolButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.quit = QPushButton(self.widget)
        self.quit.setObjectName(u"quit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.quit.sizePolicy().hasHeightForWidth())
        self.quit.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.quit)

        self.rungameButton = QPushButton(self.widget)
        self.rungameButton.setObjectName(u"rungameButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.rungameButton.sizePolicy().hasHeightForWidth())
        self.rungameButton.setSizePolicy(sizePolicy3)
        self.rungameButton.setMinimumSize(QSize(300, 0))
        self.rungameButton.setMaximumSize(QSize(300, 100))
        font = QFont()
        font.setPointSize(26)
        self.rungameButton.setFont(font)
        self.rungameButton.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout.addWidget(self.rungameButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.main, "")
        self.setting = QWidget()
        self.setting.setObjectName(u"setting")
        self.widget1 = QWidget(self.setting)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(13, 4, 831, 441))
        self.horizontalLayout_5 = QHBoxLayout(self.widget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.game_path = QHBoxLayout()
        self.game_path.setObjectName(u"game_path")
        self.game_path_label = QLabel(self.widget1)
        self.game_path_label.setObjectName(u"game_path_label")

        self.game_path.addWidget(self.game_path_label)

        self.game_path_lineEdit = QLineEdit(self.widget1)
        self.game_path_lineEdit.setObjectName(u"game_path_lineEdit")

        self.game_path.addWidget(self.game_path_lineEdit)

        self.game_select = QToolButton(self.widget1)
        self.game_select.setObjectName(u"game_select")

        self.game_path.addWidget(self.game_select)


        self.verticalLayout.addLayout(self.game_path)

        self.java_path = QHBoxLayout()
        self.java_path.setObjectName(u"java_path")
        self.java_path_label = QLabel(self.widget1)
        self.java_path_label.setObjectName(u"java_path_label")

        self.java_path.addWidget(self.java_path_label)

        self.java_path_lineEdit = QLineEdit(self.widget1)
        self.java_path_lineEdit.setObjectName(u"java_path_lineEdit")

        self.java_path.addWidget(self.java_path_lineEdit)

        self.java_select = QToolButton(self.widget1)
        self.java_select.setObjectName(u"java_select")

        self.java_path.addWidget(self.java_select)


        self.verticalLayout.addLayout(self.java_path)

        self.username = QHBoxLayout()
        self.username.setObjectName(u"username")
        self.username_label = QLabel(self.widget1)
        self.username_label.setObjectName(u"username_label")

        self.username.addWidget(self.username_label)

        self.username_lineEdit = QLineEdit(self.widget1)
        self.username_lineEdit.setObjectName(u"username_lineEdit")

        self.username.addWidget(self.username_lineEdit)


        self.verticalLayout.addLayout(self.username)

        self.men = QHBoxLayout()
        self.men.setObjectName(u"men")
        self.maxmen_label = QLabel(self.widget1)
        self.maxmen_label.setObjectName(u"maxmen_label")

        self.men.addWidget(self.maxmen_label)

        self.horizontalSlider = QSlider(self.widget1)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.men.addWidget(self.horizontalSlider)


        self.verticalLayout.addLayout(self.men)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.tabWidget.addTab(self.setting, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(MinecraftLauncher)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MinecraftLauncher)
    # setupUi

    def retranslateUi(self, MinecraftLauncher):
        MinecraftLauncher.setWindowTitle(QCoreApplication.translate("MinecraftLauncher", u"Minecraft Launcher", None))
        self.version_label.setText(QCoreApplication.translate("MinecraftLauncher", u"\u9009\u62e9\u7248\u672c", None))
        self.toolButton.setText(QCoreApplication.translate("MinecraftLauncher", u"...", None))
        self.quit.setText(QCoreApplication.translate("MinecraftLauncher", u"\u9000\u51fa", None))
        self.rungameButton.setText(QCoreApplication.translate("MinecraftLauncher", u"\u542f\u52a8\u6e38\u620f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), QCoreApplication.translate("MinecraftLauncher", u"\u4e3b\u9875", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting), QCoreApplication.translate("MinecraftLauncher", u"\u8bbe\u7f6e", None))
    # retranslateUi

