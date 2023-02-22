# Написать функцию, которая принимает n-ое количество координат точек.
# И в ответ возвращает длину маршрута между ними.
# Каждая координата представлена кортежем, состоящим из двух объектов типа int.
# Длина отрезка: https://www.calc.ru/Formula-Dliny-Otrezka.html
# Примеры использования функции:
# result = distance((1, 1), (1, 2), (3, 3))
# print(result) # выведет 1
#
# В общем виде:
# result = distance((1, 1), (2, 3), (5, 8), ..., (xn, yn))

import math


def distance(*coordinates):
    result_of_range = 0
    for i in range(len(coordinates) - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i + 1]
        result_of_range += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return result_of_range


result = distance((1, 1), (1, 2), (3, 3), (18, 34))
print(result)
