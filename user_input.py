import re
class UserInput:
    @staticmethod
    def get_int(title = "Введите целое число: "):
        '''получение от пользователя целого числа без проверки'''
        return int(input(title))

    @staticmethod
    def get_int_safe(title = "Введите целое число: "):
        '''получение от пользователя целого числа с проверкой'''
        res = None
        
        while res == None:
            try:
                res = int(input(title))
            except ValueError:
                print('Ожидалось целое число!')

        return res        

    @staticmethod
    def get_float_safe(title = "Введите число: "):
        '''получение от пользователя вещественного числа с проверкой'''
        res = None
        
        while res == None:
            try:
                res = float(input(title))
            except ValueError:
                print('Ожидалось число!')

        return res

    @staticmethod
    def get_bin_safe(title = "Введите двоичное число: "):
        '''получение от пользователя двоичного числа с проверкой'''
        while True:
            match = re.match("^[01]+$", input(title)) 
            if match == None:
                print("Ожидалось двоичное число!")
            else:
                return match.group()

    @staticmethod
    def get_hex_safe(title = "Введите шестнадцатиричное число: "):
        '''получение от пользователя шестнадцатиричного числа с проверкой'''
        while True:
            match = re.match("^[0-9a-fA-F]+$", input(title)) 
            if match == None:
                print("Ожидалось шестнадцатиричное число!")
            else:
                return match.group().upper()