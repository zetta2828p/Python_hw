# Площадь квадрата округляя вверх, если сторона не является целым числом

import math


def square(side):
    area = side * side

    if side != int(side):
        area = math.ceil(area)

    return area


num_side = float(input("Укажите размер стороны квадрата: "))
print(f"Площадь квадрата равна: {square(num_side)}")
