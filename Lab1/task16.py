from general import get_num
import math

# вычисление площади круга
def round_area(r):
    return math.pi * r ** 2

# вычисление объема шара
def ball_volume(r):
    return 4 / 3 * math.pi * r ** 3

def main():
    r = get_num("Радиус: ")

    # вывод рассчитанных данных
    print("Площадь круга: ", round_area(r))
    print("Объем шара: ", ball_volume(r))

# точка входа
main()