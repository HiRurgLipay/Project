from datetime import datetime
from time import sleep

def time_list(n):
    date_list = [datetime.strftime(datetime.now(sleep(1)), '%Y-%m-%d %H:%M:%S') for _ in range(n)]
    return date_list

print(time_list(int(input('Введите число: '))))

'''Не мог разобраться с условием до последнего занятия,посмотрел ваш вариант решения и вариант решения Анастасии
и попробовал решить одной функцией со sleep, мне показался этот вариант решения самым понятным и удачным,потом в группе
телеграм увидел что Сергей тоже сделл программу одной функцией'''
