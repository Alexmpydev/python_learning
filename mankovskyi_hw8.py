from main_file import printer
from math import sqrt
import random
from time import sleep


# 2. Написать функцию принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения: периметр квадрата,
# площадь квадрата и диагональ квадрата. Можете воспользоваться модулем math для математики
def square(square_side):
    p = square_side * 4
    s = square_side * 2
    d = square_side ** 0.5
    # d1 = sqrt(square_side)
    print(p, s, d)


# 3. * Напишите "Русскую рулетку". В револьвер заряжается 1 патрон из 6. Спрашиваем пользователя
# "Стрелять или нет ?". Случайным образом определяется патрон. Если заряжен - показываем сообщение "Бабах!" .
# Если нет - спрашиваем "Стрелять или нет ?" и тд..
def russian_roulette():
    yes_ = ['yes', 'y', 'да', 'д', 'стрелять']
    no_ = ['no', 'n', 'нет', 'н']

    while True:
        patron = int(random.randrange(1, 6))
        reel = int(random.randrange(1, 6))
        print('Заряжен ли сейчас', patron == reel)

        user_answer = input('Стрелять или нет?\n')
        if user_answer in yes_ and patron == reel:
            print('Бабах!')
            break
        elif user_answer in no_:
            print('Досвидули, ссыкун!')
            break
        elif user_answer not in no_ and user_answer not in yes_:
            print('Буду считать, что ответ НЕТ и снова крутим барабан')
            continue
        else:
            print('Повезло, пока ты жив!')
            continue


if __name__ == '__main__':
    print('Исполняю 1 задание')
    printer()
    sleep(5)
    print('Исполняю 2 задание')
    square(5)
    sleep(5)
    print('Исполняю 3 задание')
    russian_roulette()
