from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class App(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window = Window(self)
        self.window.show()

class Window(QtWidgets.QWidget):    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("букашка управляемая слайдерами")
        self.resize(300, 200)

        self.vSlider = QtWidgets.QSlider()
        self.hSlider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        
        self.vSlider.setInvertedAppearance(True)
        
        self.vSlider.valueChanged.connect(self.on_vSliderValueChanged)
        self.hSlider.valueChanged.connect(self.on_hSliderValueChanged)
        
        self.field = Field()
        
        self.hSlider.setRange(0, self.field.size().width() - 50)
        self.vSlider.setRange(0, self.field.size().height() - 50)

        main_layout = QtWidgets.QHBoxLayout()  
        left_vBox = QtWidgets.QVBoxLayout()
        left_vBox.addWidget(self.vSlider)
        
        right_vBox = QtWidgets.QVBoxLayout()
        right_vBox.addWidget(self.field)
        right_vBox.addWidget(self.hSlider)
               
        main_layout.addLayout(left_vBox)
        main_layout.addLayout(right_vBox)

        self.setLayout(main_layout)
        
    def resizeEvent(self, event):
        self.set_sliders_range()
        return super(Window, self).resizeEvent(event)
    
    def set_sliders_range(self):
        self.hSlider.setMaximum(self.field.size().width() - self.field.image_size.width())
        self.vSlider.setMaximum(self.field.size().height() - self.field.image_size.height())
        
    def on_hSliderValueChanged(self):
        self.field.create_image(self.hSlider.value(), self.field.y)
        
    def on_vSliderValueChanged(self):
        self.field.create_image(self.field.x, self.vSlider.value())
        
class Field(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        
        self.direction = "right"
        
        self.image_size = QtCore.QSize(50, 50)
        
        self.pix = QtGui.QPixmap('ic_bug.png')
        self.pix = self.pix.scaled(self.image_size.width(), 
                                   self.image_size.height())  
    
    def create_image(self, x, y):
        self.set_direction(x, y)
        
        self.x = x
        self.y = y
        
        # вызов paintEvent
        self.update()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw_pixmap(qp, self.x, self.y)
        qp.end()
        
    def draw_pixmap(self, qp, x, y):   
        transform = QtGui.QTransform()
        transform.rotate(self.get_degree())
        
        pt = self.pix.transformed(transform)
        qp.drawPixmap(x, y, pt)
        
    def get_degree(self):
        if (self.direction == "right"): return 0
        if (self.direction == "left"): return 180
        if (self.direction == "up"): return 90
        if (self.direction == "down"): return 270
        
    def set_direction(self, x, y):
        if (x > self.x): self.direction = "right"
        if (x < self.x): self.direction = "left"
        if (y > self.y): self.direction = "up"
        if (y < self.y): self.direction = "down"  

if __name__ == "__main__":
    app = App()
    sys.exit(app.exec())