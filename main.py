
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QFileDialog

from threading import Thread
from os import scandir
from Ui_main import Ui_MinecraftLauncher
from gmclcore import run, Config


def rungame(java_path, game_path):
    # run(mcdir="D:/Project/PycharmProjects/MinecraftLauncher/.minecraft", version="1.19.4",
    # javaw_path="D:\Software\Java\jdk-17.0.4.1\\bin\javaw.exe",
    # max_men="1024M")
    rung = Thread(target=run, args=(game_path,
                                    "1.19.4", java_path, "1024M"))
    rung.start()


class Launcher(Ui_MinecraftLauncher, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.config = Config()
        self.load()
        self.bind()
        self.set_sidebar()

    def bind(self):
        self.run_btn.clicked.connect(lambda:
                                     rungame(self.java_path_lineEdit.text(), self.game_path_lineEdit.text()))
        self.java_select.clicked.connect(self.get_java_path)
        self.game_select.clicked.connect(self.get_game_path)
        self.quit_btn.clicked.connect(exit)

    def load(self) -> None:
        # self.java_select.setIcon(QIcon("./assets/folder.svg"))
        # self.game_select.setIcon(QIcon("./assets/folder.svg"))
        self.java_path_lineEdit.setText(self.config.get("java_path"))
        self.game_path_lineEdit.setText(self.config.get("game_dir"))
        self.get_version_list()

    def set_sidebar(self) -> None:
        self.stackedWidget.setCurrentIndex(0)
        self.home_btn.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0))
        self.core_btn.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(1))
        self.user_btn.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(2))
        self.toolButton_4.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(3))
        self.setting_btn.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(4))

    def get_game_path(self) -> None:
        game_dir = QFileDialog.getExistingDirectory(
            self, "选择游戏根目录", r"C:\\")
        if game_dir:  # 防止点取消后清空
            self.java_path_lineEdit.setText(game_dir)
            self.config.save("game_dir", game_dir)
            self.game_path_lineEdit.setText(self.config.get("game_dir"))

    def get_java_path(self) -> None:
        java_path, _ = QFileDialog.getOpenFileName(
            self, "", r"C:\\", "Java (java.exe)")
        if java_path:  # 防止点取消后清空
            self.java_path_lineEdit.setText(java_path)
            self.config.save("java_path", java_path)
            self.java_path_lineEdit.setText(self.config.get("java_path"))

    def get_version_list(self) -> None:
        for i in scandir("./.minecraft/versions"):
            if i.is_dir():
                self.comboBox.addItem(i.name)


if __name__ == '__main__':
    app = QApplication([])
    main = Launcher()
    main.show()
    app.exec()
