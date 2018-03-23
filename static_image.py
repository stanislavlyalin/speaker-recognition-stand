# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

class StaticImage(QLabel):
    def __init__(self, path):
        super().__init__()
        self.setPixmap(QPixmap(path))
