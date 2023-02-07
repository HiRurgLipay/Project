def func(n: str):
    try:
        number = float(n)
        if int(number) == number:
            if int(number) < 0:
                return "Вы ввели отрицательное целое число"
            else:
                return "Вы ввели положительное целое число"
        else:
            if number < 0:
                return "Вы ввели отрицательное дробное число"
            else:
                return "Вы ввели положительное дробное число"
    except:
        return "Вы ввели некорректные данные"

print(func(input("Введите число: ")))

