def func(n: str):
    if n.isdigit():
        if isinstance(n,float):
            if float(n) < 0:
                return f'Вы ввели отрицательное дробное число: {n}'
            else:
                return f'Вы ввели положительное дробнео число: {n}'
        else:
            if int(n) < 0:
                return f'Вы ввели положительное число: {n}'
            else:
                return f'Вы ввели отрицательное число: {n}'
    else:
        return f'Вы ввели некорректное число: {n}'

print(func(input('Введите дробное или целое число')))



