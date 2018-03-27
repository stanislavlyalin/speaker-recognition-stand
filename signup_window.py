# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5 import QtCore
from phrases import randomPhrase
from users import write, nextId

ENABLED_STYLE = 'color: green; border: 1px solid green; border-radius: 5px'
DISABLED_STYLE = 'color: grey; border: 1px solid grey; border-radius: 5px'

# форма добавления нового пользователя
class SignUpWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Зарегистрироваться в системе')
        self.attempts = 0

        self.vBox = QVBoxLayout()
        self.attemptsBox = QHBoxLayout()
        self.buttonsBox = QHBoxLayout()
        self.readyBox = QHBoxLayout()
        self.setLayout(self.vBox)

        # создание компонентов
        self.userName = QLineEdit('Ваше имя')
        self.attemptLabels = [QLabel(str(i+1)) for i in range(3)]
        self.startButton = QPushButton('Старт')
        self.stopButton = QPushButton('Стоп')
        self.stopButton.setEnabled(False)
        self.textToSpeech = QLabel('Текст для произнесения')
        self.readyButton = QPushButton('Готово')

        # расположение компонентов на форме
        self.vBox.addWidget(QLabel('Представьтесь'))
        self.vBox.addWidget(self.userName)
        self.vBox.addWidget(QLabel('Запишите 3 фрагмента речи'))
        for i in range(3):
            self.attemptLabels[i].setStyleSheet(DISABLED_STYLE)
            self.attemptLabels[i].setAlignment(QtCore.Qt.AlignCenter)
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

        # connect
        self.startButton.clicked.connect(lambda: self.startButtonClicked())
        self.stopButton.clicked.connect(lambda: self.stopButtonClicked())
        self.readyButton.clicked.connect(lambda: self.readyButtonClicked())

    def showEvent(self, event):
        self.reset()
        self.textToSpeech.setText(randomPhrase())

    def startButtonClicked(self):
        self.stopButton.setEnabled(True)
        self.startButton.setEnabled(False)

    def stopButtonClicked(self):
        self.attemptLabels[self.attempts].setStyleSheet(ENABLED_STYLE)
        self.attempts += 1
        self.stopButton.setEnabled(False)
        self.startButton.setEnabled(True if self.attempts < 3 else False)
        self.readyButton.setEnabled(self.attempts >= 3)
        self.textToSpeech.setText(randomPhrase())
        print(nextId())

    def readyButtonClicked(self):
        write(nextId(), self.userName.text())

    def reset(self):
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.readyButton.setEnabled(False)
        self.attempts = 0
        for i in range(3):
            self.attemptLabels[i].setStyleSheet(DISABLED_STYLE)
