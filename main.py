# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit, QSpacerItem
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

class StaticImage(QLabel):
    def __init__(self, path):
        super().__init__()
        self.setPixmap(QPixmap(path))


# форма добавления нового пользователя
class SignUpWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.vBox = QVBoxLayout()
        self.attemptsBox = QHBoxLayout()
        self.buttonsBox = QHBoxLayout()
        self.readyBox = QHBoxLayout()
        self.setLayout(self.vBox)

        # создание компонентов
        self.attemptLabels = [QLabel(str(i+1)) for i in range(3)]
        self.startButton = QPushButton('Старт')
        self.stopButton = QPushButton('Стоп')
        self.textToSpeech = QLabel('Текст для произнесения')
        self.readyButton = QPushButton('Готово')

        # расположение компонентов на форме
        self.vBox.addWidget(QLabel('Представьтесь'))
        self.vBox.addWidget(QLineEdit('Ваше имя'))
        self.vBox.addWidget(QLabel('Запишите 3 фрагмента речи'))
        for i in range(3):
            self.attemptLabels[i].setStyleSheet('color: grey; border: 1px solid grey; border-radius: 5px')
            self.attemptLabels[i].setAlignment(QtCore.Qt.AlignCenter)
            self.attemptLabels[i].setEnabled(False)
            self.attemptsBox.addWidget(self.attemptLabels[i])
        self.vBox.addLayout(self.attemptsBox)
        self.vBox.addWidget(self.textToSpeech)

        self.buttonsBox.addStretch(1)
        self.buttonsBox.addWidget(self.startButton)
        self.buttonsBox.addWidget(self.stopButton)
        self.buttonsBox.addStretch(1)
        self.vBox.addLayout(self.buttonsBox)

        self.readyBox.addStretch(1)
        self.readyBox.addWidget(self.readyButton)
        self.vBox.addLayout(self.readyBox)


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
