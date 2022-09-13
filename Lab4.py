from wsgiref import handlers
from random_password import RandomPassword as rp
from user_input import UserInput as ui
from string import ascii_uppercase

class Task19:
    def print_answer():
        count = 0
        password = rp.get_random_password()

        while not rp.is_strong(password):
            # ? print(password)
            count += 1
            password = rp.get_random_password()

        print(f"Пароль: {password}]\nПопытки: {count}")
class Task20:
    @classmethod
    def print_answer(self):
        h = ui.get_hex_safe()
        dec = self.hex2int(h)
        print(f"Ответ: {dec} Проверка: {int(h, 16)}")
        
        dec = ui.get_int_safe()
        h = self.int2hex(dec)
        print(f"Ответ: {h}, Проверка: {hex(dec)}")
        
    @classmethod
    def hex2int(self, hex):
        sum = 0
        dec_list = self.get_dec_list(hex)
        
        j = len(dec_list) - 1
        
        print(dec_list)
        
        for i in dec_list:
            sum += i * 16 ** j
            j -= 1
        
        return sum
        
    def get_dec_list(hex):
        dec_list = []
        
        for i in hex:
            if (not i.isdigit()): # замена буквы на число
                dec_list.append(ascii_uppercase.find(i) + 10)
            else:
                dec_list.append(int(i))
                
        return dec_list
    
    def int2hex(q):
        result = ""

        while q > 0:
            r = q % 16
            # замена числа больше 10 на букву
            r = r if r < 10 else ascii_uppercase[r - 10] 
            result = str(r) + result
            q //= 16

        return result
    
if __name__ == "__main__": 
    print("Задание 19")
    Task19.print_answer()
    print()
    print("Задание 20")
    Task20.print_answer()