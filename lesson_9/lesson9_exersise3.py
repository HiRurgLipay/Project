# ЗАДАНИЕ 3
# Программа на вход должна принимать файл с каким-то текстом.
# Пользователь вводит любую английскую букву.
# Программа должна считать сколько раз эта буква встречается в
# тексте (без учёта регистра). То есть буквы n и N
# считать одинаковыми.
#
# Пример работы:
# Введите букву: n
# Результат: буква встречается 124 раза в тексте.

def count_letter(filename, letterinfunc):
    with open(filename, 'r') as file:
        text = file.read()

    lowercase_letter = letterinfunc.lower()
    count = 0
    for char in text:
        if char.lower() == lowercase_letter:
            count += 1

    return count


file_name = input("Enter the file name: ")
letter = input("Enter the letter: ")
result = count_letter(file_name, letter)
print(f"The letter '{letter}' appears {result} times in the text.")
