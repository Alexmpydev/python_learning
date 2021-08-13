from math import sqrt
"""
1. Напишите класс Triangle. Треугольник должен определяться с помощью обьектов-точек (класс Point).
Реализуйте в нем метод, который бы возвращал площадь треугольника.
2. *Реализуйте в классе Triangle возможность итерировать его обьекты по вершинам (точкам)
"""


def checker(x):
    if type(x) == float:
        return float(x)
    elif type(x) == int:
        return int(x)
    else:
        return 'Это не число'


class Point:
    x_coord: int = 0
    y_coord: int = 0

    def __init__(self, x, y):
        self.x_coord = checker(x)
        self.y_coord = checker(y)

    # def __eq__(self, other):
    #     if not isinstance(other, Point):
    #         return NotImplemented
    #     return self.x_coord == other.x_coord and self.y_coord == other.y_coord

    def __str__(self):
        return f'Point {self.x_coord}, {self.y_coord}'


class Triangle:
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point.x_coord == other.x_coord and Point.y_coord == other.y_coord

    def __init__(self, p1, p2, p3):
        if p1 != p2 and p1 != p3 and p2 != p3 and isinstance(p1, Point) and isinstance(p2, Point) \
                and isinstance(p3, Point):
            self.first_point = p1
            self.second_point = p2
            self.third_point = p3
        else:
            raise Exception('Координаты равны или координаты не пренадлежат классу Point')

    def __str__(self):
        return f'Треугольник с вершинами {self.first_point}, {self.second_point}, {self.third_point}'

    def triangle_square(self):
        x1 = self.first_point.x_coord - self.third_point.x_coord
        x2 = self.second_point.x_coord - self.third_point.x_coord
        y1 = self.first_point.y_coord - self.third_point.y_coord
        y2 = self.second_point.y_coord - self.third_point.y_coord

        s1 = (x1 * y2) - (x2 * y1)

        s = 0.5 * abs(s1)
        print(f'Площадь треугольника = {s}')
        return s

    def iter_tops(self):
        return [self.first_point, self.second_point, self.third_point]


p_1 = Point(5, 55.2)
p_2 = Point(10, 65.2)
p_3 = Point(50, 250)

tr1 = Triangle(p_1, p_2, p_3)
print(tr1.__str__())
square = tr1.triangle_square()

for i in tr1.iter_tops():
    print(f'Вершина с координатами {i}')
