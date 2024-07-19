print("-" * 50)


# задание 1
"""
Напишите программу, которая проверяет, является ли введенное число в терминале четным и положительным.
все иные ситуации должны так же отрабатываться и писаться в терминале.
Например, если число нечетное и положительное, нечетное и отрицательное и т.д.
На любое число должен быть верный вывод
"""

number = int(input("Введите свое число: "))

print(f"Ваше число: {number}, оно {'четное' if number % 2 == 0 else 'нечетное'} и {'положительное' if number >= 0 else 'отрицательное'}.")


print("-" * 50)


# задание 2

"""
Напишите программу, генератор паролей, которая на входе спрашивает:
1) длину пароля от 5 до 8 символов, если введено число меньше 5 или больше 8, то генерируется случайное
число между 5 и 8
2) надо ли включать в пароль цифры, принимая ответ 'да' или 'нет'
3) надо ли включать в пароль прописные буквы, принимая ответ 'да' или 'нет' 
4) надо ли включать в пароль строчные буквы, принимая ответ 'да' или 'нет'
5) надо ли включать в пароль спецсимволы, принимая ответ 'да' или 'нет'

Всего программа должна задать 5 вопросов и получить ответы в терминале
Программа должна генерировать случайный пароль имеющий нужную длину и все выбранные символы, 
порядок символов или повторение не имеет значения.
Используйте вложенные операторы.
Попробуйте сгенерировать пароль из 5 символов с 4 включенными параметрами.
Попробуйте сгенерировать пароль из 8 символов с 1 включенным параметром (например только из цифр).
Если хотите сделать вариант с использованием цикла, сдавайте 2 варианта решения, с циклом и без.

Не пугайтесь если ваш код будет получаться очень большим и будет много повторяющихся элементов, 
на данном этапе это нормально.
"""

import random

password_length = int(input("Введите длину пароля (от 5 до 8): "))
password_length = password_length if 5 <= password_length <= 8 else random.randint(5, 8)

small_letters = "abcdefghijklmnopqrstuvwxyz"
big_letters = small_letters.upper()
numbers = "0123456789"
symbols = "!@№#%$:%,^.&;*()"

small_letters_in_password = input("Нужно ли включить в пароль строчные буквы? Ответь 'да' или 'нет': ") == "да"
big_letters_in_password = input("Нужно ли включить в пароль прописные буквы? Ответь 'да' или 'нет': ") == "да"
numbers_in_password = input("Нужно ли включить в пароль цифры? Ответь 'да' или 'нет': ") == "да"
symbols_in_password = input("Нужно ли включить в пароль символы? Ответь 'да' или 'нет': ") == "да"

password = ''

if len(password) < password_length:
    if small_letters_in_password:
        password += random.choice(small_letters)
    if big_letters_in_password:
        password += random.choice(big_letters)
    if numbers_in_password:
        password += random.choice(numbers)
    if symbols_in_password:
        password += random.choice(symbols)

    if len(password) < password_length:
        if small_letters_in_password:
            password += random.choice(small_letters)
        if big_letters_in_password:
            password += random.choice(big_letters)
        if numbers_in_password:
            password += random.choice(numbers)
        if symbols_in_password:
            password += random.choice(symbols)

        if len(password) < password_length:
            if small_letters_in_password:
                password += random.choice(small_letters)
            if big_letters_in_password:
                password += random.choice(big_letters)
            if numbers_in_password:
                password += random.choice(numbers)
            if symbols_in_password:
                password += random.choice(symbols)

            if len(password) < password_length:
                if small_letters_in_password:
                    password += random.choice(small_letters)
                if big_letters_in_password:
                    password += random.choice(big_letters)
                if numbers_in_password:
                    password += random.choice(numbers)
                if symbols_in_password:
                    password += random.choice(symbols)

                if len(password) < password_length:
                    if small_letters_in_password:
                        password += random.choice(small_letters)
                    if big_letters_in_password:
                        password += random.choice(big_letters)
                    if numbers_in_password:
                        password += random.choice(numbers)
                    if symbols_in_password:
                        password += random.choice(symbols)

                    if len(password) < password_length:
                        if small_letters_in_password:
                            password += random.choice(small_letters)
                        if big_letters_in_password:
                            password += random.choice(big_letters)
                        if numbers_in_password:
                            password += random.choice(numbers)
                        if symbols_in_password:
                            password += random.choice(symbols)

                        if len(password) < password_length:
                            if small_letters_in_password:
                                password += random.choice(small_letters)
                            if big_letters_in_password:
                                password += random.choice(big_letters)
                            if numbers_in_password:
                                password += random.choice(numbers)
                            if symbols_in_password:
                                password += random.choice(symbols)

                            if len(password) < password_length:
                                if small_letters_in_password:
                                    password += random.choice(small_letters)
                                if big_letters_in_password:
                                    password += random.choice(big_letters)
                                if numbers_in_password:
                                    password += random.choice(numbers)
                                if symbols_in_password:
                                    password += random.choice(symbols)

print(f"Ваш пароль: {password}")


print("-" * 50)


# задание 3

"""
Напишите программу которая генерирует:
случайный газ от 15 до 25 (не включительно)
случайный баланс от 0 до 2 (не включительно)
случайное количество транзакций в кошельке от 0 до 3 (не включительно)

Если баланс нулевой делаем вывод с биржи рандомной суммы от 1 до 2. 
Используйте оператор not и прибавляем к балансу.

Далее при помощи тернарного оператора программа кладет в
переменную активность которую нужно делать:
Если газ ниже или равно 20 - кладем активность 'Bridge',
Если газ выше 20 - кладем активность 'Swap'
Далее программа должна используя условный оператор проверить что мы 
должны делать и выполнить нужное действия вычитая его цену из баланса,
отработайте ситуацию в случае если не будет хватать баланса на бридж, 
нужно будет добавить проверку баланса и возможность вывода недостающей суммы на баланс
и напечатать сообщение о проделанной работе.
Бридж стоит 2, свап стоит 1.

Вам нужно сделать программу, которая делает чтобы на кошельке было всего 5 транзакций
с учетом изначально сгенерированного кол-ва транз. транзакции каждый раз выбираться 
в зависимости от газа в конкретный момент.
Перед каждой операцией нужно генерировать новое значение стоимости газа.
Учитывайте вариант, что баланс может быть нулевым и нужно будет сделать вывод с биржи.
Учитывайте что вам нужно сделать 5 операций, но не более.
Учитывайте что на старте количество транзакций в кошельке может быть 0.

Попробуйте реализовать без циклов и функций.
Либо сделайте несколько решений, в одном из которых вы будете использовать
только то что проходили.
"""

import random

gas = random.randint(15, 25)
balance = random.randint(0, 2)
transaction_number = random.randint(0, 3)
transaction_target = 5

activity = 'Bridge' if gas <= 20 else 'Swap'

if not balance:
    withdrawal = random.randint(1,2)
    balance += withdrawal
    print(f"Ваш баланс равен нулю, сейчас выведем {withdrawal} с биржи")
    print(f"Баланс: {balance}")

if activity == 'Bridge':
    if balance < 2:
        difference = 2 - balance
        balance += difference
        print(f"У вас не хватает средств для выполнения Bridge, сейчас выведем {difference}")
        print(f"Баланс: {balance}")

    balance -= 2
    transaction_number += 1
    print(f"Мы сделали Bridge! Текущее кол-во транзакций на кошельке: {transaction_number}/{transaction_target}")
    print(f"Баланс: {balance}")

else:
    balance -= 1
    transaction_number += 1
    print(f"Мы сделали Swap! Текущее кол-во транзакций на кошельке: {transaction_number}/{transaction_target}")
    print(f"Баланс: {balance}")


if transaction_number < transaction_target:
    if not balance:
        withdrawal = random.randint(1, 2)
        balance += withdrawal
        print(f"Ваш баланс равен нулю, сейчас выведем {withdrawal} с биржи")
        print(f"Баланс: {balance}")

    gas = random.randint(15, 25)
    activity = 'Bridge' if gas <= 20 else 'Swap'

    if activity == 'Bridge':
        if balance < 2:
            difference = 2 - balance
            balance += difference
            print(f"У вас не хватает средств для выполнения Bridge, сейчас выведем {difference}")
            print(f"Баланс: {balance}")

        balance -= 2
        transaction_number += 1
        print(f"Мы сделали Bridge! Текущее кол-во транзакций на кошельке: {transaction_number}/{transaction_target}")
        print(f"Баланс: {balance}")

    else:
        balance -= 1
        transaction_number += 1
        print(f"Мы сделали Swap! Текущее кол-во транзакций на кошельке: {transaction_number}/{transaction_target}")
        print(f"Баланс: {balance}")

    if transaction_number < transaction_target:
        if not balance:
            withdrawal = random.randint(1, 2)
            balance += withdrawal
            print(f"Ваш баланс равен нулю, сейчас выведем {withdrawal} с биржи")
            print(f"Баланс: {balance}")

        gas = random.randint(15, 25)
        activity = 'Bridge' if gas <= 20 else 'Swap'

        if activity == 'Bridge':
            if balance < 2:
                difference = 2 - balance
                balance += difference
                print(f"У вас не хватает средств для выполнения Bridge, сейчас выведем {difference}")
                print(f"Баланс: {balance}")

            balance -= 2
            transaction_number += 1
            print(
                f"Мы сделали Bridge! Текущее кол-во транзакций на кошельке: {transaction_number}/{transaction_target}")
            print(f"Баланс: {balance}")

        else:
            balance -= 1
            transaction_number += 1
            print(
                f"Мы сделали Swap! Текущее кол-во транзакций на кошельке: {transaction_number}/{transaction_target}")
            print(f"Баланс: {balance}")

        if transaction_number < transaction_target:
            if not balance:
                withdrawal = random.randint(1, 2)
                balance += withdrawal
                print(f"Ваш баланс равен нулю, сейчас выведем {withdrawal} с биржи")
                print(f"Баланс: {balance}")

            gas = random.randint(15, 25)
            activity = 'Bridge' if gas <= 20 else 'Swap'

            if activity == 'Bridge':
                if balance < 2:
                    difference = 2 - balance
                    balance += difference
                    print(f"У вас не хватает средств для выполнения Bridge, сейчас выведем {difference}")
                    print(f"Баланс: {balance}")

                balance -= 2
                transaction_number += 1
                print(
                    f"Мы сделали Bridge! Текущее кол-во транзакций на кошельке: {transaction_number}/{transaction_target}")
                print(f"Баланс: {balance}")

            else:
                balance -= 1
                transaction_number += 1
                print(
                    f"Мы сделали Swap! Текущее кол-во транзакций на кошельке: {transaction_number}/{transaction_target}")
                print(f"Баланс: {balance}")

            if transaction_number < transaction_target:
                if not balance:
                    withdrawal = random.randint(1, 2)
                    balance += withdrawal
                    print(f"Ваш баланс равен нулю, сейчас выведем {withdrawal} с биржи")
                    print(f"Баланс: {balance}")

                gas = random.randint(15, 25)
                activity = 'Bridge' if gas <= 20 else 'Swap'

                if activity == 'Bridge':
                    if balance < 2:
                        difference = 2 - balance
                        balance += difference
                        print(f"У вас не хватает средств для выполнения Bridge, сейчас выведем {difference}")
                        print(f"Баланс: {balance}")

                    balance -= 2
                    transaction_number += 1
                    print(
                        f"Мы сделали Bridge! Текущее кол-во транзакций на кошельке: {transaction_number}/{transaction_target}")
                    print(f"Баланс: {balance}")

                else:
                    balance -= 1
                    transaction_number += 1
                    print(
                        f"Мы сделали Swap! Текущее кол-во транзакций на кошельке: {transaction_number}/{transaction_target}")
                    print(f"Баланс: {balance}")


print("-" * 50)