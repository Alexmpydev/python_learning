"""
Напишите функцию для парсинга номерных знаков автомоблей Украины (стандарты - AА1234BB, 12 123-45AB, a12345BC)
с помощью регулярных выражений. Функция принимает строку и возвращает None если вся строка не является номерным
 знаком. Если является номерным знаком - возвращает саму строку.

* Напишите класс, который выбирает из произвольного текста номерные знаки и возвращает их в виде пронумерованного
списка с помощью регулярных выражений.

** Создайте репозиторий на GitLab или GitHub. Сохраните отдельной веткой (пусть будет HW14) дз по регулярным выражениям
"""
import re


def auto_parse():
    pattern1 = re.compile(pattern='^[ABCEHIKMOPTX]{2}\d{4}(?<!0{4})[ABCEHIKMOPTX]{2}$')
    pattern2 = re.compile(pattern='^[abcehikmoptx]{1}\d{5}(?<!0{5})[ABCEHIKMOPTX]{2}$')
    pattern3 = re.compile(pattern='^\d{2}(?<!0{2})\s{1}\d{3}(?<!0{3})[-]{1}\d{2}(?<!0{2})[ABCEHIKMOPTX]{2}$')
    inp = input('Введите номер автомобиля: ')
    num = pattern1.findall(inp) or pattern2.findall(inp) or pattern3.findall(inp)
    if num:
        print(str(num[0]))
        return str(num[0])
    else:
        print(None)
        return None

",kgjdkgj"


class AutoDetect:

    def __str__(self):
        return 'Instance of AutoDetect'

    def auto_parse(self, user_input=input('Введите номер автомобиля: ')):
        pattern1 = re.compile(pattern='[ABCEHIKMOPTX]{2}\d{4}(?<!0{4})[ABCEHIKMOPTX]{2}')
        pattern2 = re.compile(pattern='[abcehikmoptx]{1}\d{5}(?<!0{5})[ABCEHIKMOPTX]{2}')
        pattern3 = re.compile(pattern='\d{2}(?<!0{2})\s{1}\d{3}(?<!0{3})[-]{1}\d{2}(?<!0{2})[ABCEHIKMOPTX]{2}')
        num = pattern1.findall(user_input) or pattern2.findall(user_input) or pattern3.findall(user_input)
        if num:
            print(num)
            return num
        else:
            print(None)
            return None


auto_parse()

n = AutoDetect()
print(n.__str__())
n.auto_parse()

