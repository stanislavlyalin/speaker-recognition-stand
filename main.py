# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap

class StaticImage(QLabel):
    def __init__(self, path):
        super().__init__()
        self.setPixmap(QPixmap(path))


# форма добавления нового пользователя
class SignUpWindow(QDialog):
    def __init__(self):
        super().__init__()

# форма голосовой идентификации
class IdentifyWindow(QDialog):
    def __init__(self):
        super().__init__()

# форма с информацией об устройстве системы
class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.vBox = QVBoxLayout()
        self.setLayout(self.vBox)
        self.vBox.addWidget(StaticImage('about.png'))


# главное окно приложения
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.vBox = QVBoxLayout()
        self.buttonsBox = QHBoxLayout()
        self.setLayout(self.vBox)

        # создание компонентов
        self.usersText = QLabel('В системе 28 пользователей')
        self.signUpButton = QPushButton('Зарегистрироваться')
        self.identifyButton = QPushButton('Идентифицировать')
        self.aboutButton = QPushButton('Как это работает?')

        # создание форм
        self.signUpWindow = SignUpWindow()
        self.identifyWindow = IdentifyWindow()
        self.aboutWindow = AboutWindow()

        # добавление компоненов на форму
        self.vBox.addWidget(self.usersText)
        self.vBox.addWidget(StaticImage('users.png'))
        self.vBox.addLayout(self.buttonsBox)
        self.buttonsBox.addWidget(self.signUpButton)
        self.buttonsBox.addWidget(self.identifyButton)
        self.buttonsBox.addWidget(self.aboutButton)

        # связка кнопок с формами
        self.signUpButton.clicked.connect(self.signUpWindow.show)
        self.identifyButton.clicked.connect(self.identifyWindow.show)
        self.aboutButton.clicked.connect(self.aboutWindow.show)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
