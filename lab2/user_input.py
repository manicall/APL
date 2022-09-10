import re

# возврат целого числа
def get_num(title):
    return int(input(title))

def get_float_safe(title):
    try:
        return float(input(title))
    except ValueError:
        print('Ожидалось число')
