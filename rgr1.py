from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class App(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window = Window(self)
        self.window.show()
     
class Window(QtWidgets.QWidget):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Первая программа на PyQt")
        self.resize(300, 200)
        
        vSlider = QtWidgets.QSlider()
        hSlider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        
        label = QtWidgets.QLabel()


        pix = QtGui.QPixmap('ic_bug.png')
        
        pix = pix.scaled(QtCore.QSize(100, 100), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

        
        painter = QtGui.QPainter()

        painter.drawPixmap(100, 100, pix)

        

        main_layout = QtWidgets.QHBoxLayout()  
        left_vBox = QtWidgets.QVBoxLayout()
        left_vBox.addWidget(vSlider)
        
        right_vBox = QtWidgets.QVBoxLayout()
        right_vBox.addWidget(label)
        right_vBox.addWidget(hSlider)
               
        main_layout.addLayout(left_vBox)
        main_layout.addLayout(right_vBox)
        
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = App()
    sys.exit(app.exec())