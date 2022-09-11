import re

class UserInput:
    # возврат целого числа
    @staticmethod
    def get_int(title = "Введите целое число: "):
        return int(input(title))

    @staticmethod
    def get_int_safe(title = "Введите целое число: "):
        res = None
        
        while res == None:
            try:
                res = int(input(title))
            except ValueError:
                print('Ожидалось целое число!')

        return res        

    @staticmethod
    def get_float_safe(title = "Введите число: "):
        res = None
        
        while res == None:
            try:
                res = float(input(title))
            except ValueError:
                print('Ожидалось число!')

        return res

    @staticmethod
    def get_bin_safe(title = "Введите двоичное число: "):
        while True:
            match = re.match("^[01]+$", input(title)) 
            if match == None:
                print("Ожидалось двоичное число!")
            else:
                return match.group()
