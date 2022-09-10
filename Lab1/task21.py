from general import get_num

# вычисление площади треугольника
def triangle_area(b, h):
    return  b * h / 2

def main():
    print("Площадь треугольника: ", triangle_area(get_num("Основание: "), get_num("Высота: ")))

# точка входа
main()