# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from static_image import StaticImage
from signup_window import SignUpWindow
from identify_window import IdentifyWindow
from about_window import AboutWindow

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