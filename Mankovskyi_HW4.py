from time import sleep


def list_remove():
    """
    Дан list произвольных чисел (напр [11, 77, 4, 22, 0, 3, 5, 95, 7, 87, 13, 45, 67, 44,]).
    Написать программу, которая удалит из него все числа, которые меньше 18 и больше 81.
    Учтите, что это должен быть именно исходный лист (с тем же id), а не новый.
    """

    lst = [11, 77, 4, 22, 0, 3, 5, 95, 7, 87, 13, 45, 67, 44]
    print('Before', id(lst), lst)

    for element in lst:
        if element < 18 or element > 81:
            # lst.pop(lst.index(element))
            # lst.remove(element)
            del lst[lst.index(element)]
    print('After', id(lst), lst)


def task_2():
    """"
    Искусственный интеллект". Есть строка произвольного содержания. Программа должна сообщить:
    "It's phone number" если строка это телефонный номер ("+" и 12 цифр, напр "+380631112233")
    "It's name" если строка это ФИО (имя и инициалы, например "Ivanov A. B.")
    """

    input_ = input('Введите строку номер телефона или что-то иное: \n')
    if type(input_) != str or not input_:
        print('Это не строка, аборт))')
        return
    else:
        x_ = input_.split()  # split() помещает строку в список по элементно, не по буквам

    if len(x_) == 1 and len(list(x_[0])) == 13 and list(x_[0])[0] == '+':
        print('It\'s phone number')
    elif len(x_) == 2:
        print('It\'s bullshit')
    elif len(x_) >= 3:
        print('It\'s name')
    else:
        print('Something went wrong')


def task_3():
    """
    * Есть строка произвольного содержания. Найти и вывести на экран самое длинное слово в строке, в котором
    присутствуют подряд две согласные буквы. Если в строке присутствует слово с тремя согласными буквами
    подряд - вывести это слово на экран в верхнем регистре.
    """
    user_input = input('Enter here: ')

    consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
                      'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

    longest_word = ''

    for word in user_input.split():
        for cl in consonant_list:
            if cl * 3 in word:
                longest_word = word.upper()
                break
            if cl * 2 in word:
                if len(word) > len(longest_word):
                    longest_word = word
    if longest_word == '':
        pass
    else:
        print(f'The longest word with the couple consonants: {longest_word}')


if __name__ == '__main__':
    print('Исполняю 1 задание')
    list_remove()
    sleep(5)
    print('Исполняю 2 задание')
    task_2()
    sleep(5)
    print('Исполняю 3 задание')
    task_3()


