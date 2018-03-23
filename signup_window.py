# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5 import QtCore
from phrases import randomPhrase

# форма добавления нового пользователя
class SignUpWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Зарегистрироваться в системе')

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

    def showEvent(self, event):
        self.textToSpeech.setText(randomPhrase())
