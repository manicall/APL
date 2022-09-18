from PyQt5 import QtWidgets, QtCore, QtGui
import numpy as np
import sys

class App(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window = Window()
        self.window.show()

class Window(QtWidgets.QMainWindow):    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Решение СЛУ")
        self.widget = Widget()
        self.resize(self.widget.size())
        self.setMaximumSize(self.size())
        
        menu_bar = self.menuBar()
        menu_bar.addAction("Решение СЛУ", self.solve)

        self.setCentralWidget(self.widget) 

    def solve(self):   
        def get_result(x):
            message = "Ответ: "
            for i in range(len(x)):
                message += f"x{i + 1} = {round(x[i], 2)}, "
            return message[0:-2]
                
        try:
            x = np.linalg.solve(self.get_A(), self.get_b())
            # вывод результата
            QtWidgets.QMessageBox.information(self, "результат", get_result(x),
                            defaultButton=QtWidgets.QMessageBox.Ok)
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Ошибка преобразования",
                    "Текстовые поля содержат некорректные данные",
                    defaultButton=QtWidgets.QMessageBox.Ok)
    
    def get_A(self):
        A = []
        for row in self.widget.line_text_grid:
            A.append([])
            for i in range(len(row) - 1):
                A[-1].append(float(row[i].text()))
                
        return A
    
    def get_b(self):
        b = []
        for row in self.widget.line_text_grid:
            b.append(float(row[-1].text()))
            
        return b
        
class Widget(QtWidgets.QTabWidget): 
    def __init__(self):
        super().__init__()    
        A = np.array([[2, 3, 5], 
                      [3, 7, 4], 
                      [1, 2, 2]])

        b = np.array([10, 3, 3])
           
        def get_label_text():
            nonlocal A
            if j != len(A[i]) - 1:
                return "x" + str(j + 1) + " +"
            else:
                return "x" + str(j + 1) + " ="
            
        grid = QtWidgets.QGridLayout()
   
        # список текстовых полей
        self.line_text_grid = []
   
        for i in range(len(A)):
            self.line_text_grid.append([])
            for j in range(len(A[i])):
                label = QtWidgets.QLabel(get_label_text())
                # сохранение текстового поля в список
                self.line_text_grid[i].append(LineEdit(str(A[i][j])))  
                
                hbox = QtWidgets.QHBoxLayout()
                
                hbox.addWidget(self.line_text_grid[-1][-1])
                hbox.addWidget(label)
                                
                grid.addLayout(hbox, i, j)
            
            self.line_text_grid[i].append(LineEdit(str(b[i])))  
            grid.addWidget(self.line_text_grid[-1][-1], i, len(A[i]))
        
        self.setLayout(grid)
        self.setFixedSize(grid.columnCount() * 60, grid.rowCount() * 40)
        
class LineEdit(QtWidgets.QLineEdit):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(30, 25)
        self.setMaxLength(4)

if __name__ == "__main__":
    app = App()
    sys.exit(app.exec())