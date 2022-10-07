from lab2 import Task19, Task20
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()    
        self.title("Лабораторная работа 6")
           
        # первая группа 
        self.group_1 = tk.LabelFrame(self, padx=15, pady=10, text="Задание 16")
        self.group_1.grid(sticky=tk.N)
        # входное значение
        self.num_mark = tk.StringVar()
        # выходное значение
        self.char_mark = tk.StringVar()

        # элементы для ввода входных данных
        tk.Label(self.group_1, text="Числовая оценка").grid(sticky=tk.W)
        tk.Entry(self.group_1, textvariable=self.num_mark).grid(sticky=tk.W)
        # надпись для вывода результата
        tk.Label(self.group_1, textvariable=self.char_mark).grid(sticky=tk.W)
        tk.Button(self.group_1, text="Рассчитать", 
                  command=self.on_calc_task20).grid(pady=10, sticky=tk.E)      
        
        # вторая группа
        self.group_2 = tk.LabelFrame(self, padx=15, pady=10, text="Задание 21")
        self.group_2.grid(row=0, column=1)
        # переменные для привязки к checkbox
        self.check_rate = tk.DoubleVar(value=0)
        # входное значение
        self.rate = tk.StringVar()
        self.result_value = tk.StringVar()
        
        tk.Radiobutton(self.group_2, text="рейтинг: 0",
                       variable=self.check_rate, value=0, 
                       command=self.change_entry_state).grid(sticky=tk.W)
        
        tk.Radiobutton(self.group_2, text="рейтинг: 0.4", 
                       variable=self.check_rate, value=0.4, 
                       command=self.change_entry_state).grid(sticky=tk.W)
        
        tk.Radiobutton(self.group_2, text="рейтинг: 0.6 и выше",
                       variable=self.check_rate, value=0.6, 
                       command=self.change_entry_state).grid(sticky=tk.W)
        
        # поле для ввода рейтинга, если он больше 0.6
        self.rate_entry = tk.Entry(self.group_2, 
                                   textvariable=self.rate, state=tk.DISABLED)
        self.rate_entry.grid(sticky=tk.W)
        
        # надпись для вывода результата
        tk.Label(self.group_2, textvariable=self.result_value, 
                 justify='left').grid(sticky=tk.W)
        
        tk.Button(self.group_2, text="Рассчитать", 
                  command=self.on_calc_task21).grid(pady=10, sticky=tk.E)     
         
    def on_calc_task20(self):
        num_mark = None
         # проверка, что числовая оценка задана правильно
        def valid():
            nonlocal num_mark
            try:
                num_mark = float(self.num_mark.get())
                if (num_mark <= 0): return False
            except ValueError:
                return False
            
            return True
        
        # вывод результата
        if not valid(): 
            self.char_mark.set("Ожидалось число больше нуля")
        else:
            self.char_mark.set(f"""Буквенная оценка:
                               {Task19.get_char_mark(num_mark)}""")
        
    def change_entry_state(self):
        if self.check_rate.get() == 0.6:
            self.rate_entry['state'] = tk.NORMAL
        else: 
            self.rate_entry['state'] = tk.DISABLED
    
    def on_calc_task21(self):
        '''расчитывает значение из таблицы 
        и прибавку к зарплате по заданному рейтингу'''
        rate = None
        # проверка, что рейтинг задан правильно
        def valid():
            nonlocal rate
            try:
                rate = float(self.rate.get())
                if (rate < 0.6): return False
            except ValueError:
                return False
            
            return True

        # вывод результата
        if self.check_rate.get() == 0.6:  
            if not valid(): 
                self.result_value.set("Ожидалось число не менее 0.6")
            else:
                value, increase = Task20.get_result(rate)
                self.result_value.set(f"""Значение: {value}\n
                                      Сумма прибавки сотрудника: {increase}""")
        else: 
            value, increase = Task20.get_result(self.check_rate.get())
            self.result_value.set(f"""Значение: {value}\n 
                                  Сумма прибавки сотрудника: {increase}""")        
            
if __name__ == "__main__":
    app = App()
    app.mainloop()