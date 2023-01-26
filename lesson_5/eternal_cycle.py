
a = 1
while a == 1:
    firstname = input('Enter your first name')
    age = int(input('Enter your age'))
    if age <= 0 or not int:
        print('Ошибка, повторите ввод\n')
    elif age > 0 and age < 9:
        print('Привет,шкет', firstname, end='!\n')
    elif age >= 10 and age < 18:
        print('Как жизнь', firstname, end='?\n')
    elif age > 18 and age < 100:
        print('Чего желаете', firstname, end='?\n')
    else:
        print(firstname, ', вы лжете -  в наше время люди столько не живут ...')
'''Погрузил программу в вечный цикл'''




