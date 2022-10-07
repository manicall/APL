import tkinter as tk
import random as rand
class App(tk.Tk):
    def __init__(self):
        super().__init__()  
        self.title("Лабораторная работа 7")
        self.geometry("800x600")    
        
        self.deck = []
        
        self.create_menu()
        self.create_listboxes()
        # входное и выходное выражения
        self.input_expression = tk.StringVar()
        self.output_expression = tk.StringVar()
        
        lframe = tk.LabelFrame(self, text="задание 21")
        lframe.pack(padx=5, pady=5, anchor=tk.NW)
        
        input_frame = tk.Frame(lframe)
        output_frame = tk.Frame(lframe)
        
        input_frame.pack()
        output_frame.pack(side=tk.LEFT)

        tk.Label(input_frame, text="Выражение").pack(side=tk.LEFT)
        tk.Entry(input_frame, textvariable=self.input_expression).pack(padx=5)
        
        tk.Label(output_frame, textvariable=self.output_expression).pack(padx=5)
  
    def create_menu(self):
        main_menu = tk.Menu()
        
        lables = [
            "Создать колоду", 
            "Перетасовать колоду", 
            "Заменить унарный оператор"
        ]
        
        commands = [
            self.create_deck,
            self.shuffle, 
            self.replace_uoperations
        ]
        
        for l, c in zip(lables, commands):
            main_menu.add_cascade(label=l, command=c)

        self.config(menu=main_menu)
        
    def create_listboxes(self):     
        lframe = tk.LabelFrame(self, text="Задание 16")
        lframe.pack(fill=tk.Y, padx=5, pady=5, side=tk.LEFT)
        
        self.__listbox_ordered = self.create_listbox(lframe)  
        self.__listbox_shuffled = self.create_listbox(lframe)      
        
    @staticmethod
    def create_listbox(master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        listbox = tk.Listbox(frame)
        listbox.pack(fill=tk.Y, side=tk.LEFT)
        
        scrollbar = tk.Scrollbar(frame, orient="vertical")
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        
        return listbox
        
    def create_deck(self):
        """Создает колоду и выводит результат в listbox"""
        nominal = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K',  'A']
        # масть
        suit = ['s', 'h', 'd', 'c']
        # создание колоды
        self.deck = [i + j for j in suit for i in nominal]
        # вывод результата  
        self.clear_fill_listbox(self.__listbox_ordered, self.deck)

    def shuffle(self):
        """Выполняет перетасовку и выводит результат в listbox"""
        deck = self.deck
        # перетасовка 
        for i in range(0, len(deck)):
            j = rand.randint(0, len(deck[i]))
            deck[i], deck[j] = deck[j], deck[i]
        # вывод результата
        self.clear_fill_listbox(self.__listbox_shuffled, deck)
        
    @staticmethod
    def clear_fill_listbox(lbox, filler):
        """Очищает и заполняет listbox"""
        lbox.delete(0, tk.END)  
        for card in filler: 
            lbox.insert(tk.END,card)
            
    def replace_uoperations(self):
        tokens = self.tocken_extractor(self.input_expression.get())
        # знаки, которые могут стоять перед унарным знаком
        prev_tokens = ['+', '-', '*', '/', '^', '(']
        # унарные операции
        u_operations = prev_tokens[0:2]
        # проверка, на унарность первой лексемы в выражени
        if self.check_symbol(tokens[0], u_operations):
            tokens[0] = 'u' + tokens[0]
        
        # преобразование "+", "-" в "u+","u-"
        for i in range(1, len(tokens)):            
            if self.check_symbol(tokens[i], u_operations) \
                and self.check_symbol(tokens[i - 1], prev_tokens):
                    tokens[i] = 'u' + tokens[i]

        self.output_expression.set(" ".join(tokens))
        
    def tocken_extractor(self, _str):
        '''разбивает выражение на лексемы'''
        simple_tokens = ['+', '-', '*', '/', '^', '(', ')']
        res_list = []
        j = None
          
        for i in enumerate(_str):
            # i[0] - индекс
            # i[1] - символ в строке
            
            # если встретился оператор из simple_tokens
            if self.check_symbol(i[1], simple_tokens): 
                append_number()
                res_list.append(i[1])
            # если очередной символ является числом или резделителем дроби
            elif i[1].isdigit() or i[1] == '.': 
                # запоминает позицию в строке,
                # с которой начинается лексема, являющаяся числом
                if j == None: j = i[0]
            # если встретился неизвестный символ
            else: 
                append_number()
        
        append_number() 
            
        def append_number():
            '''если лексема оказалась числом, 
            то добавляет это число из строки с позиции j до позиции i[0] в список'''
            nonlocal j, res_list, _str
            
            if j != None:
                res_list.append(_str[j:i[0]])
                j = None
            
        return res_list    

    @staticmethod
    def check_symbol(_char, _list):
        '''проверяет содержится ли символ в списке'''
        return any(list(map(lambda x: _char == x, _list)))

if __name__ == "__main__":
    app = App()
    app.mainloop()
