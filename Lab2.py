import random as r
from user_input import UserInput as ui

class Task19:
    # словарь оценок
    marks = {
        4 : 'A', 
        3 : 'B',
        2 : 'C',
        1 : 'D',
        0 : 'F'
    }

    @classmethod
    def print_answer(self):
         # для тестирования программы используется диапазон случайных чисел
        for i in range(10):
            rand = r.uniform(-1, 6)
            print(f"Число: {rand} Оценка: {self.get_char_mark(self, rand)}")

    def get_char_mark(self, num_mark):
        if num_mark > 4.0:
            return "A+"
        if (num_mark < 0): 
            print("Необходимо ввести число больше нуля!")

        # целая часть в заданном числе
        int_part = int(num_mark)
        # дробная часть в заданном числе
        decimal_part = num_mark - int_part
        # округление дробной части
        rounded = self.get_rounded(decimal_part)
        # получение знака
        sign = self.get_sign(rounded)

        # возврат результата
        if sign == "":
            return self.marks[int_part + rounded]
        elif sign == "-": 
            return self.marks[int_part + 1] + sign
        else:
            return self.marks[int_part] + sign

    def get_rounded(decimal_part):    
        l = [0, 0.3, 0.7, 1]
        # возврат числа, к которому наиболее близок заданный параметр
        return min(l, key=lambda x:abs(x-decimal_part))

    def get_sign(rounded):
        if rounded > 0.5 and rounded < 1: 
            return "-"
        elif (rounded < 0.5 and rounded > 0):
            return "+"
        else:
            return ""

class Task20:
    @classmethod
    def print_answer(self):
        rate = None
        while True:
            rate = ui.get_float_safe("Введите число: ")
            if (rate != None):
                if (rate == 0 or rate == 0.4 or rate >= 0.6):
                    break
                else: 
                    print(
                        'В качестве рейтинга', 
                        'используются значения "0", "0.4", "0.6 и выше"')

        # Вывод результата
        value, increase = self.get_result(rate)
        print(f"Значение: {value}")
        print(f"Сумма прибавки сотрудника: {increase}")

    def get_result(rate):
        salary = 2400
        if rate == 0:
            return ("Низкий уровень", salary * rate)
        elif rate == 0.4:
            return ("Удовлетворительный уровень", salary * rate)
        elif rate >= 0.6:
            return ("Высокий уровень", salary * rate)

print("Результат задачи 19")
Task19.print_answer()

print("\nРезультат задачи 20")
Task20.print_answer()