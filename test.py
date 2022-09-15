#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

        self.x = 0
        self.y = 0

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Draw text')
        self.show()

    def create_image(self, x, y):
        self.x = x
        self.y = y
        
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawPixmap(event, qp, self.x, self.y)
        qp.end()
        
    def drawPixmap(self, event, qp, x, y):
        p = QPixmap('ic_bug.png')
        p = p.scaled(50, 50)
        qp.drawPixmap(x, y, p)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    
    for i in range(10):
        ex.create_image(i * 10, 0)
    
    sys.exit(app.exec_())