import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from scipy.optimize import linprog	

class Solver:
    @classmethod
    def scipy_solve(self):
        '''решает задачу оптимизации'''
        model = self.model
        
        try:
            c = model.get_c()
            A_ub = model.A_ub
            b_ub = model.get_b_ub()
            A_eq = model.A_eq
            b_eq = model.get_b_eq()
        except ValueError:
            mbox = QtWidgets.QMessageBox("Некоректные данные")
            mbox.setText()
            mbox.exec()
            return          
        
        solution = linprog(c, A_ub, b_ub, A_eq, b_eq)
       
        mbox = QtWidgets.QMessageBox()  
        text = ""
        try:
            for i in enumerate(solution['x']):
                text += f"x{i[0]} = {(i[1])}\n"
            # оптимальное (минимальное) значение функции
            text += "\nF = " + str(solution['fun'])
            mbox.setText(text)
        except:
            mbox.setText(solution.message)
        mbox.exec()

    @classmethod
    def set_model(self, model):
        self.model = model

class App(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window = Window()
        self.window.show()

class Window(QtWidgets.QMainWindow):    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Решение оптимизационной задачи")
        self.resize(600, 300)
        
        table_view = TableView()
        Solver.set_model(table_view.get_model())
        
        menu_bar = self.menuBar()
        menu_bar.addAction("SciPy оптимизация", Solver.scipy_solve)

        self.setCentralWidget(table_view) 

class TableView(QtWidgets.QTableView):
    def __init__(self):
        super().__init__()
        
        self.model = Model()
        self.setModel(self.model)
        
        # установка границ для заголовков
        self.horizontalHeader().setStyleSheet(self.get_header_style())       
        self.verticalHeader().setStyleSheet(self.get_header_style())
    
    def get_header_style(self): 
        return '''
        QHeaderView::section {
            border: none;
            border-bottom: 1px solid gray;
            border-right: 1px solid gray;
            background-color: white;
        } '''
    
    def get_model(self): return self.model
    
class Model(QtGui.QStandardItemModel):
    def __init__(self):
        super().__init__()
        # Коэффициенты линейной целевой функции
        self.c = [40, 110, 190, 170, 100, 150]

        # коэффициенты при переменных для условий в виде неравенств
        self.A_ub = [[1,1,1,0,0,0],
                    [0,0,0,1,1,1]]

        # вектор ограничения неравенства
        self.b_ub = [1000, 1500] 

        # содержит коэффициенты при переменных для условий в виде равенств
        self.A_eq = [[1,0,0,1,0,0],
                    [0,1,0,0,1,0],
                    [0,0,1,0,0,1]]
        
        # вектор ограничения равенства
        self.b_eq = [400,600,300] 
        
        self.setHorizontalHeaderLabels(['УШУ', 'КИЯ', 'ОС', 'Запасы'])
        self.setVerticalHeaderLabels(['ЗИМБО', 'БУМБО', 'Потребности'])
        
        self.fill_c()
        self.fill_ub()
        self.fill_b_eq()
        
    def fill_c(self):
        '''заполняет таблицу значениями коэффициентов целевой функции'''
        j = 0
        for i in range(len(self.b_ub)):
            for k in range(len(self.b_eq)):
                self.setItem(i, k, QtGui.QStandardItem(str(self.c[j])))
                j += 1
                
    def fill_ub(self):
        '''заполняет таблицу значениями вектора ограничения неравенства'''
        for i in enumerate(self.b_ub):
            item = QtGui.QStandardItem(str(i[1]))
            self.setItem(i[0], self.columnCount() - 1, item)
                    
    def fill_b_eq(self):
        '''заполняет таблицу значениями вектора ограничения равенства'''
        for i in enumerate(self.b_eq):
            item = QtGui.QStandardItem(str(i[1]))
            self.setItem(self.rowCount() - 1, i[0], item)
            
    def get_c(self):
        '''возвращает список со значениями коэффициентов целевой функции'''
        c = []
        for i in range(len(self.b_ub)):
            for k in range(len(self.b_eq)):
                c.append(int(self.item(i, k).text()))
                
        return c

    def get_b_ub(self):
        '''возвращает список со значениями вектора ограничения неравенства'''
        b_ub = []
        for i in enumerate(self.b_ub):
            b_ub.append(int(self.item(i[0], self.columnCount() - 1).text()))
        return b_ub
    
    def get_b_eq(self):
        '''возвращает список со значениями вектора ограничения равенства'''
        b_eq = []
        for i in enumerate(self.b_eq):
            b_eq.append(int(self.item(self.rowCount() - 1, i[0]).text()))
        return b_eq
    
if __name__ == "__main__":
    app = App()
    sys.exit(app.exec())