# словарь оценок
marks = {
    4 : 'A', 
    3 : 'B',
    2 : 'C',
    1 : 'D',
    0 : 'F'
}

def get_char_mark(num_mark):
    if num_mark > 4.0:
         return "A+"
    if (num_mark < 0): 
        print("Необходимо ввести число больше нуля!")

    # целая часть в заданном числе
    int_part = int(num_mark)
    # дробная часть в заданном числе
    decimal_part = num_mark - int_part
    # округление дробной части
    rounded = get_rounded(decimal_part)
    # получение знака
    sign = get_sign(rounded)

    # возврат результата
    if sign == "":
        return marks[int_part + rounded]
    elif sign == "-": 
        return marks[int_part + 1] + sign
    else:
        return marks[int_part] + sign

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

# тест алгоритма       
import random as r

for i in range(10):
    rand = r.uniform(-1, 6)
    print(f"Число: {rand} Оценка: {get_char_mark(rand)}")
    