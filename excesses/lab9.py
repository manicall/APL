import tkinter as tk
import tkcalendar as tkc
import os.path, time, locale

from calendar import monthrange
from datetime import datetime, date, timedelta
from threading import Thread
from tkinter import messagebox as mbox
from tkinter import filedialog as fdlg

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Лабораторная работа 9")
        self.geometry("800x600")   
        
        self.create_menu()
        
        frame = tk.Frame(self)
        frame.pack(side=tk.LEFT, anchor=tk.NW)
        
        now = datetime.now()
        
        # календарь для вывода даты
        self.calendar = tkc.Calendar(
            frame, 
            selectmode="day", 
            year=now.year, 
            month=now.month,
            day=now.day)
        
        self.calendar.pack(side=tk.LEFT)
        
        # поток, который выводит 5 строк в listbox
        self.thread_resume = False
        self.thread = Thread(target=self.interval_print, daemon=True)
        
        # для вывода 5 строк
        self.listbox = tk.Listbox(frame)
        self.listbox.pack(side=tk.LEFT, fill=tk.Y, padx=10)
                 
    def create_menu(self):
        lables = [
            "Преобразовать дату в день года",
            "Узнать дату последнего вторника",
            "Вывести пять строк с интервалом 3 секунды",
            "Узнать информацию о последнем изменении файла"
        ]
        
        commands = [
            self.task11,
            self.task19,
            self.task25,
            self.task38,
        ]
        
        menubar = tk.Menu(self)
        self.config(menu=menubar)
 
        main_menu = tk.Menu(menubar)
        for l, c in zip(lables, commands):
            main_menu.add_command(label=l, command=c)
          
        menubar.add_cascade(label="Меню", menu=main_menu)
  
    def task11(self):
        '''выводит результат функции date_in_day в диалоговое окно'''
        u_date = App.get_date(self.calendar.get_date())
        mbox.showinfo("День года", self.date_in_day(u_date))
    
    @staticmethod
    def get_date(str_date):
        '''возвращает date на основе даты представленной строкой'''
        split = str_date.split(".")
        return date(int(split[2]), int(split[1]), int(split[0]))
    
    @staticmethod
    def date_in_day(u_date):
        '''преобразует дату в день года'''
        print(f"\n\n{u_date}\n\n")
        return (u_date - date(u_date.year, 1, 1)).days + 1  
            
    def task19(self):
        '''выводит результат функции last_tuesday в диалоговое окно'''
        u_date = App.get_date(self.calendar.get_date())
        mbox.showinfo("Дата последнего вторника", self.last_tuesday(u_date))
        pass 
    
    @staticmethod
    def last_tuesday(u_date):
        '''рассчитывает дату последнего вторника в заданном месяце'''
        u_date = date(u_date.year, u_date.month, monthrange(u_date.year, u_date.month)[1])
        
        while u_date.weekday() != 1:
            u_date = u_date - timedelta(days=1)
        
        return u_date
    
    def task25(self):
        '''запускает поток, который выводит 5 строк в listbox'''
        if not self.thread.is_alive(): 
            self.thread.start()
            self.thread_resume = True
        elif self.thread_resume == False:
            self.thread_resume = True  
    
    def interval_print(self):
        '''вывод 5 строк с интервалов 3 секунды'''
        while True:
            if self.thread_resume == True:
                self.listbox.delete(0, tk.END)

                self.listbox.insert(tk.END, self.calendar.get_date())
                for i in range(4):
                    App.stay_interval()
                    self.listbox.insert(tk.END, self.calendar.get_date())
                
                self.thread_resume = False
                  
    @staticmethod
    def stay_interval():
        '''ожидание трех секунд'''
        saved = datetime.now()    
        while (datetime.now() - saved).seconds < 3:
            pass
        
    def task38(self):
        '''выводит информацию о последнем изме файла'''
        locale.setlocale(locale.LC_ALL, 'Russian_Russia.1251')
        format = "%a, %d %b %Y %H:%M:%S" # строка для нужного форматирования

        file_name = self.on_open()
        if file_name != '':
            local_time = time.localtime(os.path.getmtime(file_name))
            
            mbox.showinfo("информация о последнем изменении файла", 
                        time.strftime(format, local_time))
        
    @staticmethod
    def on_open():
        '''открывает диалоговое окно для выбора файла на компьтере'''
        ftypes = [('Python файлы', '*.py'), ('Все файлы', '*')]
        dlg = fdlg.Open(filetypes = ftypes)
        return dlg.show()

if __name__ == "__main__":
    app = App()
    app.mainloop()
