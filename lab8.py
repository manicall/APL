import tkinter as tk
from tkinter import messagebox as mbox

class App(tk.Tk):
    def __init__(self):
        super().__init__()  
        self.title("Лабораторная работа 8 (задание 8)")
        self.geometry("800x600")   
        
        self.create_menu()
        
        tk.Label(text="Первая строка").grid()
        self.entry1 = tk.Entry()
        self.entry1.grid(row=0, column=1)
        
        tk.Label(text="Вторая строка").grid()
        self.entry2 = tk.Entry()
        self.entry2.grid(row=1, column=1)
         
    def create_menu(self):
        main_menu = tk.Menu()
        
        lables = [
            "Проверить анаграммы"
        ]
        
        commands = [
            self.check_anagram
        ]
        
        for l, c in zip(lables, commands):
            main_menu.add_cascade(label=l, command=c)

        self.config(menu=main_menu)

    def check_anagram(self):
        '''выводит результат проверки на анаграммы в диалоговое окно'''
        positive = "Данные строки являются аннограммами"
        negative = "Данные строки не являются аннограммами"
        
        if App.is_anagram(self.entry1.get(), self.entry2.get()):
            mbox.showinfo("Ответ", positive)
        else:
            mbox.showinfo("Ответ", negative)

    @staticmethod
    def is_anagram(str1, str2):
        '''проверяет являются ли введенные строки анаграммами'''
        if len(str1) != len(str2): return False
        
        # преобразование строк словарь
        dictionary = dict(zip(list(str1), list(str2)))
        
        # проверка, что второй список содержит все символы первого списка
        for key in dictionary:
            if not App.is_contain(key, list(dictionary.values())):
                return False
            
        return True

    @staticmethod
    # поиск символа char в списке list
    def is_contain(char, list):
        for i in list:
            if char == i: return True
        return False

if __name__ == "__main__":
    app = App()
    app.mainloop()
