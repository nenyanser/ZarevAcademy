"""
Домашнее задание по list
"""


# задание 1

"""
Программа спрашивает у пользователя сколько кошельков нужно сгенерировать.
Программа генерирует список выбранного количества случайных кошельков.
Кошельки должны иметь адрес как настоящие кошельки в формате "0x" + 40 случайных символов из набора "abcdef0123456789" (16-ричная система исчисления).
Программа спрашивает сколько дропов нужно раздать.
Программа рандомно раздает дропы на кошельки, eсли кошелек уже получил дроп, то он НЕ может получить его повторно.
В конце программа должна вывести список кошельков которые получили под дроп, каждый кошелек с новой строки.
Далее программа должна заклеймить дроп с каждого кошелька:
- клейм должен происходить в рандомном порядке с рандомной паузой, чтобы не связать кошельки
- клейм должен быть только у кошельков с дропом
- 1 кошелек должен клеймить дроп только 1 раз

Далее программа должна создать список субкошельков на бирже по количеству кошельков с дропами.
Программа должна в рандомном порядке вывести токены с кошельков на кошельки субаккаунтов.
Важно соблюдать правило что 1 кошелек может вывести токены только на 1 кошелек субаккаунта, иначе кошельки свяжутся.
"""


print("-" * 50)


import random
import time

number_of_wallets = int(input('Сколько кошельков нужно сгенерировать: '))
number_of_drops = int(input('Сколько дропов нужно раздать: '))
wallet_counter = 0
symbols_counter = 0
eligible_counter = 0
process_counter = 0
subaccount_counter = 0
one_more_counter = 0
random_wallet = ''
wallet_list = []
eligible_list = []
subaccount_list = []

while wallet_counter < number_of_wallets:
    wallet_counter += 1
    while symbols_counter <= 40:
        symbols_counter += 1
        random_symbol = random.choice("abcdef0123456789")
        random_wallet += random_symbol
    random_wallet = "0x" + random_wallet
    wallet_list.append(random_wallet)
    symbols_counter = 0
    random_wallet = ''

while eligible_counter < number_of_wallets and number_of_drops > 0:
    if random.randint(0, 1):
        eligible_list.append(wallet_list[eligible_counter])
        wallet_list.remove(wallet_list[eligible_counter])
        number_of_drops -= 1
    else:
        eligible_counter += 1

    if eligible_counter >= len(wallet_list):
        eligible_counter = 0

while process_counter < len(eligible_list):
    random_wallet = eligible_list[process_counter]
    print(f"Кошелек {random_wallet} получил дроп")
    random_time = random.randint(1, 5)
    print(f"Задержка {random_time} сек...")
    time.sleep(random_time)
    print(f"Клеймим дроп с кошелька {random_wallet}")
    print('-' * 50)
    process_counter += 1

while subaccount_counter < len(eligible_list):
    symbols_counter = 0
    random_wallet = ''
    while symbols_counter < 40:
        symbols_counter += 1
        random_symbol = random.choice("abcdef0123456789")
        random_wallet += random_symbol
    random_wallet = "0x" + random_wallet
    subaccount_list.append(random_wallet)
    subaccount_counter += 1

while one_more_counter < len(eligible_list) and one_more_counter < len(subaccount_list):
    random_wallet = eligible_list[one_more_counter]
    random_subaccount = subaccount_list[one_more_counter]
    print(f"Выводим дроп с кошелька {random_wallet} на субаккаунт {random_subaccount}")
    one_more_counter += 1


# задание 2
"""
Создайте список с рандомными активностями
Создайте список из 10 кошельков, кошельки должны иметь адрес как настоящие кошельки в формате "0x" + 40 случайных символов из набора "abcdef0123456789" (16-ричная система исчисления).
Программа должна брать рандомный кошелек и выполнять активности в рандомном порядке.
Нужно чтобы отработали все кошельки, все активности по 1 разу.
"""


print("-" * 50)


import random

activities = ["swap", "bridge", "deploy", "buy", "sell"]
wallet_list = []
random_wallet = ''

wallet_counter = 0
symbols_counter = 0

while wallet_counter < 10:
    wallet_counter += 1
    while symbols_counter <= 40:
        symbols_counter += 1
        random_symbol = random.choice("abcdef0123456789")
        random_wallet += random_symbol
    random_wallet = "0x" + random_wallet
    wallet_list.append(random_wallet)
    symbols_counter = 0
    random_wallet = ''

while wallet_list:
    random_wallet = random.choice(wallet_list)
    activities_copy = activities.copy()
    while activities_copy:
        random_activity = random.choice(activities_copy)
        print(f"Кошелек {random_wallet} делает {random_activity}")
        activities_copy.remove(random_activity)
    wallet_list.remove(random_wallet)


# задание 3

"""
Создайте список из 10 кошельков, кошельки должны иметь адрес как настоящие кошельки в формате "0x" + 40 случайных символов из набора "abcdef0123456789" (16-ричная система исчисления).
Создайте список в котором будут храниться счетчики транзакций по каждому кошельку (изначально сгенерированные случайно от 0 до 3. Каждый счетчик имеет такой же индекс в списке как и кошелек.
Программа должна спрашивать у пользователя сколько минимально транзакций нужно выполнить на кошельках.
Программа должна выбирать:
- либо рандомный кошелек для транзакции и выполнять от 1 до 5 транзакций, увеличивая счетчик транзакций.
- либо кошелек с самым маленьким количеством транзакций и выполнять от 1 до 5 транзакций, увеличивая счетчик транзакций.

Программа должна завершиться когда все кошельки сделают минимальное количество транзакций. Между транзакциями делайте паузу.
"""


print("-" * 50)


import random
import time

symbols_counter = 0
process_counter = 0
random_wallet = ''
wallet_list = []
counter_list = []

while len(wallet_list) < 10:
    while symbols_counter < 40:
        symbols_counter += 1
        random_symbol = random.choice("abcdef0123456789")
        random_wallet += random_symbol
    random_wallet = "0x" + random_wallet
    wallet_list.append(random_wallet)
    symbols_counter = 0
    random_wallet = ''

while len(counter_list) < 10:
    counter = random.randint(0, 3)
    counter_list.append(counter)

transactions = int(input(f"Какое минимальное количество транзакций нужно выполнить: "))

while min(counter_list) < transactions:
    if random.randint(0, 1):
        randomize = random.randint(0, len(wallet_list) - 1)
        wallet_index = randomize
    else:
        wallet_index = counter_list.index(min(counter_list))

    random_wallet = wallet_list[wallet_index]
    random_counter = counter_list[wallet_index]
    random_trx = random.randint(1, 5)
    random_counter += random_trx
    counter_list[wallet_index] = random_counter
    print(f"На кошельке {random_wallet} сейчас {random_counter} транзакций. Выполняем {random_trx} транзакций.")
    process_counter += 1

print("Все кошельки выполнили минимальное количество транзакций.")