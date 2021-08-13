import random
from time import sleep

"""
Пишем игру. Программа выбирает из диапазона чисел (пусть для начала будет 1-100) случайное число и предлагает
пользователю его угадать. Пользователь вводит число. Если пользователь не угадал - предлагает пользователю
угадать еще раз, пока он не угадает. Если угадал - спрашивает хочет ли он повторить игру (Y/N).
Если Y - повторить. N - Прекратить
"""


def int_checker(x):
    try:
        return int(x)
    except ValueError as e:
        print(f'%%%%%% LOGS: Поймали ошибку ввода {e}')
        to_int = input('Это не целое число, повтори ввод \n')
        try:
            return int(to_int)
        except ValueError as e2:
            print(f'%%%%%% LOGS: Поймали ошибку ввода {e2}')
            print('User output: Снова введено не целое число, прерываю программу')
            exit()


def is_hot(x_value, try_value):
    diff = abs(x_value - try_value)
    if 10 > diff > 5:
        return 'Тепло'
    elif 4 > diff > 1:
        return 'Горячо'
    else:
        return 'Холодно'


def task_1_random_number_game():
    answers = ['yes', 'no', 'y', 'n']
    current = int(random.randrange(1, 100))
    print(f'Я загадал >>>>>>> {current} <<<<<<< \n')

    while True:
        is_right = int_checker(input('Угадай число, которое я сгенерировал \n'))
        if is_right < 1 or is_right > 100:
            print('Это не целое число или число вне разрешенного диапазона, прерываю программу')
            exit()

        elif is_right == current:
            restart = str(input('Угадал, хочешь повторить тупую игру (Y/N) \n'))
            restart.lower()
            if restart in answers and restart == answers[0] or restart == answers[2]:
                continue
            else:
                print('Досвидули')
                break

        elif is_right > current:
            print('Не угадал, попробуй еще раз, твое число больше загаданного')

        elif is_right < current:
            print('Не угадал, попробуй еще раз, твое число меньше загаданного')

        else:
            exit()


"""
* Добавить в задание 2 счетчик попыток и диапазон чисел (начало и конец). Пользователь вводит количество
попыток, за которые он может угадать число, начало и конец диапазона. На каждом шаге угадывания числа
сообщайте пользователю сколько попыток у него осталось. Если пользователь не смог угадать за отведенное
количество попыток сообщить ему об окончании (Looser!).


** Добавить в задание 2 вывод сообщения-подсказки. Если пользователь ввел число, и не угадал - сообщать:
"Холодно" если разница между загаданным и введенным числами больше 10, "Тепло" - если от 5 до 10 и
"Горячо" если от 4 до 1.
"""



def task_2_random_number_game():
    reload = False
    answers = ['yes', 'no', 'y', 'n']
    print('Нужно ввести диапазон для генерации случайного числа \n')
    range_min = int_checker(input('Введите нижнюю границу диапазона \n'))
    range_max = int_checker(input('Введите верхнюю границу диапазона \n'))
    max_tries = int_checker(input('Введите количество попыток для угадывания \n'))

    current = int(random.randrange(range_min, range_max))
    print(f'%%%% LOGS: Загаданое число - {current} \n')

    for try_ in range(1, max_tries + 1):
        hint = '0 YOU ARE LOOSER!' if 0 == max_tries - try_ else max_tries - try_
        is_right = int_checker(input(f'Угадай число, которое я сгенерировал в диапазоне {range_min} - {range_max} \n'))

        if is_right < range_min or is_right > range_max:
            print('Число вне разрешенного диапазона, прерываю программу')
            exit()
        elif is_right == current:
            restart = str(input('Угадал, хочешь повторить тупую игру (Y/N) \n'))
            restart.lower()
            if restart in answers and restart == answers[0] or restart == answers[2]:
                reload = True
                break
            else:
                print('Досвидули')
                exit()

        elif is_right > current:
            print(f'Не угадал, попробуй еще раз, твое число больше загаданного и {is_hot(current, is_right)}')
            print(f'Осталось попыток {hint}')

        elif is_right < current and is_hot(current, is_right):
            print(f'Не угадал, попробуй еще раз, твое число меньше загаданного и {is_hot(current, is_right)}')
            print(f'Осталось попыток {hint}')

        else:
            print('##############')
            exit()

    if reload:
        task_2_random_number_game()
    else:
        exit()


if __name__ == '__main__':
    print('Исполняю 1 задание')
    task_1_random_number_game()
    # sleep(5)
    # print('Исполняю 2 задание')
    # task_2_random_number_game()
