"""
Домашнее задание по for
"""

# задание 1

"""
Создайте список из 5 разных крипто активностей.
Программа создает список 100 кошельков с адресами в формате "0x" + 40 случайных символов из набора "abcdef0123456789".
Программа создает список балансов кошельков, которые изначально равны 0.
Программа создает список количества транзакций кошельков, которые изначально равны 0.
Программа должна сделать ровно 10 рандомных транзакций из списка активностей на каждом кошельке, по одной транзакции за 1 раз. Активности могут повторяться.
Кошельки могут отрабатываться по порядку, без рандомизации.
Если баланс кошелька нулевой программа должна выводить с биржи от 1 до 3 токенов и прибавлять к балансу.
Стоимость одной транзакции - активности = от 1 до 2 токенов (рандомно). Если денег на транзакцию не хватает,
программа должна выводить не хватающую сумму и прибавлять к балансу перед осуществлением транзакции.
Нужно печатать информацию о каждой транзакции и минусовать из баланса стоимость транзакции.
"""

print('-' * 50)


import random

activities = ['swap', 'mint', 'claim', 'deploy', 'send']
random_wallet = '0x'
address_list = []
balance_list = []
transaction_list = []

for wallets in range(0, 100):
    for wallet in range(40):
        random_wallet += random.choice("abcdef0123456789")
    address_list.append(random_wallet)
    random_wallet = '0x'

for balances in range(0, 100):
    balance_list.append(0)

for transactions in range(0, 100):
    transaction_list.append(0)

for index, wallet in enumerate(address_list):  # Если нужно чередовать кошельки, а не транзакции, можно поменять внутренний и внешний циклы местами
    print(f"\nРаботаем с кошельком {wallet}:")
    for _ in range(10):
        if not balance_list[index]:
            random_withdrawal = random.randint(1, 3)
            print(f'Кошелек пуст, выводим {random_withdrawal}')
            balance_list[index] += random_withdrawal
        transaction_cost = random.randint(1, 2)
        if balance_list[index] < transaction_cost:
            difference = transaction_cost - balance_list[index]
            print(f"Для выполнения транзы нужно {transaction_cost}, но на кошельке {balance_list[index]}. Выводим разницу с биржи...")
            balance_list[index] += difference
        random_activity = random.choice(activities)
        balance_list[index] -= transaction_cost
        print(f"Выполняем {random_activity} за {transaction_cost}, баланс: {balance_list[index]}")
        transaction_list[index] += 1


# задание 2

"""
Реализуйте программу ниже с помощью 3 строчек кода используя однострочное создание списков.

Сгенерируйте список из 100 паролей длиной 8 символов, состоящих из цифр и маленьких букв - одной строкой кода. (подсказка: используйте random.choices)
Сгенерируйте второй список с теми же паролями, только буквы большие. (используйте исходный список паролей за основу) - одной строкой кода
Сгенерируйте третий список в котором будут лежать пароли из 2 списка в верхнем регистре у которых есть буква "D" - одной строкой кода.
"""

print('-' * 50)


password_list = [''.join(random.choices("abcdef0123456789", k=8)) for _ in range(100)]
password_list_upper = [password.upper() for password in password_list]
password_list_with_d = [password for password in password_list_upper if "D" in password]

print(password_list)
print(password_list_upper)
print(password_list_with_d)


print('-' * 50)






















































































































print(f'Спасибо тебе огромное, что проверяешь мои домашки, несмотря на то, как сильно я отстал от потока. \nЧестно говоря, я думал пройти этот путь уже самостоятельно, ориентируясь по готовым материалам. \nДля меня это был большой сюрприз и это очень приятно, что про тебя не забывают, даже несмотря на то, что ты сам проебался :)')