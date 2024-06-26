# задание 1

"""
При проверке баланса кошелька в debank нужно перейти по url
https://debank.com/profile/0xac8ce8fbc80115a22a9a69e42f50713aae9ef2f7
где 0xac8ce8fbc80115a22a9a69e42f50713aae9ef2f7 - адрес вашего кошелька.
Напишите программу, которая спрашивает ввод адреса кошелька
в терминал и выводит в терминале url, сделайте без использования f строк (без f"")
P.S. с f строками делать удобнее, но мы тренируем конкатенацию
"""

a = input("Введите адрес кошелька:")
print("https://debank.com/profile/" + a)


# задание 2

"""
Напишите программу, которая генерирует простой пароль состоящий из 4 символов,
в пароле должны быть:
- маленькая латинская буква
- большая латинская буква
- цифра
- спец символ (например !@#$%^&*)
при каждом запуске программы пароль должен быть разным, 
для работы используйте только те инструменты,
которые мы обсуждали  в уроках (индексация строк, конкатенация, 
генератор случайного числа и т.д.).
Попробуйте сделать 2 разные реализации программы
"""

import random

letters = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
letters_list = letters.split(", ")
random_letter = random.choice(letters_list)
random_upper_letter = random_letter.upper()

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
numbers_list = numbers.split(", ")
random_number = random.choice(numbers_list)

symbols = "!, @, #, $, %, ^, &, *"
symbols_list = symbols.split(", ")
random_symbol = random.choice(symbols_list)

password = random_letter + random_upper_letter + random_number + random_symbol

print(password)


# задание 3

"""
Напишите программу, которая проверяет длину пароля введенную пользователем.
При запуске программы пользователь должен ввести пароль в терминал,
если длина пароля меньше 8 символов, программа должна вывести в терминал
сообщение с текстом False, если длина пароля больше или равна 8 символам,
программа должна вывести в терминал сообщение с текстом True
"""

password = input()

if len(password) >= 8:
    print("True")
else:
    print("False")


# задание 4

"""
Напишите программу, которая запрашивает в терминале 
Фамилию, Имя и возраст в одну строчку, например ("  Макс Зарев 31 ")
программа должна удалять пустые символы до и после введенных данных, если пользователь ввел лишние пробелы,
и выводит в терминале сообщение, где имя должно быть написано 3 раза, фамилия 4 раза,
а возраст на 10 лет старше введенного, например (Макс Макс Макс Зарев Зарев Зарев Зарев 41)
"""

user_input = input("Введите имя, фамилию и возраст в одну строчку через пробел:")

stripped_user_input = user_input.strip()
word_1, word_2, word_3 = stripped_user_input.split(" ")
word_3_int = int(word_3)

print(f"{word_1} {word_1} {word_1} {word_2} {word_2} {word_2} {word_2} {word_3_int + 10}")


# задание 5

"""
Нарисовать в терминале елочку используя умножение строк
     * 
    ***
   *****
  *******
 *********
***********
     *
    ***
"""

print(" " * 5, "*" * 1, " " * 5)
print(" " * 4, "*" * 3, " " * 4)
print(" " * 3, "*" * 5, " " * 3)
print(" " * 2, "*" * 7, " " * 2)
print(" " * 1, "*" * 9, " " * 1)
print(" " * 0, "*" * 11, " " * 0)
print(" " * 5, "*" * 1, " " * 5)
print(" " * 4, "*" * 3, " " * 4)


# задание 6

"""
Создайте программу которая запрашивает в терминале текст и после печатает его
в терминале в обратном порядке (например вводим "привет", программа печатает "тевирп")
реализуйте используя только индексацию строк и срезы (нужно будет погуглить)
"""

text = input("Введите текст, который нужно перевернуть: ")
reversed_text = text[::-1]
print(reversed_text)


# задание 7

"""
Создайте программу в которой должен быть записан пароль в переменную,
программа при запуске должна спрашивать пользователя ввести пароль и 
выводить True если пароль верный и False если нет.
"""

true_password = "zarevmax93pizdec"

password = str(input("Введите пароль:"))

if password == str(true_password):
    print("True")
else:
    print("False")