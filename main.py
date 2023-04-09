from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow

from os import scandir
from threading import Thread
from sys import exit

from Ui_main import Ui_GMCL
from gmclcore import run, Config


def rungame(java_path, game_path):
    # run(mcdir="D:/Project/PycharmProjects/MinecraftLauncher/.minecraft", version="1.19.4",
    # javaw_path="D:\Software\Java\jdk-17.0.4.1\\bin\javaw.exe",
    # max_men="1024M")
    rung = Thread(target=run, args=(game_path,
                                    "1.19.4", java_path, "1024M"))
    rung.start()


class Main(QMainWindow, Ui_GMCL):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.c()
        self.config = Config()
        self.load()
        # self.ui = QUiLoader().load("assets/main.ui")
        self.bind()

    def load(self):
        # self.java_select.setIcon(QIcon("./assets/folder.svg"))
        # self.game_select.setIcon(QIcon("./assets/folder.svg"))
        self.java_path_lineEdit.setText(self.config.get("java_path"))
        self.game_path_lineEdit.setText(self.config.get("game_dir"))
        self.get_version_list()

    def bind(self):
        self.rungameButton.clicked.connect(lambda:
                                           rungame(self.java_path_lineEdit.text(), self.game_path_lineEdit.text()))
        self.java_select.clicked.connect(self.get_java_path)
        self.game_select.clicked.connect(self.get_game_path)
        self.quit.clicked.connect(exit)

    def c(self):
        self.stackedWidget.setCurrentIndex(0)
        self.to0.setChecked(True)
        self.to0.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.to1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.to2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

    def get_java_path(self):
        java_path, _ = QFileDialog.getOpenFileName(
            self, "", r"C:\\", "Java (java.exe)")
        if java_path:  # 防止点取消后清空
            self.java_path_lineEdit.setText(java_path)
            self.config.save("java_path", java_path)
            self.java_path_lineEdit.setText(self.config.get("java_path"))

    def get_game_path(self):
        game_dir = QFileDialog.getExistingDirectory(
            self, "选择游戏根目录", r"C:\\")
        if game_dir:  # 防止点取消后清空
            self.java_path_lineEdit.setText(game_dir)
            self.config.save("game_dir", game_dir)
            self.game_path_lineEdit.setText(self.config.get("game_dir"))

    def get_version_list(self):
        for i in scandir("./.minecraft/versions"):
            if i.is_dir():
                self.comboBox.addItem(i.name)


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon("assets/icon.png"))
    main = Main()
    main.show()
    app.exec()
