"""
Домашнее задание по list
"""


print('-' * 50)


# задание 1

"""
Вы вводите в терминале любой текст через пробел, программа должна напечатать список в котором все слова в обратном порядке, 
отдельное слово в отдельном элементе списка.
"""

user_input = input("Введите ваш текст: ")

my_list = user_input.split()

print(my_list[::-1])


print('-' * 50)


# задание 2
"""
Возьмите предыдущее задание 3 из урока по while где нужно было раздать дроп рандомным кошелькам и доработайте программу таким образом чтобы кошельки, которые получают
дроп собирались в список и в конце печатался список кошельков получивших дроп, а не строчка.
"""

import random
import time

while True:
    wallets = input("Введите количество кошельков: ")
    if wallets.isdigit():
        wallets = int(wallets)
        break
    else:
        print("Ошибка, введите число")

while True:
    drops = input("Введите количество дропов: ")
    if drops.isdigit():
        drops = int(drops)
        break
    else:
        print("Ошибка, введите число")

gas_price = 50

wallet_counter = 0
display_wallets = []

while wallet_counter < wallets:

    wallet_counter += 1

    if random.randint(0, 1) and drops > 0:
        print(f"Кошелек {wallet_counter} получил дроп.")
        drops -= 1
        display_wallets.append(wallet_counter)

    else:
        print(f"Кошелек {wallet_counter} не получил дроп.")
        continue

    while True:
        gas_price = random.randint(15, 50)
        if gas_price > 30:
            print(f"Газ {gas_price}, что выше порога в 30, ждем более низкого.")
            time.sleep(1)
            continue
        else:
            print(f"Газ {gas_price}, клеймим дроп.")
            break

    if drops != 0 and wallet_counter == wallets:
        wallet_number = 0

print(f"Распродажа завершена, дроп получили кошельки: {display_wallets}")


print('-' * 50)


# задание 3

"""
Создайте при помощи цикла while список в котором будут перечислены четные числа от 1 до 100 включительно. (пример: [2, 4, 6, 8, 10, ...])
В во втором цикле while замените все числа на эти же числа в квадрате.
"""

number = 0
index = 0
my_list = []
squared_list = []

while number < 100:
    number += 2
    my_list.append(number)
print(my_list)

while index < len(my_list):
    squared_number = my_list[index] ** 2
    squared_list.append(squared_number)
    index += 1
print(squared_list)


print('-' * 50)


# задание 4
"""
Создайте генератор списков паролей, который будет запрашивать диапазон длины пароля (от скольки до скольки символов), какие символы должны входить в пароль, 
а так же количество паролей.
На выходе должен получаться список с необходимым количеством паролей и в соответствии с запросом пользователя.
"""

import random

alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
special = "!@#$%^&*"
alphabet_upper = alphabet_lower.upper()

pass_length_from = int(input("От скольки символов создать пароль: "))
pass_length_to = int(input("До скольки символов создать пароль: "))

pass_content_small_letters = input("Добавлять ли строчные буквы в пароль? Ответьте 'да' или 'нет': ")
pass_content_big_letters = input("Добавлять ли прописные буквы в пароль? Ответьте 'да' или 'нет': ")
pass_content_numbers = input("Добавлять ли цифры в пароль? Ответьте 'да' или 'нет': ")
pass_content_symbols = input("Добавлять ли спецсимволы в пароль? Ответьте 'да' или 'нет': ")

pass_number = int(input("Сколько паролей создать: "))

password_list = []
pass_counter = 0

while pass_counter < pass_number:
    pass_counter += 1
    random_length = random.randint(pass_length_from, pass_length_to)
    password = ""

    while len(password) < random_length:
        if pass_content_small_letters == 'да' and random.randint(0, 1):
            password += random.choice(alphabet_lower)
        if pass_content_big_letters == 'да' and random.randint(0, 1):
            password += random.choice(alphabet_upper)
        if pass_content_numbers == 'да' and random.randint(0, 1):
            password += random.choice(numbers)
        if pass_content_symbols == 'да' and random.randint(0, 1):
            password += random.choice(special)

    password_list.append(password)

print(password_list)


print('-' * 50)


# задание 5

"""
Создайте программу которая генерирует рандомный газ, при этом газ с вероятностью 50% должен увеличиваться или уменьшаться на 1 единицу раз в секунду.
Программа должна замерять газ за минуту и выводить его в виде списка, а так же печатать среднее значение газа за последнюю минуту.
"""

import random
import time

random_gas = random.randint(1, 100)
gas_list = []
time_counter = 0

print(f"Начинаем с газа: {random_gas}")

while time_counter <= 60:
    time_counter += 1
    time.sleep(1)
    if random.randint(0, 1):
        random_gas += 1
    else:
        random_gas -= 1
    gas_list.append(random_gas)
    print(random_gas)
    print(gas_list)
    print("...1 сек...")

average_gas = sum(gas_list) / len(gas_list)

print(gas_list)
print(average_gas)


print('-' * 50)


# задание 6
"""
Создайте список из 10 разных активностей. Программа должна спрашивать сколько транзакций нужно выполнить.
Создайте программу которая будет рандомно выбирать одну из активностей и выполнять ее (печатать в консоль), после рандомной паузы повторяет 
пока не сделает запрошенное количество транзакций.

HARD LEVEL: 
доработай программу так чтобы она печатала сколько раз была выполнена каждая активность.
"""

import random

activities = ["swap", "bridge", "mint", "claim", "deposit", "withdraw", "deploy", "donate", "sell", "buy"]

target = int(input("Сколько раз сегодня активничаем: "))
counter = 0

while counter < target:
    counter += 1
    print("Делаем", random.choice(activities))


print('-' * 50)