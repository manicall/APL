from lab1 import Task16, Task21
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()        
        self.group_1 = tk.LabelFrame(self, padx=15, pady=10, text="Задание 16")
        self.group_1.grid(sticky=tk.N)
        self.radius = tk.StringVar()

        tk.Label(self.group_1, text="Радиус").grid(row=0, sticky=tk.W)
        tk.Entry(self.group_1, textvariable=self.radius).grid(row=1, sticky=tk.W)
        
        tk.Button(self.group_1, text="Рассчитать", command=self.on_calc_task16).grid(row=4, pady=10, sticky=tk.E)      
        
        self.group_2 = tk.LabelFrame(self, padx=15, pady=10, text="Задание 21")
        self.group_2.grid(row=0, column=1)
        self.base = tk.StringVar()
        self.height = tk.StringVar()
        
        tk.Label(self.group_2, text="Основание").grid(row=0, sticky=tk.W)
        tk.Entry(self.group_2, textvariable=self.base).grid(row=1, sticky=tk.W)      
        tk.Label(self.group_2, text="Высота").grid(row=2, sticky=tk.W)
        tk.Entry(self.group_2, textvariable=self.height).grid(row=3, sticky=tk.W)
        
        tk.Button(self.group_2, text="Рассчитать", command=self.on_calc_task21).grid(row=5, pady=10, sticky=tk.E)     
         
    def on_calc_task16(self):
        try:
            radius = float(self.radius.get())
            if (radius <= 0): return
        except ValueError:
            return
        
        tk.Label(self.group_1, text=f"Площадь круга: {Task16.round_area(radius)}").grid(row=2, sticky=tk.W)
        tk.Label(self.group_1, text=f"Объем шара: {Task16.ball_volume(radius)}").grid(row=3, sticky=tk.W)
        
    def on_calc_task21(self):
        try:
            base = float(self.base.get())
            height = float(self.height.get())
            if (base <= 0 or height <= 0): return
        except ValueError:
            return
        
        tk.Label(self.group_2, text=f"Площадь треугольника: {Task21.triangle_area(base, height)}").grid(row=4, sticky=tk.W)

if __name__ == "__main__":
    app = App()
    app.mainloop()