import tkinter as tk
import random as rand
import sys, argparse, re

from tkinter import messagebox as mbox
from tkinter import filedialog as fdlg

# возвращает объект, из которого можно извлечь название файла,
# переданного в командной строке
def get_namespace():
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser()
        parser.add_argument("-f1", "--file1", type=open)
        parser.add_argument("-f2", "--file2", type=open)
        
        try:
            return parser.parse_args(sys.argv[1:])
        except:
            print("файл не найден")

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
            "проверка орфографии",
            "Повторяющиеся слова"
        ]
        
        commands = [
            self.__task19,
            self.__task20
        ]
        
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        for l, c in zip(lables, commands):
            menubar.add_cascade(label=l, command=c)

    def __task19(self):
        namespace = get_namespace()
        if namespace != None and namespace.file1 != None:
            text1 = namespace.file1.read()
        else:
            text1 = open(App.__onOpen()).read()
            
        text2 = open("словарь.txt").read()
    
        splited = text2.split(" ")
        dictionary = dict(zip(splited, [0 for i in range(len(splited))]))
    
        text_list = App.__get_only_alnum_list(text1)
        
        # выводит результат в listbox
        self.listbox.delete(0, tk.END)
        for word in enumerate(text_list):
            if word[1] not in dictionary:
                self.listbox.insert(tk.END, f"Слово: {word[1]} Номер в тексте: {word[0]}")
    
    # создает словарь из заданного текста
    @staticmethod
    def __create_dictionary(text):
        # устранение дубликатов в тексте
        dictionary = " ".join(set(App.__get_only_alnum_list(text)))
        return dictionary

    # создает список слов в нижнем регистре из заданного текста
    @staticmethod
    def __get_only_alnum_list(text):
        # приведение символов к нижнему регистру
        l = ['']

        for i in range(len(text)):
            # если встретилась буква цифра или дефис
            if text[i].isalnum() or text[i] == '-': 
                # добавляем ее в посленюю строку в списке в нижнем регистре
                l[-1] += text[i].lower()
            # если встретился пробельный символ
            elif re.match("\s", text[i]) != None:
                if l[-1] != '': 
                    l.append('')
        
        return l

    def __task20(self):
        namespace = get_namespace()
        if namespace != None and namespace.file2 != None:
            text = namespace.file2.read()
        else:
            text = open(App.__onOpen()).read()
        
        result = App.__find_double_words(text)
        
        self.listbox.delete(0, tk.END)
        for i in range(len(result)):
             self.listbox.insert(tk.END, f"Слово: {result[i][0]} Строка: {result[i][1]}")
        
        # добавляет двойные слова в текст и разбивает его на строки
        # open(file.name, 'w').write(App.split_on_lines(App.double_words(text)))
    
    @staticmethod
    def __find_double_words(text):
        result = []     
        line_count = 0

        splited = ['']

        # разделение слов без удаления переноса сроки
        for i in range(len(text)):    
            if text[i] == ' ':
                if splited[-1] != '':
                    splited.append('')
            elif text[i] == '\n':
                splited.append('\n')
                splited.append('')
            elif text[i].isalnum():
                splited[-1] += text[i]    

        for i in range(1, len(splited)):
            # если данное слово оказалось равным предыдущему (с проверкой, 
            # что между словами может стоять перенос строки),
            # то запоминаем слово, и строку в которой оно было найдено        
            if splited[i - 1] == '\n' and splited[i] == splited[i - 2] or splited[i] == splited[i - 1]:
                result.append((splited[i], line_count))     
            if splited[i] == '\n': 
                line_count += 1
            
        return result
            
    # расставляет по тексту переносы строки в случайных местах
    @staticmethod
    def __split_on_lines(text):
        l = list(text)
        rnd = None
        count = 0
            
        for i in range(len(l)):
            if l[i] == ' ': count += 1
            if rnd == None: rnd = rand.randint(20, 30)
            if rnd == count:
                l[i] = "\n"
                rnd = None
                count = 0
        
        return "".join(l)
    
    # создает двойные слова в случайных местах
    @staticmethod
    def __double_words(text):
        l = re.split("\s", text)
        
        rnd = None
        count = 0
            
        for i in range(len(l)):
            if l[i].isalpha(): count += 1
            if rnd == None: rnd = rand.randint(20, 30)
            if rnd == count:
                l.insert(i, l[i])
                rnd = None
                count = 0
        
        return " ".join(l)  
    
    @staticmethod
    def __onOpen():
        ftypes = [('Текстовые файлы', '*.txt')]
        dlg = fdlg.Open(filetypes = ftypes)
        return dlg.show()

if __name__ == "__main__":
    app = App()
    app.mainloop()
