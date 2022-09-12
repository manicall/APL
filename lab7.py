from os import pardir
import tkinter as tk
import random as rand

class App(tk.Tk):
    def __init__(self):
        super().__init__()  
        self.title("Лабораторная работа 7")
        self.geometry("800x600")    
        
        self.deck = []
        
        self.__create_menu()
        self.__create_listboxes()
        self.expression = tk.StringVar()
        
        lframe = tk.LabelFrame(self, text="задание 21")
        lframe.pack(padx=5, pady=5, anchor=tk.NW)
        
        tk.Label(lframe, text="Выражение ").pack(side=tk.LEFT,  anchor=tk.NW)
        tk.Entry(lframe, textvariable=self.expression).pack(side=tk.LEFT, anchor=tk.NW)
        
        self.__listbox_expression = self.__create_listbox(lframe)
       
          
    def __create_menu(self):
        main_menu = tk.Menu()
        main_menu.add_cascade(label="Создать колоду", command=self.__create_deck)
        main_menu.add_cascade(label="Перетасовать колоду", command=self.__shuffle)

        self.config(menu=main_menu)
        
    def __create_listboxes(self):     
        lframe = tk.LabelFrame(self, text="Задание 16")
        lframe.pack(fill=tk.Y, padx=5, pady=5, side=tk.LEFT)
        
        self.__listbox_ordered = self.__create_listbox(lframe)  
        self.__listbox_shuffled = self.__create_listbox(lframe)      
        
    @staticmethod
    def __create_listbox(master):        
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        listbox = tk.Listbox(frame)
        listbox.pack(fill=tk.Y, side=tk.LEFT)
        
        scrollbar = tk.Scrollbar(frame, orient="vertical")
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        
        return listbox
        
    def __create_deck(self):
        """Создает колоду и выводит результат в listbox"""
        nominal = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K',  'A']
        # масть
        suit = ['s', 'h', 'd', 'c']
        # создание колоды
        self.deck = [i + j for j in suit for i in nominal]
        # вывод результата  
        self.__clear_fill_listbox(self.__listbox_ordered, self.deck)

    def __shuffle(self):
        """Выполняет перетасовку и выводит результат в listbox"""
        deck = self.deck
        # перетасовка 
        for i in range(0, len(deck)):
            j = rand.randint(0, len(deck[i]))
            deck[i], deck[j] = deck[j], deck[i]
        # вывод результата
        self.__clear_fill_listbox(self.__listbox_shuffled, deck)
        
    @staticmethod
    def __clear_fill_listbox(lbox, filler):
        """Очищает и заполняет listbox"""
        lbox.delete(0, tk.END)  
        for card in filler: 
            lbox.insert(tk.END,card)
           
if __name__ == "__main__":
    app = App()
    app.mainloop()
