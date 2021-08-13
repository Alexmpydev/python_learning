"""
1. Есть list с данными lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишите механизм, который формирует новый list (например lst2), который содержит только переменные
типа строка, которые есть в lst1.

"""

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']


def filter_list(list_to_filer):
    list_to_return = []
    for a in list_to_filer:
        print(a)
        if isinstance(a, str):
            print("this is string ", a)
            list_to_return.append(a)
    print(list_to_return)
    return list_to_return


# filter_list(lst1)

"""
2. Ввести из консоли строку. Определить количество слов в этой строке, которые начинаются на букву "а" 
(учтите, что слова могут начинаться с большой буквы).
"""


def find_a(string):
    input_str = input("Enter your string: ")

    print(input_str)

    res = input_str.lower()
    my_list = res.split(" ")
    print(my_list)

    result = 0
    for word in my_list:
        if word.startswith('a'):
            result = result + 1

    print(result)


"""
*3. Вывести пользователю приветствие ('Hello!'). Спросить у пользователя, хочет ли он повторно его 
увидеть этот текст?. Если пользователь введет Y - повторить приветствие. После каждого приветствия повторять 
вопрос. Если если пользователь введет N - прекратить спрашивать. Если пользователь ввел не Y или N - попросить 
ввести именно Y или N, переспрашивать пока не введет Y или N и по результату принимать решение повторять или нет.


"""

print('Hello!')

input_str = input("хочет ли он повторно его увидеть этот текст?: ")
print(input_str)

to_continue = True
while to_continue:
    if input_str not in ["Y", "N"]:
        input_str = input("Неверный ввод. Возможные варианты Y/N. Повторите ввод  ")
    if input_str == "Y":
        print('Hello!')
        break
    elif input_str == "N":
        to_continue = False

