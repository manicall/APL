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
        self.__input_expression = tk.StringVar()
        self.__output_expression = tk.StringVar()
        
        lframe = tk.LabelFrame(self, text="задание 21")
        lframe.pack(padx=5, pady=5, anchor=tk.NW)
        
        input_frame = tk.Frame(lframe)
        output_frame = tk.Frame(lframe)
        
        input_frame.pack()
        output_frame.pack(side=tk.LEFT)

        tk.Label(input_frame, text="Выражение").pack(side=tk.LEFT)
        tk.Entry(input_frame, textvariable=self.__input_expression).pack(padx=5)
        
        tk.Label(output_frame, textvariable=self.__output_expression).pack(padx=5)
  
    def __create_menu(self):
        main_menu = tk.Menu()
        
        lables = [
            "Создать колоду", 
            "Перетасовать колоду", 
            "Заменить унарный оператор"
        ]
        
        commands = [
            self.__create_deck,
            self.__shuffle, 
            self.__replace_uoperations
        ]
        
        for l, c in zip(lables, commands):
            main_menu.add_cascade(label=l, command=c)

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
            
    def __replace_uoperations(self):
        tokens = self.__tocken_extractor(self.__input_expression.get())
        
        prev_tokens = ['+', '-', '*', '/', '^', '(']
        u_operations = prev_tokens[0:2]

        if self.__check_symbol(tokens[0], u_operations):
            tokens[0] = 'u' + tokens[0]
        
        for i in range(1, len(tokens)):            
            if self.__check_symbol(tokens[i], u_operations) \
                and self.__check_symbol(tokens[i - 1], prev_tokens):
                    tokens[i] = 'u' + tokens[i]

        self.__output_expression.set(" ".join(tokens))
        
    def __tocken_extractor(self, _str):
        simple_tokens = ['+', '-', '*', '/', '^', '(', ')']
        res_list = []
        j = None
        
        def append_number():
            nonlocal j, res_list, _str
            
            if j != None:
                    res_list.append(_str[j:i[0]])
                    j = None
        
        for i in enumerate(_str):
            if self.__check_symbol(i[1], simple_tokens):
                append_number()
                res_list.append(i[1])
            elif i[1].isdigit() or i[1] == '.':
                if j == None: j = i[0]
            else:
                append_number()
        
        append_number() 
            
        return res_list    

    @staticmethod
    def __check_symbol(_char, _list):
        return any(list(map(lambda x: _char == x, _list)))

        
           
if __name__ == "__main__":
    app = App()
    app.mainloop()
