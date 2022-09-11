from user_input import UserInput as ui

class Task19:
    @classmethod
    def print_answer(self):
        str_bin = ui.get_bin_safe()
        dec = self.bin_to_dec(str_bin)

        print(f"Ответ: {dec} Проверка: {int(str_bin, 2)}")

    def bin_to_dec(str_bin):
        sum = 0
        j = len(str_bin) - 1

        for i in str_bin:
            sum += 2 ** j * int(i)
            j -= 1

        return sum
        

class Task20:
    @classmethod
    def print_answer(self):
        decimal = ui.get_int_safe()
        binary = self.dec_to_bin(decimal)

        print(f"Ответ: {binary} Проверка: {bin(decimal)}")
        
    def dec_to_bin(q):
        result = ""

        while q > 0:
            r = q % 2
            result = str(r) + result
            q //= 2

        return result

print("Задание 19")
Task19.print_answer()
print()
print("Задание 20")
Task20.print_answer()