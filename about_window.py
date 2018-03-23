# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QVBoxLayout
from static_image import StaticImage

# форма с информацией об устройстве системы
class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.vBox = QVBoxLayout()
        self.setLayout(self.vBox)
        self.vBox.addWidget(StaticImage('about.png'))
        self.setWindowTitle('Как это работает?')
