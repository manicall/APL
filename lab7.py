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
        
        frame = tk.Frame(self).pack(side=tk.LEFT, anchor=tk.NW)
        tk.Label(frame, text="Выражение:").pack(side=tk.TOP)
        tk.Entry(frame, textvariable=self.expression).pack(side=tk.LEFT)
          
    def __create_menu(self):
        main_menu = tk.Menu()
        main_menu.add_cascade(label="Создать колоду", command=self.__create_deck)
        main_menu.add_cascade(label="Перетасовать колоду", command=self.__shuffle)

        self.config(menu=main_menu)
        
    def __create_listboxes(self):        
        self.__listbox_ordered = self.__create_listbox()  
        self.__listbox_shuffled = self.__create_listbox()
        
        
    def __create_listbox(self):
        side = "left"
        
        frame = tk.Frame(self)
        frame.pack(side=side, fill="y", padx=10)
        
        listbox = tk.Listbox(frame)
        listbox.pack(fill="y", side=side)
        
        scrollbar = tk.Scrollbar(frame, orient="vertical")
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=side, fill="y")
        
        return listbox
        
    def __create_deck(self):
        nominal = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K',  'A']
        suit = ['s', 'h', 'd', 'c']
        
        # создание колоды
        self.deck = [i + j for j in suit for i in nominal]
        
        self.__clear_fill_listbox(self.__listbox_ordered, self.deck)

    def __shuffle(self):
        deck = self.deck
        # перетасовка 
        for i in range(0, len(deck)):
            j = rand.randint(0, len(deck[i]))
            deck[i], deck[j] = deck[j], deck[i]
        
        self.__clear_fill_listbox(self.__listbox_shuffled, deck)
        
    @staticmethod
    def __clear_fill_listbox(lbox, filler):
        lbox.delete(0, tk.END)  
        for card in filler: 
            lbox.insert(tk.END,card)
           
if __name__ == "__main__":
    app = App()
    app.mainloop()
