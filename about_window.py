# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon
from static_image import StaticImage


# форма с информацией об устройстве системы
class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Как это работает?')
        self.setWindowIcon(QIcon('Voice-Search.ico'))
        self.vBox = QVBoxLayout()
        self.setLayout(self.vBox)
        self.vBox.addWidget(StaticImage('about.png'))
