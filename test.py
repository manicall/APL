#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets 

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Draw text')
        
        self.field = Field()
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.field)
            
        for i in range(10):
            self.field.create_image(i * 10, 0)
    
        self.setLayout(vbox)
        self.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    
    sys.exit(app.exec_())