from functools import wraps
from time import process_time
from time import time
from timeit import default_timer

"""
1. Модифицируйте класс Point с занятия. Реализуйте передачу в X и Y только числовых значений.
Модифицируйте класс Line с занятия следующим образом - обеспечьте проверку точек начала и
конца - координаты точек начала и конца отрезка не должны совпадать.

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


p_1 = Point(10, 55.2)
p_2 = Point(10, 55.2)
print(p_1 == p_2)


class Line:
    first_point = None
    second_point = None

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point.x_coord == other.x_coord and Point.y_coord == other.y_coord

    def __init__(self, p1, p2):
        if p1 != p2 and isinstance(p1, Point) and isinstance(p2, Point):
            self.first_point = p1
            self.second_point = p2
        else:
            raise Exception('Координаты равны или координаты не пренадлежат классу Point')

    def length(self):
        x = (self.first_point.x_coord - self.second_point.x_coord)**2
        y = (self.first_point.y_coord - self.second_point.y_coord)**2
        return (x + y) ** 0.5

    def __str__(self):
        return f'Line {str(self.first_point), str(self.second_point)} with length {self.length()}'


l1 = Line(p1=p_1, p2=p_2)
print(l1)
print(l1.first_point, l1.second_point)

"""
 2. Напишите декоратор, измеряющий время выполнения функции. Работа функции не должна быть и
 возвращаемое значение нарушено работой декоратора
3. * Модифицируйте декоратор таким образом, чтобы декоратор изменял возвращаемое значение функции на дикт

{
 'result': результат работы функции
'time' : время выполнения в формате H-MM-SS-MS (часы-минуты-секунды-милисекунды)
 }
"""


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = default_timer() * 1000
        try:
            return func(*args, **kwargs)
        finally:
            end_ = (default_timer() * 1000) - start
            print(
                f"Total execution time {func.__name__}: {end_} ms"
            )

    return _time_it


def dict_decor(foo):
    def wrapper(*args, **kwargs):
        t1 = default_timer() * 1000
        res = foo(*args, **kwargs)
        t2 = (default_timer() * 1000) - t1

        return print({'result': res, 'time': t2},  foo.__name__)
    return wrapper


@measure
def foo1(n):
    res = 0
    for i in range(500):
        res += i + n
    return res

foo1(7)


@dict_decor
def foo2(n):
    res = 0
    for i in range(500):
        res += i + n
    return res

foo2(6)
