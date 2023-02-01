from random import randint
def fill_list(m1, m2, amount, l):
    for i in range(amount):
        l.append(randint(m1, m2))

def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1

list_ = []
dict_ = {}

min = int(input('Минимум: '))
max = int(input('Максимум: '))
qty = int(input('Количество элементов: '))

fill_list(min, max, qty, list_)
analysis(list_, dict_)

for item in sorted(dict_):
    print(('Число -',item, 'встречается -',dict_[item],'раз(а)'))






