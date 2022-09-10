import user_input as ui

def main():
    rate = None
    while True:
        rate = ui.get_float_safe("Введите число: ")
        if (rate != None):
            if (rate == 0 or rate == 0.4 or rate >= 0.6):
                break
            else: 
                print('В качестве рейтинга используются значения "0", "0.4", "0.6 и выше"')

    # Вывод результата
    value, increase = get_result(rate)
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

main()