print("-" * 50)


# задание 1
"""
Напишите программу, которая будет запрашивать ввести баланс
кошелька в терминале и выводить сообщение о том, кем является
владелец кошелька с таким балансом:
0 = нищий
от 1 до 100 = нормис
от 101 до 1000 = деген
от 1001 до 10000 = кит
от 10001 и выше = Илон Маск
"""

balance = int(input("Введите свой баланс: "))

if balance == 0:
    print("Ты нищий")

elif 1 <= balance <= 100:
    print("Ты нормис")

elif 101 <= balance <= 1000:
    print("Ты деген")

elif 1001 <= balance <= 10000:
    print("Ты кит")

elif balance >= 10001:
    print("Ты Илон Макс")

else:
    print("Ты ввел какую-то хуйню, будем считать, что ты бомж.")


print("-" * 50)


# задание 2
"""
Напишите программу, которая генерирует цену на газ (от 10 до 100) и начальный баланс кошелька (от 2000 до 10000).

Стоимость операций:

- мост Scroll стоит = цена газа * 75
- свап внутри Scroll стоит = цена газа * 40
- минт домена Clusters стоит = цена газа * 100

Если на кошельке недостаточно средств для операций, программа должна сначала 
вывести недостающую сумму с биржи, вывести сообщение о выводе и прибавить к балансу сумму вывода.

- Если цена на газ ниже 25, то программа запускает мост Scroll, расходы должны вычитаться с баланса.
- Если цена на газ ниже 15, то после запуска моста программа должна еще сминтить домен Clusters, расходы должны вычитаться с баланса.
- Если цена на газ выше 25, то программа запускает свап внутри Scroll, расходы должны вычитаться с баланса.
- Если цена на газ выше 50, то программа ничего не делает и рекомендует поработать в другой раз.
В конце программа выводит сообщение о завершении работы, указывает выполненные операции и оставшийся баланс кошелька."""

import random

gas_price = random.randint(10, 100)
wallet_balance = random.randint(2000, 10000)

scroll_bridge = gas_price * 75
scroll_swap = gas_price * 40
clusters_mint = gas_price * 100

print(f"Цена газа сейчас: {gas_price}")
print(f"Ваш баланс сейчас: {wallet_balance}$")
print("Запускаем работу...")

if gas_price < 25:
    if wallet_balance < scroll_bridge:
        difference = scroll_bridge - wallet_balance
        wallet_balance += difference
        print(f"У тебя на кошельке не хватает {difference}$ для выполнения бриджа. Выводим с биржи...")
    wallet_balance = wallet_balance - scroll_bridge
    print(f"Делаем бридж Scroll: {gas_price} * 75 = {scroll_bridge}, Остаток: {wallet_balance}$")

if gas_price < 15:
    if wallet_balance < clusters_mint:
        difference = clusters_mint - wallet_balance
        wallet_balance += difference
        print(f"У тебя на кошельке не хватает {difference}$ для выполнения минта. Выводим с биржи...")
    wallet_balance = wallet_balance - clusters_mint
    print(f"Делаем минт Clusters: {gas_price} * 40 = {clusters_mint}, Остаток: {wallet_balance}$")

if 50 > gas_price > 25:
    if wallet_balance < scroll_swap:
        difference = scroll_swap - wallet_balance
        wallet_balance += difference
        print(f"У тебя на кошельке не хватает {difference}$ для выполнения свапа. Выводим с биржи...")
    wallet_balance = wallet_balance - scroll_swap
    print(f"Делаем свап в Scroll: {gas_price} * 100 = {scroll_swap}, Остаток: {wallet_balance}$")

if gas_price > 50:
    print(f"Ебу дал? Газ = {gas_price}. Очень дорого, иди отдохни и возвращайся позже.")

print(f"Работа завершена, оставшийся баланс: {wallet_balance}$. Были выполнены: {'Scroll бридж' if gas_price < 25 else 'Scroll бридж мы не делали'}, {'Минт Clusters' if gas_price < 15 else 'Минт Clusters мы не делали'}, {'Свап' if 50 > gas_price > 25 else 'Свап мы не делали'}.")


print("-" * 50)


# задание 3
"""
У вас есть 2 переменные с балансами кошелька в токене ETH и USDC.
Еще одна переменная описывает стоимость ETH в USDC.
Напишите программу, которая будет делать обмен из ETH в USDC если баланс USDC нулевой, при этом оставляя 5% токенов ETH на комиссии
Если баланс USDC не нулевой, то программа должна делать обмен всех токенов USDC в ETH

Во время обмена должно печататься в терминале какой токен меняется на какой и какая сумма обмена

Попробуйте сделать чтобы программа делала 5 свапов подряд по условиям выше с рандомной паузой между транзакциями.

В конце работы программа должна выводить сообщение актуальный баланс токенов ETH и USDC.
"""

import time
import random

eth_price = 3000
delay = random.uniform(1, 5)

eth_balance = random.randint(0, 10)
usdc_balance = random.randint(0, 30000)

print(f"Сгенерировали ваши ETH, ваш баланс: {eth_balance} ETH")
print(f"Сгенерировали ваши USDC, ваш баланс: {usdc_balance} USDC")

for _ in range(5):

    if usdc_balance == 0:
        usdc_balance += eth_balance * 0.95 * eth_price
        eth_balance *= 0.05
        print(f"Ваш баланс USDC: {usdc_balance}.")
        print(f"Меняем {eth_balance * 19} ETH на {usdc_balance} USDC...")
        print(f"Свап завершен удачно. Ваш баланс USDC: {usdc_balance}, ETH: {eth_balance}")

    if usdc_balance > 0:
        eth_balance += usdc_balance / eth_price
        print(f"Ваш баланс USDC: {usdc_balance}.")
        print(f"Меняем {usdc_balance} USDC на {usdc_balance / eth_price} ETH...")
        usdc_balance *= 0
        print(f"Свап завершен удачно. Ваш баланс USDC: {usdc_balance}, ETH: {eth_balance}")

    print(f"Задержка на {delay:.2f} секунд")
    time.sleep(delay)

print(f"Ваш итоговый баланс: ETH: {eth_balance}, USDC: {usdc_balance}")


print("-" * 50)