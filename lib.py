# функцию, которая требует от пользователя ответить да или нет ( Y\N )
# и возвращает True\False в зависимости от того, что он ввел.

def repeater(request):
    answers = ['yes', 'no', 'y', 'n']
    if request in answers and request == answers[0] or request == answers[2]:
        return True
    else:
        return False


