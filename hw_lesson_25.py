"""
Домашнее задание по dict
"""

# задание 1

"""
Программа на входе спрашивает сколько кошельков сделать и пользователь в терминале вводит число.
Программа создает список кошельков по введенному количеству (реализуйте одной строчкой кода).
Программа создает список балансов кошельков, где баланс это случайное число от 1 до 1000 (реализуйте одной строчкой кода).
Должно получиться 2 списка.
Объедините 2 списка в словарь, где ключ это кошелек, а значение это баланс.
Сделайте программу, которая будет умножать на 2 все четные значения балансов.
Выведите конечный результат в формате "Кошелек {адрес}: баланс {баланс}", каждый элемент с новой строки.
"""

import random

number_of_wallet = int(input("Сколько сделать кошельков: "))
wallets_list = ["0x" + "".join([random.choice("abcdef0123456789") for _ in range(40)]) for _ in range(number_of_wallet)]
balances_list = [random.randint(1, 1000) for _ in range(number_of_wallet)]
my_dictionary = dict(zip(wallets_list, balances_list))

for wallet, balance in my_dictionary.items():
    if balance % 2 == 0:
        my_dictionary[wallet] = balance * 2

for wallet, balance in my_dictionary.items():
    print(f'Кошелек {wallet}: баланс {balance}')


print('-' * 50)


# задание 2

"""
НЕ ПАДАЙТЕ В ОБМОРОК

Пользователь вводит в терминале количество кошельков, минимальное количество транзакций (должно быть равно или больше).
В программе должен быть создан словарь со списком 3 активностей и их РАНДОМНОЙ стоимостью от 10 до 100 единиц
(стоимость указывается в единицах газа):
swap = 30 (замените на рандомное число от 10 до 100 единиц)
mint_nft = 50 (замените на рандомное число от 10 до 100 единиц)
burn_nft = 65 (замените на рандомное число от 10 до 100 единиц)
Программа создает словарь в котором ключами являются адреса кошельков, а значением словарь в котором:
- словарь с балансами, где ключ это название токена, а значение количество токена, должен быть 2 токена
-- ETH баланс рандомно от 0,2 до 0,8.
-- USDC баланс рандомно от 0 до 50.
- общее количество транзакций - изначально по 0.
- словарь с транзакциями, где ключ это название транзакции, а значение количества транзакции, изначально по 0.

Программа должна ждать когда будет рабочий газ ниже 30, при этом газ каждую 0,1 секунды обновляется, рандомно увеличиваясь или уменьшаясь на 1,
газ не может быть меньше 10 или больше 50, если он достигает этих значений он должен начать двигаться в противоположную сторону.

Если газ достиг нужного значения, программа должна запустить в работу кошелек.

Кошелек должен выбираться рандомно, среди тех, которые еще не достигли целевого количества транзакций.

Кошелек должен выбирать рандомную активность, отдавая предпочтения тем которые имеют 0 транзакций.
Все транзакции оплачиваются в токене ETH.
Стоимость транзакции считается по формуле (газ * цена транзакции в еденицах газа / 10000).
Если на балансе недостаточно денег для выполнения транзакции нужно сделать вывод с биржи суммы равной транзакции умноженной на 2 + рандомный %,
чтобы сумма вывода была всегда рандомная.

Программа должна ждать когда будет рабочий газ ниже 30, при этом газ каждую 0,1 секунды обновляется, рандомно увеличиваясь или уменьшаясь на 1,
газ не может быть меньше 10 или больше 50, если он достигает этих значений он должен начать двигаться в противоположную сторону.

Если газ достиг нужного значения, программа должна запустить в работу кошелек.

Кошелек должен выбираться рандомно, среди тех, которые еще не достигли целевого количества транзакций.

Кошелек должен выбирать рандомную активность, отдавая предпочтения тем которые имеют 0 транзакций.
Все транзакции оплачиваются в токене ETH.
Стоимость транзакции считается по формуле (газ * цена транзакции в еденицах газа / 10000).
Если на балансе недостаточно денег для выполнения транзакции нужно сделать вывод с биржи суммы равной транзакции умноженной на 2 + рандомный %,
чтобы сумма вывода была всегда рандомная.
Если выбранная транзакция mint_nft или burn_nft, то нужно только потратить деньги с баланса ETH на комиссию и записать транзакцию в общий счетчик транзакций
и счетчик конкретной активности.

Если транзакция swap нужно сделать обмен обмен:
- если баланс USDC нулевой, то ETH на USDC, рандомную сумму в пределах баланса за вычетом комиссии
- если баланс USDC НЕ нулевой, то все USDC меняем на ETH
Стоимость ETH в USDC должна генерироваться в момент обмена в диапазоне от 2000 до 3000.
Балансы кошелька в обоих токенах должны быть обновлены после обмена.
Не забудьте списать стоимость транзакции с баланса, а так же записать транзакцию в общий счетчик транзакций
и счетчик конкретной активности.

После транзакции ожидайте рандомную паузу от 0,5 до 1,5 секунд перед выбором следующего кошелька.

Программа должна завершиться когда все кошельки сделают минимальное количество транзакций.
Программа должна напечатать в терминале перечисление итоговых данных по всем кошелькам в формате:
Кошелек {адрес}:
--- Баланс ETH: {количество токена}
--- Баланс USDC: {количество токена}
--- Количество транзакций: {количество}
--- Количество транзакций swap: {количество}
--- Количество транзакций mint_nft: {количество}
--- Количество транзакций burn_nft: {количество}

В данной задаче нужно будет гуглить, использовать чат жпт, пытайтесь решать задачу кусками, попробуйте реализовать одну часть, а потом другую.
Можете реализовать не все задания из задачи, но попробуйте.
"""


import random
import time

number_of_wallets = int(input("Сколько кошельков сделать: "))

while True:
    number_of_transactions = int(input("Сколько минимально сделать транзакций: "))
    if not number_of_transactions >= number_of_wallets:
        print(
            f"Я не могу сделать {number_of_transactions} транзакций, потому как их должно быть столько же или больше, сколько и кошельков. Сейчас кошельков: {number_of_wallets}. Давай попробуем еще раз.")
        continue
    break

activities_list = ["swap", "mint_nft", "burn_nft"]
costs_list = [random.randint(10, 100) for _ in range(len(activities_list))]
my_dictionary = dict(zip(activities_list, costs_list))

wallets_list = ["0x" + "".join([random.choice("abcdef0123456789") for _ in range(40)]) for _ in
                range(number_of_wallets)]

another_dictionary = {}

for wallet in wallets_list:
    balances_dict = {"ETH": random.uniform(0.2, 0.8), "USDC": random.randint(0, 50)}
    summary_transactions = 0
    value_dict = {"swap": 0, "mint_nft": 0, "burn_nft": 0}

    another_dictionary[wallet] = {
        "balances": balances_dict,
        "transactions": summary_transactions,
        "activities": value_dict
    }

wallets = list(another_dictionary.keys())

gas_limit = 30
gas_price = random.randint(10, 50)

while True:

    if not wallets:
        print("Все кошельки выполнили минимальное количество транзакций.")
        break

    wallet = random.choice(wallets)

    while gas_price >= gas_limit:
        gas_price += random.choice([-1, 1])
        if gas_price <= 10:
            gas_price = 11
        elif gas_price >= 50:
            gas_price = 49

        print(f"Газ: {gas_price}")
        time.sleep(0.1)

    print(f"Газ достиг нужного значения: {gas_price}. Начинаем работу.")

    activities = another_dictionary[wallet]["activities"]
    if all(activities.values()) or not any(activities.values()):
        activity = random.choice(list(activities.keys()))
    else:
        zero_activities = [activity for activity in activities if not activities[activity]]
        activity = random.choice(zero_activities)

    price_activity = (my_dictionary[activity] * gas_price) / 10000
    current_balance = another_dictionary[wallet]["balances"]["ETH"]

    if current_balance < price_activity:
        withdrawal_amount = price_activity * 2 * random.uniform(1.1, 1.2)
        another_dictionary[wallet]["balances"]["ETH"] += withdrawal_amount
        print(f"Кошелек {wallet} вывел {withdrawal_amount} ETH с биржи для выполнения транзакции {activity}")

    if activity == "swap":
        eth_usdc_price = random.randint(2000, 3000)
        if another_dictionary[wallet]["balances"]["USDC"] > 0:
            usdc_to_swap = another_dictionary[wallet]["balances"]["USDC"]
            eth_received = usdc_to_swap / eth_usdc_price
            another_dictionary[wallet]["balances"]["ETH"] += eth_received
            another_dictionary[wallet]["balances"]["USDC"] = 0
        else:
            swap_amount = random.uniform(0, another_dictionary[wallet]["balances"]["ETH"] - price_activity)
            another_dictionary[wallet]["balances"]["ETH"] -= swap_amount
            another_dictionary[wallet]["balances"]["USDC"] += swap_amount * eth_usdc_price

    another_dictionary[wallet]["balances"]["ETH"] -= price_activity
    another_dictionary[wallet]["transactions"] += 1
    another_dictionary[wallet]["activities"][activity] += 1

    print(f"Кошелек {wallet} выполнил активность {activity} за {price_activity} ETH")

    if another_dictionary[wallet]["transactions"] >= number_of_transactions:
        wallets.remove(wallet)

    gas_price += random.choice([-1, 1])
    if gas_price <= 10:
        gas_price = 11
    elif gas_price >= 50:
        gas_price = 49

    time.sleep(random.uniform(0.5, 1.5))

print("Итоговые данные по кошелькам:")

for wallet, data in another_dictionary.items():
    print(f"Кошелек {wallet}:")
    print(f"--- Баланс ETH: {data['balances']['ETH']}")
    print(f"--- Баланс USDC: {data['balances']['USDC']}")
    print(f"--- Количество транзакций: {data['transactions']}")
    print(f"--- Количество транзакций swap: {data['activities']['swap']}")
    print(f"--- Количество транзакций mint_nft: {data['activities']['mint_nft']}")
    print(f"--- Количество транзакций burn_nft: {data['activities']['burn_nft']}")


print('-' * 50)

print('Честно признаюсь, что примерно 2/3 сделал сам, но потом просто запутался, мозг перестал понимать что происходит и доделал с чатгпт.')