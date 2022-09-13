import tkinter as tk
import random as rand
import re

from tkinter import messagebox as mbox
from tkinter import filedialog as fdlg

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Лабораторная работа 10")
        self.geometry("800x600")   
        
        self.__create_menu()
        
        self.listbox = tk.Listbox(width=50)
        self.listbox.pack(side=tk.LEFT, anchor=tk.NW)
                
    def __create_menu(self):
        lables = [
            "Повторяющиеся слова"
        ]
        
        commands = [
            self.__task20
        ]
        
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        for l, c in zip(lables, commands):
            menubar.add_cascade(label=l, command=c)

    def __task20(self):
        file = open(App.__onOpen())
        text = file.read()
        
        result = App.__find_double_words(text)
        
        for i in range(len(result)):
             self.listbox.insert(tk.END, f"Слово: {result[i][0]} Строка: {result[i][3]}")
      
        # добавляет двойные слова в текст и разбивает его на строки
        # open(file.name, 'w').write(App.split_on_lines(App.double_words(text)))
   
    @staticmethod
    def __find_double_words(text):
        result = []
        
        l = re.split(" ", text)
        
        char_count = 0
        word_count = 0
        line_count = 0
        
        print(l)
        
        for i in range(1, len(l)):       
            if l[i] == l[i - 1]:
                result.append((l[i], char_count, word_count, line_count))
            for j in range(len(l[i])): 
                if l[i][j] == '\n': 
                    line_count += 1
                
            if(l[i][0].isalpha()):
                word_count += 1
                
            char_count += len(l[i]) + 1
            
        return result
 
            
    @staticmethod
    def __split_on_lines(text):
        l = list(text)
        _rand = None
        count = 0
            
        for i in range(len(l)):
            if l[i] == ' ': count += 1
            if _rand == None: _rand = rand.randint(20, 30)
            if _rand == count:
                l[i] = "\n"
                _rand = None
                count = 0
        
        return "".join(l)
    
    @staticmethod
    def __double_words(text):
        l = re.split("\s", text)
        
        _rand = None
        count = 0
            
        for i in range(len(l)):
            if l[i].isalpha(): count += 1
            if _rand == None: _rand = rand.randint(20, 30)
            if _rand == count:
                l.insert(i, l[i])
                _rand = None
                count = 0
        
        return " ".join(l)  
        
    @staticmethod
    def __onOpen():
        ftypes = [('Текстовые файлы', '*.txt'), ('Все файлы', '*')]
        dlg = fdlg.Open(filetypes = ftypes)
        return dlg.show()

if __name__ == "__main__":
    app = App()
    app.mainloop()

