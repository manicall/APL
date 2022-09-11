from curses.ascii import isdigit, islower, isupper
import random as r

class RandomPassword:
    @staticmethod
    def get_random_password():
        size = r.randint(7, 10)
        password = ""
        for i in range(size):
            password += chr(r.randint(33, 126))

        return password
    
    @staticmethod
    def is_strong(password):
        if len(password) < 8:
            return False

        # условия надежности пароля
        has_lower = False
        has_upper = False
        has_digit = False

        for p in password:
            has_lower = check_condition(has_lower, islower)
            has_upper = check_condition(has_upper, isupper)
            has_digit = check_condition(has_digit, isdigit)

        # проверяет условие, если оно еще не истинно
        def check_condition(pass_condition, func):
            return func(pass_condition) if (not pass_condition) else True

        # возвращает истину, если пароль надежный
        return True if (has_lower and has_upper and has_digit) else False

