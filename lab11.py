from colour import Color
from tkinter import messagebox as mbox

import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Лабораторная работа 11")
        
        self.width = 600
        self.height = 600
        
        self.geometry(f"{self.width}x{self.height}")
        self.count = None
        
        self.create_menu()
        
        f = tk.Frame(self)
        f.pack(fill="both", expand=True)
        
        self.canvas = tk.Canvas(f)
        self.canvas.pack(fill="both", expand=True)
       
    def create_menu(self):
        main_menu = tk.Menu()
        
        lables = [
            "Ввести число"
        ]
        
        commands = [
            self.create_rounds
        ]
        
        for l, c in zip(lables, commands):
            main_menu.add_cascade(label=l, command=c)

        self.config(menu=main_menu)
    
    def create_rounds(self):
        '''функция создающая круги, заданного количества'''
        self.create_window()
        try:
            count = int(self.count)
        except ValueError:
            mbox.showerror("Ошибка преобразования", 
                           "Неудалось привести введеное значение к числу")
            return # выход из функции
        
        self.canvas.delete("all")   
        # список содержащий цвета от синего до желтого
        colors = list(Color("blue").range_to(Color("yellow"), count))
        
        # извлечение ширины и высоты окна
        size = self.geometry().split('+')[0].split('x')
        size[0], size[1] = int(size[0]), int(size[1])
        
        interval = 8
        
        xoffset = size[0] / 2 
        yoffset = size[1] / 2 

        def get_x(i):
            nonlocal xoffset, interval
            return xoffset + i * interval
        
        def get_y(i):
            nonlocal yoffset, interval
            return yoffset + i * interval

        for i in range(count, 0, -1):
            self.canvas.create_oval(get_x(-i), get_y(-i), get_x(i), get_y(i), 
                                    outline="#000", fill=colors[i - 1], width=1)
        
    def create_window(self):
        '''создание диалогового окна для ввода'''
        window = tk.Tk()
        window.title="Ввод числа"
        window.geometry("200x100")
        
        frame = tk.Frame(window)
        frame.pack(fill="both", expand=True)
        
        e = tk.Entry(frame)
        e.pack(fill="both", expand=True)

        e.focus_set()

        def callback():
            nonlocal window, e, self
            
            # ! значение извлекаемое из поля для ввода
            self.count = e.get()
            window.destroy()

        b = tk.Button(frame, text="OK", width=10, command=callback)
        b.pack()
        
        window.wait_window()
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
