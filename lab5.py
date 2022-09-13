from lab1 import Task16, Task21
import tkinter as tk
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Лабораторная работа 5")
                
        self.group_1 = tk.LabelFrame(self, padx=15, pady=10, text="Задание 16")
        self.group_1.grid(sticky=tk.N)
        self.radius = tk.StringVar()
        self.task16_out_ra = tk.StringVar()
        self.task16_out_bv = tk.StringVar()

        tk.Label(self.group_1, text="Радиус").grid(sticky=tk.W)
        tk.Entry(self.group_1, textvariable=self.radius).grid(sticky=tk.W)
        tk.Label(self.group_1, textvariable=self.task16_out_ra).grid(sticky=tk.W)
        tk.Label(self.group_1, textvariable=self.task16_out_bv).grid(sticky=tk.W)
        tk.Button(self.group_1, text="Рассчитать", command=self.on_calc_task16).grid(pady=10, sticky=tk.E)      
        
        self.group_2 = tk.LabelFrame(self, padx=15, pady=10, text="Задание 21")
        self.group_2.grid(row=0, column=1)
        self.base = tk.StringVar()
        self.height = tk.StringVar()
        self.task21_out_ta = tk.StringVar()
        
        tk.Label(self.group_2, text="Основание").grid(sticky=tk.W)
        tk.Entry(self.group_2, textvariable=self.base).grid(sticky=tk.W)      
        tk.Label(self.group_2, text="Высота").grid(sticky=tk.W)
        tk.Entry(self.group_2, textvariable=self.height).grid(sticky=tk.W)
        tk.Label(self.group_2, textvariable=self.task21_out_ta).grid(sticky=tk.W)
        tk.Button(self.group_2, text="Рассчитать", command=self.on_calc_task21).grid(pady=10, sticky=tk.E)     
         
    def on_calc_task16(self):
        radius = None
        
        def valid():
            nonlocal radius
            try:
                radius = float(self.radius.get())
                if (radius <= 0): return False
            except ValueError:
                return False
            
            return True
        
        if not valid(): 
            self.task16_out_ra.set(f"Ожидалось число больше нуля")
            self.task16_out_bv.set("")
        else:
            self.task16_out_ra.set(f"Площадь круга: {Task16.round_area(radius)}")
            self.task16_out_bv.set(f"Объем шара: {Task16.ball_volume(radius)}")
        
    def on_calc_task21(self):
        base = None
        height = None
        
        def valid():
            nonlocal base, height
            
            try:
                base = float(self.base.get())
                height = float(self.height.get())
                if (base <= 0 or height <= 0): return False
            except ValueError:
                return False
            
            return True
     
        if not valid():
            self.task21_out_ta.set(f"Ожидалось число больше нуля")
        else:
            self.task21_out_ta.set(f"Площадь треугольника: {Task21.triangle_area(base, height)}")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
