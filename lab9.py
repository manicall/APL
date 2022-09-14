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
        
        self.__create_menu()
        
        frame = tk.Frame(self)
        frame.pack(side=tk.LEFT, anchor=tk.NW)
        
        now = datetime.now()
        
        self.calendar = tkc.Calendar(
            frame, 
            selectmode="day", 
            year=now.year, 
            month=now.month,
            day=now.day)
        
        self.calendar.pack(side=tk.LEFT)
        
        self.thread_resume = False
        self.thread = Thread(target=self.interval_print, daemon=True)
        
        self.listbox = tk.Listbox(frame)
        self.listbox.pack(side=tk.LEFT, fill=tk.Y, padx=10)
                 
    def __create_menu(self):
        lables = [
            "Преобразовать дату в день года",
            "Узнать дату последнего вторника",
            "Вывести пять строк с интервалом 3 секунды",
            "Узнать информацию о последнем изменении файла"
        ]
        
        commands = [
            self.__task11,
            self.__task19,
            self.__task25,
            self.__task38,
        ]
        
        menubar = tk.Menu(self)
        self.config(menu=menubar)
 
        main_menu = tk.Menu(menubar)
        for l, c in zip(lables, commands):
            main_menu.add_command(label=l, command=c)
          
        menubar.add_cascade(label="Меню", menu=main_menu)
  
    def __task11(self):
        _date = App.__get_date(self.calendar.get_date())
        mbox.showinfo("День года", self.date_in_day(_date))
    
    @staticmethod
    def __get_date(str_date):
        split = str_date.split(".")
        return date(int(split[2]), int(split[1]), int(split[0]))
    
    @staticmethod
    def date_in_day(u_date):
        print(f"\n\n{u_date}\n\n")
        return (u_date - date(u_date.year, 1, 1)).days + 1  
            
    def __task19(self):
        _date = App.__get_date(self.calendar.get_date())
        mbox.showinfo("Дата последнего вторника", self.last_tuesday(_date))
        pass 
    
    @staticmethod
    def last_tuesday(u_date):
        u_date = date(u_date.year, u_date.month, monthrange(u_date.year, u_date.month)[1])
        
        while u_date.weekday() != 1:
            u_date = u_date - timedelta(days=1)
        
        return u_date
    
    def __task25(self):
        if not self.thread.is_alive(): 
            self.thread.start()
            self.thread_resume = True
        elif self.thread_resume == False:
            self.thread_resume = True  
    
    def interval_print(self):
        while True:
            if self.thread_resume == True:
                self.listbox.delete(0, tk.END)

                self.listbox.insert(tk.END, [self.calendar.get_date()])
                for i in range(4):
                    App.__stay_interval()
                    self.listbox.insert(tk.END, [self.calendar.get_date()])
                
                self.thread_resume = False
                  
    @staticmethod
    def __stay_interval():
        saved = datetime.now()    
        while (datetime.now() - saved).seconds < 3:
            pass
        
    def __task38(self):
        locale.setlocale(locale.LC_ALL, 'Russian_Russia.1251')
        format = "%a, %d %b %Y %H:%M:%S" # строка для нужного форматирования

        local_time = time.localtime(os.path.getmtime(self.onOpen()))
        
        mbox.showinfo("информация о последнем изменении файла", 
                      time.strftime(format, local_time))

    @staticmethod
    def onOpen():
        ftypes = [('Python файлы', '*.py'), ('Все файлы', '*')]
        dlg = fdlg.Open(filetypes = ftypes)
        return dlg.show()

if __name__ == "__main__":
    app = App()
    app.mainloop()
