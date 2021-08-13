from time import sleep

"""
   1. Написать функцию, принимающую один аргумент. Функция должна вывести на экран тип данных этого аргумента
   (используйте type)
"""


def task_1(x):
    print(type(x))
    return
""" 
   2. Написать функцию, принимающую два аргумента. Функция должна :
    - если оба аргумента относятся к числовым типам - вернуть их произведение,
    - если к строкам - соединить в одну строку и вернуть,
    - если первый строка, а второй нет - вернуть словарь (dict), в котором ключ - первый аргумент, значение - второй
    в любом другом случае вернуть кортеж (tuple) из аргументов
"""

def task_2(var1, var2):
    from numbers import Number
    if isinstance(var1, Number) and isinstance(var2, Number):
        return var1 * var2

    elif type(var1) == str and type(var2) == str:
        return var1 + var2

    elif isinstance(var1, str) and type(var2) != str:
        return {var1: var2}

    else:
        return (var1, var2)

"""
    3. Дан словарь продавцов и цен на какой то товар у разных продавцов:
    { 'citrus': 47.999, 'istudio' 42.999, 'moyo': 49.999, 'royal-service': 37.245, 'buy.ua': 38.324,
    'g-store': 37.166, 'ipartner': 38.988, 'sota': 37.720 }.
     Написать функцию возвращающую список имен продавцов, чьи цены попадают в определенный диапазон
     ( верхняя и нижняя граница цены). Функция должна принимать словарь с ценами, начало и конец
     диапазона и возвращать список (list) имен.
"""

def task_3(prices: dict, bot: float, top: float):
    lst = []
    for k, v in prices.items():
        if bot < v < top:
            lst.append(k)
        else:
            pass
    print(lst)
    return lst

"""
    4.* Пользователь вводит строку произвольной длины. Написать функцию, которая должна вернуть
    словарь следующего содержания: ключ - количество букв в слове, значение - список слов с
    таким количеством букв. Отдельным ключем, например "0", записать количество пробелов.
    Отдельным ключем, например "punctuation", записать все уникальные знаки препинания, которые есть в тексте. 
    Например:
    {
     "0": 137,
     "1": ['a', 'c', 'в', 'о']
     "2": ['по', 'за']
     "3": ['при', 'про', 'еще']
     и т.д  для всех возможных вариантов длины слова в переденной строке...
    "punctuation" : ('.', '?', ',')
     }
"""

def task_4(text: str):
    count = 0
    for i in range(0, len(text)):
        if text[i] == " ":
            count += 1

    count_punct = set()
    punct = ['.', ',', '!', '?', '-']
    for i in range(0, len(text)):
        if text[i] in punct:
            count_punct.add(text[i])

    print({'0': count, 'punctuation': count_punct})
    return {'0': count, 'punctuation': tuple(count_punct)}


if __name__ == '__main__':
    print('Исполняю 1 задание')
    task_1([])
    sleep(5)

    print('Исполняю 2 задание')
    print(task_2('Karl', 2.6))
    sleep(5)

    print('Исполняю 3 задание')
    x = {'citrus': 35.999, 'istudio': 42.999, 'moyo': 15.999, 'royal-service': 27.245, 'buy.ua': 13.324,
         'g-store': 30.166, 'ipartner': 55.988, 'sota': 5.720}

    task_3(x, 15, 35.5)
    sleep(5)

    print('Исполняю 4 задание')
    task_4('dlkg, dkgdlkh. dlk. ldhgdk? gkkdh! ')
    sleep(5)




