# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QPushButton

# форма голосовой идентификации
class IdentifyWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.vBox = QVBoxLayout()
        self.buttonsBox = QHBoxLayout()
        self.readyBox = QHBoxLayout()
        self.setLayout(self.vBox)
        self.setWindowTitle('Идентифицировать себя')

        # создание компонентов
        self.textToSpeech = QLabel('Текст для произнесения')
        self.startButton = QPushButton('Старт')
        self.stopButton = QPushButton('Стоп')
        self.userName = QLabel('Вы - Вася Пупкин')
        self.readyButton = QPushButton('Готово')

        # добавление компонентов на форму
        self.vBox.addWidget(QLabel('Произнесите фразу'))
        self.vBox.addWidget(self.textToSpeech)

        self.buttonsBox.addStretch(1)
        self.buttonsBox.addWidget(self.startButton)
        self.buttonsBox.addWidget(self.stopButton)
        self.buttonsBox.addStretch(1)
        self.vBox.addLayout(self.buttonsBox)

        self.vBox.addWidget(self.userName)

        self.readyBox.addStretch(1)
        self.readyBox.addWidget(self.readyButton)
        self.vBox.addLayout(self.readyBox)
