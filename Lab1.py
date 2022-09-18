import math
from user_input import UserInput as ui

class Task16:
    # вычисление площади круга
    def round_area(r):
        return math.pi * r ** 2

    # вычисление объема шара
    def ball_volume(r):
        return 4 / 3 * math.pi * r ** 3

    # результат программы
    @classmethod
    def print_answer(self):
        r = ui.get_num("Радиус: ")

        # вывод рассчитанных данных
        print("Площадь круга: ", self.round_area(r))
        print("Объем шара: ", self.ball_volume(r))

class Task21:
    # вычисление площади треугольника
    def triangle_area(b, h):
        return  b * h / 2
    
    # результат программы
    @classmethod
    def print_answer(self):
        b = ui.get_num("Основание: ")
        h = ui.get_num("Высота: ")
        print("Площадь треугольника: ", self.triangle_area(b, h))

if __name__ == "__main__":
    Task21.print_answer()
    Task16.print_answer()