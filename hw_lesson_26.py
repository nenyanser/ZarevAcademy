"""
Домашнее задание по function
"""

# задание 1

"""
Создать функцию которая принимает 1 аргумент gas_limit, в функции в цикле должен генерироваться рандомный газ от 10 до 50
Если газ выше чем gas_limit, то функция должна вставать на паузу 0,1 секунду и писать уведомление в терминал,
если сгенерированный газ меньше чем gas_limit, то функция печатает "можно работать" и завершает работу.
"""

import time
import random

def gas_limit(gas_limit):
    while True:
        gas_price = random.randint(10, 50)
        if gas_price > gas_limit:
            time.sleep(0.1)
            print(f"Сгенерированный газ - {gas_price}, что выше чем gas лимит. Генерируем новый...")
        else:
            print(f"Газ {gas_price}, можно работать")
            break


# задание 2

"""
Создать функцию генератор паролей, которая принимает 4 аргумента: длину пароля, а так же 3 аргумента bool (true/false):
1. использовать ли латинские буквы
2. использовать ли цифры
3. использовать ли спец символы
Функция должна генерировать пароль с использованием выбранных символов и печатать его в терминале.
"""

def password_generator(password_length, use_letters=True, use_digits=True, use_symbols=True):
    letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "1234567890"
    symbols = "№%@#$%^&*"

    using_chars = ""
    if use_letters:
        using_chars += letters
    if use_digits:
        using_chars += digits
    if use_symbols:
        using_chars += symbols

    password = "".join(random.choice(using_chars) for _ in range(password_length))
    return password


# задание 3

"""
Создать функцию генератор кошельков, которая принимает 1 аргумент, количество кошельков и генерирует список из нужного количества кошельков
в формате "0x" + 40 случайных символов из набора "abcdef0123456789" (16-ричная система исчисления).
Итоговый список должен быть сохранен в через глобальную переменную wallets снаружи функции, чтобы полученный список можно было использовать вне функции.
"""

def wallet_generator(wallets_number):
    return ["0x" + "".join(random.choice("abcdef0123456789") for _ in range(40)) for _ in range(wallets_number)]


# задание 4

"""
Создать функцию вывода с биржи, на вход должна получать адрес кошелька и минимальный баланс, внутри должен проходить псевдо запрос баланса (генерируем рандомно), 
если баланс ниже минимальной суммы делать вывод на кошелек рандомной суммы и напечатать сообщение об этом.
"""

def withdrawal_generator(wallet_address, min_balance):
    balance = random.randint(1, 100)
    if balance < min_balance:
        random_withdrawal = random.randint(1, 100)
        balance += random_withdrawal
        print(f"Вывели на кошелек {random_withdrawal}, так как баланс был ниже минимального")
    print(f"Актуальный баланс кошелька {wallet_address}: {balance}")


# задание 5

"""
Используя созданные функции создайте программу, которая:
создает список кошельков
Потом в цикле перебирает список кошельков и делает следующее:
Печатает название кошелька.
Генерирует новый пароль при помощи функции и печатает его в терминале.
Ждет когда газ будет меньше 30 и печатает уведомление в терминале.
Проверяет баланс кошелька, если баланс меньше 1000 делает вывод на кошелек рандомной суммы.

Функции должны быть определены в верхней части программы, логика программы и вызов функций в нижней части.
"""

wallets_list = wallet_generator(10)

for wallet in wallets_list:
    print(f"Кошелек: {wallet}")
    password = password_generator(8, True, True, True)
    print(f"Ваш пароль: {password}")
    gas_limit(30)
    withdrawal_generator(wallet, 1000)
    print("-" * 50)